# Black-Scholes Option Pricing

This Python script calculates option prices and various Greeks (Delta, Gamma, Vega, Theta) using the Black-Scholes option pricing model. The Black-Scholes model is a widely used mathematical model for estimating the theoretical price of financial options.

## Usage

1. Make sure you have Python and NumPy installed on your system.
2. Run the script in your terminal or Python environment.
3. Enter the required parameters such as the current stock price, strike price, time to expiration, risk-free interest rate, volatility, and option type (call or put).
4. The script will calculate and display the option price along with Delta, Gamma, Vega, and Theta.

## Parameters

- `S`: Current stock price.
- `K`: Strike price.
- `T`: Time to expiration (in years).
- `r`: Risk-free interest rate.
- `sigma`: Volatility of the underlying asset.
- `option_type`: Type of option ('call' for call option, 'put' for put option).

## Greeks

- **Delta**: Measures the sensitivity of the option price to changes in the underlying asset's price.
- **Gamma**: Measures the rate of change of Delta with respect to changes in the underlying asset's price.
- **Vega**: Measures the sensitivity of the option price to changes in volatility.
- **Theta**: Measures the rate of change of the option price with respect to time decay.

## Example

Here's an example of how to use the script:

```python
python black_scholes_option_pricing.py
Enter current stock price: 100
Enter strike price: 110
Enter time to expiration (in years): 1
Enter risk-free interest rate: 0.05
Enter volatility: 0.2
Enter option type (call/put): call
Option Price: 8.22
Delta: 0.64
Gamma: 0.03
Vega: 39.91
Theta: -7.76
```

## License
MIT
