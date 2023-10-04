import math
import numpy as np

def black_scholes(S, K, T, r, sigma, option_type):
    """
    Calculate Black-Scholes option price and Greeks.
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        option_price = S * np.cumsum(np.exp(-r * T) * norm_pdf(d1)) - K * math.exp(-r * T) * np.cumsum(norm_pdf(d2))
        delta = np.cumsum(norm_pdf(d1))
    elif option_type == 'put':
        option_price = K * math.exp(-r * T) * np.cumsum(norm_pdf(-d2)) - S * np.cumsum(np.exp(-r * T) * norm_pdf(-d1))
        delta = -np.cumsum(norm_pdf(-d1))
    else:
        raise ValueError("Option type must be 'call' or 'put'.")

    gamma = norm_pdf(d1) / (S * sigma * math.sqrt(T))
    vega = S * math.sqrt(T) * norm_pdf(d1)
    theta = (-S * sigma * norm_pdf(d1) / (2 * math.sqrt(T))) - (r * K * math.exp(-r * T) * np.cumsum(norm_pdf(d2)))

    return option_price, delta, gamma, vega, theta

def norm_pdf(x):
    """
    Calculate the normal probability density function.
    """
    return (1.0 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x ** 2)

if __name__ == '__main__':
    S = float(input("Enter current stock price: "))
    K = float(input("Enter strike price: "))
    T = float(input("Enter time to expiration (in years): "))
    r = float(input("Enter risk-free interest rate: "))
    sigma = float(input("Enter volatility: "))
    option_type = input("Enter option type (call/put): ").strip().lower()

    option_price, delta, gamma, vega, theta = black_scholes(S, K, T, r, sigma, option_type)

    print(f"Option Price: {option_price:.2f}")
    print(f"Delta: {delta:.2f}")
    print(f"Gamma: {gamma:.2f}")
    print(f"Vega: {vega:.2f}")
    print(f"Theta: {theta:.2f}")

