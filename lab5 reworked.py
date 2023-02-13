#Lab 5 Part B
yen = ["¥", "yen", "Yen", "YEN"]
dollar = ["$", "dollar", "Dollar", "DOLLAR"]
euro = ["€", "euro", "Euro", "EURO"]
pound = ["£", "pound", "Pound", "POUND"]
total = "Invalid"

money_amount = input("How much money do you want to convert?\n>>>")
OG_currency = input("What currency is the money you want to convert?/n>>>")
New_currency = input("What currency do you want to convert the money to?\n>>>")

def convertMoney(amount, fromInput, toInput = "yen"):
    if fromInput in yen and toInput in dollar:
        total = amount * .009
    if fromInput in yen and toInput in euro:
        total = amount * .008
    if fromInput in yen and toInput in pound:
        total = amount * .0069

    if fromInput in dollar and toInput in yen:
        total = amount * 111.58
    if fromInput in dollar and toInput in euro:
        total = amount * .89
    if fromInput in dollar and toInput in pound:
        total = amount * .77

    if fromInput in euro and toInput in yen:
        total = amount * 125.28
    if fromInput in euro and toInput in dollar:
        total = amount * 1.12
    if fromInput in euro and toInput in pound:
        total = amount * .86

    if fromInput in pound and toInput in yen:
        total = amount * 144.82
    if fromInput in pound and toInput in dollar:
        total = amount * 1.3
    if fromInput in pound and toInput in euro:
        total = amount * 1.16
    print(amount, fromInput+"(s)", "is worth", total, toInput+"(s)")

try:
    convertMoney(money_amount, OG_currency, New_currency)
except TypeError:
    print("Cannot identify money amount. Please make sure the money amount is typed as 10, not ten")
except UnboundLocalError:
    print("Cannot compute conversion. Please check the currency")