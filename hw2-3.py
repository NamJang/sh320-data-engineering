if __name__ == '__main__':
    hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
    prices = [30, 25, 40, 20, 20, 35, 50, 35]
    last_week = [2, 3, 5, 8, 4, 4, 6, 2]

    total_price = 0

    for i in prices:
        total_price += i
    average_price = total_price / len(prices)
    print(f"Average price is {average_price}")
    new_prices = [i-5 for i in prices]
    print(new_prices)

    total_revenue = 0
    for i in range(0, len(hairstyles)):
        total_revenue += prices[i] * last_week[i]
    print(total_revenue)
    print(f'Average daily revenue is {total_revenue/7}')

    cuts_under_30 = []
    for i in range(0, len(hairstyles)):
        if(new_prices[i]<30):
            cuts_under_30.append(hairstyles[i])
    print(cuts_under_30)
