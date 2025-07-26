import requests

def handler(event):
    chain = event.get("chain", "solana").lower()
    wallet = event.get("wallet", "").strip()

    if not wallet:
        return {"error": "⚠️ Please provide a wallet address."}

    if chain == "solana":
        rpc_url = "https://api.mainnet-beta.solana.com"
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [wallet]
        }

        try:
            res = requests.post(rpc_url, json=payload, timeout=5)
            res.raise_for_status()
            lamports = res.json().get("result", {}).get("value", 0)
            sol = lamports / 1_000_000_000
            return {
                "chain": "Solana",
                "wallet": wallet,
                "balance": f"{sol:.4f} SOL"
            }

        except Exception as e:
            return {"error": f"🚫 Failed to fetch balance: {str(e)}"}

    elif chain == "ethereum":
        return {
            "info": "🧪 Ethereum support coming soon. Stay tuned!"
        }

    else:
        return {
            "info": f"❌ Support for '{chain}' is not available yet."
          }
