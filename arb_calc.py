import streamlit as st

def arbitrage_calculator(odds_A, odds_B, total_budget):
    # Check if an arbitrage opportunity exists
    if odds_A * odds_B - odds_A - odds_B > 0:
        # Calculate the payout (P) for both outcomes
        payout = total_budget / (1 / odds_A + 1 / odds_B)
        # Calculate the amount to bet on each outcome
        bet_A = payout / odds_A
        bet_B = payout / odds_B
        # Calculate profit
        profit = payout - total_budget
        return {
            'Arbitrage Opportunity': True,
            'Bet on outcome A': round(bet_A, 2),
            'Bet on outcome B': round(bet_B, 2),
            'Total payout (same for both outcomes)': round(payout, 2),
            'Profit': round(profit, 2)
        }
    else:
        return {
            'Arbitrage Opportunity': False,
            'Message': "No arbitrage opportunity exists with the given odds."
        }

def main():
    st.title("Arbitrage Calculator")
    
    st.write("This app calculates potential arbitrage opportunities based on the odds for two outcomes and your total budget.")
    
    odds_A = st.number_input("Enter odds for outcome A:", min_value=1.0, value=2.0, step=0.1)
    odds_B = st.number_input("Enter odds for outcome B:", min_value=1.0, value=2.0, step=0.1)
    total_budget = st.number_input("Enter your total budget:", min_value=0.0, value=100.0, step=10.0)
    
    if st.button("Calculate Arbitrage"):
        result = arbitrage_calculator(odds_A, odds_B, total_budget)
        
        if result['Arbitrage Opportunity']:
            st.success("Arbitrage Opportunity Found!")
            st.write(f"Bet on outcome A: ${result['Bet on outcome A']}")
            st.write(f"Bet on outcome B: ${result['Bet on outcome B']}")
            st.write(f"Total payout: ${result['Total payout (same for both outcomes)']}")
            st.write(f"Profit: ${result['Profit']}")
        else:
            st.warning(result['Message'])

if __name__ == "__main__":
    main()