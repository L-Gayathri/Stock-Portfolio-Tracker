import yfinance as yf
from prettytable import PrettyTable
<link rel="
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        """Add a stock to the portfolio."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol} to your portfolio.")

    def remove_stock(self, symbol, quantity):
        """Remove a stock from the portfolio."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from your portfolio.")
            else:
                self.portfolio[symbol] -= quantity
                print(f"Removed {quantity} shares of {symbol} from your portfolio.")
        else:
            print(f"{symbol} is not in your portfolio.")

    def view_portfolio(self):
        """Display the portfolio with real-time data."""
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        table = PrettyTable()
        table.field_names = ["Stock", "Quantity", "Current Price", "Total Value"]
        total_value = 0

        for symbol, quantity in self.portfolio.items():
            try:
                stock = yf.Ticker(symbol)
                price = stock.history(period="1d")['Close'].iloc[-1]
                total_stock_value = price * quantity
                total_value += total_stock_value
                table.add_row([symbol, quantity, f"${price:.2f}", f"${total_stock_value:.2f}"])
            except Exception as e:
                table.add_row([symbol, quantity, "N/A", "N/A"])
                print(f"Error fetching data for {symbol}: {e}")

        print(table)
        print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




































