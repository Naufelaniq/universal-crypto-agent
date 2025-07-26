# Universal Crypto Agent 🧠💸

Check wallet balances directly from Solana (Ethereum coming soon).  
Built to be used as a backend server for ChainOpera Agents.

---

## 🔍 Features

- ✅ Supports Solana mainnet  
- 📥 Input: Wallet address  
- 📤 Output: SOL balance (with 4 decimal places)  
- ⏱️ Fast & lightweight API logic  
- 🔐 Ethereum support coming soon

---

## ⚙️ How It Works

The `handler.py` file takes this input:

```json
{
  "chain": "solana",
  "wallet": "YourWalletAddressHere"
}
And returns:

```json
{
  "chain": "Solana",
  "wallet": "YourWalletAddressHere",
  "balance": "1.2345 SOL"
}
```