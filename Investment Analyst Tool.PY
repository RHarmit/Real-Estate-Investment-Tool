import numpy as np
import numpy_financial as npf  # Import numpy_financial for financial functions

def calculate_npv(discount_rate, cash_flows):
    """
    Calculates the Net Present Value (NPV).
    """
    npv = sum(cf / ((1 + discount_rate) ** i) for i, cf in enumerate(cash_flows, start=1))
    return npv

def calculate_irr(cash_flows):
    """
    Calculates the Internal Rate of Return (IRR).
    """
    irr = npf.irr(cash_flows)  # Use numpy_financial's IRR function
    return irr

def calculate_cash_on_cash(initial_investment, annual_cash_flow):
    """
    Calculates the Cash-on-Cash Return.
    """
    return (annual_cash_flow / initial_investment) * 100

def calculate_cap_rate(annual_income, property_value):
    """
    Calculates the Capitalization Rate (Cap Rate).
    """
    return (annual_income / property_value) * 100

def main():
    print("Real Estate Investment Analysis Tool")
    print("-----------------------------------")
    
    # User inputs
    discount_rate = float(input("Enter the discount rate (as a decimal, e.g., 0.08 for 8%): "))
    num_years = int(input("Enter the number of years: "))
    print("Enter the cash flows for each year:")
    cash_flows = [float(input(f"Year {i + 1}: ")) for i in range(num_years)]
    initial_investment = float(input("Enter the initial investment amount: "))
    annual_cash_flow = float(input("Enter the expected annual cash flow: "))
    property_value = float(input("Enter the property value: "))
    annual_income = float(input("Enter the expected annual income: "))

    # Calculations
    npv = calculate_npv(discount_rate, cash_flows)
    irr = calculate_irr([-initial_investment] + cash_flows)
    cash_on_cash = calculate_cash_on_cash(initial_investment, annual_cash_flow)
    cap_rate = calculate_cap_rate(annual_income, property_value)

    # Display results
    print("\nInvestment Analysis Results:")
    print(f"Net Present Value (NPV): ${npv:,.2f}")
    print(f"Internal Rate of Return (IRR): {irr * 100:.2f}%")
    print(f"Cash-on-Cash Return: {cash_on_cash:.2f}%")
    print(f"Capitalization Rate (Cap Rate): {cap_rate:.2f}%")

if __name__ == "__main__":
    main()
