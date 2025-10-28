# Monte Carlo Option Pricing

This project implements a Monte Carlo simulation for pricing European Call and Put options. The Monte Carlo method is a powerful numerical technique that uses random sampling to obtain numerical results, particularly useful in option pricing where analytical solutions may be complex or unavailable.

## 📊 Features

- European Call and Put option pricing using Monte Carlo simulation
- Geometric Brownian Motion (GBM) for stock price path simulation
- Visual representation of simulated stock prices at maturity
- Configurable parameters for flexible option pricing scenarios

## 🔧 Prerequisites

To run this project, you need Python 3.x installed on your system along with the following packages:

```bash
numpy      # For numerical computations
matplotlib # For plotting results
```

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/monte_carlo_option_pricing.git
cd monte_carlo_option_pricing
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the script using Python:

```bash
python monte_carlo_option_pricing.py
```

The script uses the following default parameters which can be modified in the code:
- Initial Stock Price (S0): $100
- Strike Price (K): $105
- Risk-free Rate (r): 5%
- Volatility (σ): 20%
- Time to Maturity (T): 1 year
- Number of Simulations: 100,000

## 📈 Output

The program will output:
1. The calculated European Call option price
2. The calculated European Put option price
3. A histogram plot showing the distribution of simulated stock prices at maturity

## 🧮 Mathematical Background

The Monte Carlo simulation uses the following formula for stock price simulation:

ST = S0 * exp((r - 0.5 * σ²) * T + σ * √T * Z)

Where:
- ST is the stock price at maturity
- S0 is the initial stock price
- r is the risk-free rate
- σ is the volatility
- T is the time to maturity
- Z is a random number from standard normal distribution

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
