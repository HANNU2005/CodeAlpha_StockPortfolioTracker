import csv
from datetime import datetime

def get_stock_prices():
    """
    Returns a dictionary with hardcoded stock prices.
    In a real application, this would fetch live data from an API.
    """
    return {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "GOOGL": 135.20,
        "MSFT": 415.30,
        "AMZN": 145.80,
        "NVDA": 875.20,
        "META": 325.60,
        "NFLX": 485.90,
        "AMD": 142.35,
        "INTC": 45.20
    }

def display_available_stocks(stock_prices):
    """
    Display all available stocks and their current prices.
    """
    print("\n📈 Available Stocks and Current Prices:")
    print("-" * 40)
    for symbol, price in stock_prices.items():
        print(f"{symbol}: ${price:.2f}")
    print("-" * 40)

def get_user_portfolio():
    """
    Get stock holdings from user input.
    Returns a dictionary with stock symbols as keys and quantities as values.
    """
    portfolio = {}
    stock_prices = get_stock_prices()
    
    print("\n🎯 Build Your Portfolio")
    print("Enter stock symbol and quantity. Type 'done' when finished.")
    
    while True:
        stock_symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        
        if stock_symbol == 'DONE':
            break
        
        if stock_symbol not in stock_prices:
            print(f"❌ '{stock_symbol}' is not available. Please choose from the list above.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity of {stock_symbol} shares: "))
            if quantity <= 0:
                print("❌ Quantity must be a positive number.")
                continue
            
            if stock_symbol in portfolio:
                portfolio[stock_symbol] += quantity
                print(f"✅ Added {quantity} more shares of {stock_symbol}. Total: {portfolio[stock_symbol]}")
            else:
                portfolio[stock_symbol] = quantity
                print(f"✅ Added {quantity} shares of {stock_symbol}")
                
        except ValueError:
            print("❌ Please enter a valid number for quantity.")
    
    return portfolio

def calculate_portfolio_value(portfolio, stock_prices):
    """
    Calculate total portfolio value and return detailed breakdown.
    """
    portfolio_details = []
    total_value = 0
    
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value = quantity * price
        total_value += value
        
        portfolio_details.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'value': value
        })
    
    return portfolio_details, total_value

def display_portfolio(portfolio_details, total_value):
    """
    Display portfolio summary in a formatted table.
    """
    print("\n" + "="*60)
    print("📊 PORTFOLIO SUMMARY")
    print("="*60)
    print(f"{'Stock':<8} {'Quantity':<10} {'Price':<12} {'Total Value':<15}")
    print("-"*60)
    
    for stock in portfolio_details:
        print(f"{stock['symbol']:<8} {stock['quantity']:<10} ${stock['price']:<11.2f} ${stock['value']:<14.2f}")
    
    print("-"*60)
    print(f"{'TOTAL PORTFOLIO VALUE:':<45} ${total_value:.2f}")
    print("="*60)

def save_to_file(portfolio_details, total_value):
    """
    Save portfolio data to either a TXT or CSV file based on user preference.
    """
    while True:
        file_choice = input("\nSave portfolio to file? (txt/csv/no): ").lower().strip()
        
        if file_choice == 'no':
            return
        
        if file_choice not in ['txt', 'csv']:
            print("Please choose 'txt', 'csv', or 'no'.")
            continue
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if file_choice == 'txt':
            filename = f"portfolio_{timestamp}.txt"
            save_to_txt(portfolio_details, total_value, filename)
        else:
            filename = f"portfolio_{timestamp}.csv"
            save_to_csv(portfolio_details, total_value, filename)
        
        print(f"✅ Portfolio saved to {filename}")
        break

def save_to_txt(portfolio_details, total_value, filename):
    """
    Save portfolio to a text file.
    """
    with open(filename, 'w') as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 50 + "\n")
        file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        file.write(f"{'Stock':<8} {'Quantity':<10} {'Price':<12} {'Total Value':<15}\n")
        file.write("-" * 50 + "\n")
        
        for stock in portfolio_details:
            file.write(f"{stock['symbol']:<8} {stock['quantity']:<10} ${stock['price']:<11.2f} ${stock['value']:<14.2f}\n")
        
        file.write("-" * 50 + "\n")
        file.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")

def save_to_csv(portfolio_details, total_value, filename):
    """
    Save portfolio to a CSV file.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value'])
        
        # Write data
        for stock in portfolio_details:
            writer.writerow([stock['symbol'], stock['quantity'], stock['price'], stock['value']])
        
        # Write total
        writer.writerow(['', '', 'TOTAL:', total_value])

def main():
    """
    Main function to run the stock portfolio tracker.
    """
    print("💰 Welcome to Stock Portfolio Tracker!")
    print("Track your investments and calculate total portfolio value.")
    
    stock_prices = get_stock_prices()
    
    while True:
        display_available_stocks(stock_prices)
        
        # Get user's portfolio
        portfolio = get_user_portfolio()
        
        if not portfolio:
            print("No stocks added to portfolio.")
            break
        
        # Calculate portfolio value
        portfolio_details, total_value = calculate_portfolio_value(portfolio, stock_prices)
        
        # Display results
        display_portfolio(portfolio_details, total_value)
        
        # Optional: Save to file
        save_to_file(portfolio_details, total_value)
        
        # Ask if user wants to create another portfolio
        while True:
            again = input("\nCreate another portfolio? (yes/no): ").lower().strip()
            if again in ['yes', 'y']:
                print("\n" + "="*60 + "\n")
                break
            elif again in ['no', 'n']:
                print("Thank you for using Stock Portfolio Tracker!")
                return
            else:
                print("Please enter 'yes' or 'no'.")

# Run the program if this script is executed directly
if __name__ == "__main__":
    main()