# Monte Carlo Simulation for European Option Pricing

This project implements a **Monte Carlo simulation** to estimate the fair price of a **European call and put option** under the **Black–Scholes model**.

---

## 📘 Overview
Monte Carlo methods simulate thousands of random future price paths of a stock to approximate the expected payoff of an option. This method is widely used in **quantitative finance** for pricing complex derivatives where analytical formulas are hard to apply.

---

## ⚙️ Mathematical Background

The stock price \( S_t \) follows:
\[
dS_t = \mu S_t dt + \sigma S_t dW_t
\]

The analytical solution is:
\[
S_T = S_0 \exp\left[\left(\mu - \frac{1}{2}\sigma^2\right)T + \sigma \sqrt{T} Z \right]
\]
where \( Z \sim N(0,1) \).

The discounted expected payoff of a European Call is:
\[
C = e^{-rT} \mathbb{E}[\max(S_T - K, 0)]
\]

---

## 🧠 Parameters

| Parameter | Meaning |
|------------|----------|
| `S0` | Initial stock price |
| `K` | Strike price |
| `r` | Risk-free interest rate |
| `sigma` | Volatility |
| `T` | Time to maturity (in years) |
| `num_simulations` | Number of Monte Carlo runs |

---

## 🧩 Code Example

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 100       # initial stock price
K = 105        # strike price
r = 0.05       # risk-free rate
sigma = 0.2    # volatility
T = 1.0        # time to maturity (1 year)
num_simulations = 100000  # number of Monte Carlo paths

# Step 1: Simulate end-of-period stock prices using GBM
Z = np.random.standard_normal(num_simulations)
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)

# Step 2: Compute payoffs for call and put
call_payoff = np.maximum(ST - K, 0)
put_payoff = np.maximum(K - ST, 0)

# Step 3: Discounted mean payoff
call_price = np.exp(-r * T) * np.mean(call_payoff)
put_price = np.exp(-r * T) * np.mean(put_payoff)

print(f"Monte Carlo European Call Price: {call_price:.4f}")
print(f"Monte Carlo European Put Price: {put_price:.4f}")

# Step 4: Visualize distribution of simulated prices
plt.hist(ST, bins=50, alpha=0.7)
plt.title("Simulated Stock Prices at Maturity (Monte Carlo)")
plt.xlabel("Stock Price at T")
plt.ylabel("Frequency")
plt.show()
```

---

## 📊 Example Output
```
Monte Carlo European Call Price: 8.0451
Monte Carlo European Put Price: 7.9924
```

---

## 💡 Possible Extensions
- Compare results with **Black–Scholes closed-form formula**
- Implement **Antithetic Variates** for variance reduction
- Explore **Asian or Barrier options**
- Add **convergence plots** to show simulation accuracy

---

## 🧰 Requirements
Install dependencies with:
```
pip install -r requirements.txt
```
# -Monte-Carlo-Simulation-for-EU-Option-Pricing
