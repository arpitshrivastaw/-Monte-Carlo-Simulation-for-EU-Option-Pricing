import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo Option Pricing

S0 = 100       # initial stock price
K = 105        # strike price
r = 0.05       # risk-free rate
sigma = 0.2    # volatility
T = 1.0        # time to maturity (1 year)
num_simulations = 100000  # number of Monte Carlo paths

# Step 1: Simulate end-of-period stock prices using GBM
Z = np.random.standard_normal(num_simulations)
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)

# Step 2: Compute payoffs
call_payoff = np.maximum(ST - K, 0)
put_payoff = np.maximum(K - ST, 0)

# Step 3: Discount back to present value
call_price = np.exp(-r * T) * np.mean(call_payoff)
put_price = np.exp(-r * T) * np.mean(put_payoff)

print(f"Monte Carlo European Call Price: {call_price:.4f}")
print(f"Monte Carlo European Put Price: {put_price:.4f}")

# Step 4: Plot results
plt.hist(ST, bins=50, alpha=0.7, edgecolor='black')
plt.title('Simulated Stock Prices at Maturity (Monte Carlo)')
plt.xlabel('Stock Price at T')
plt.ylabel('Frequency')
plt.show()
