'''
Prompts for hourly pay rate and hours worked and computes total pay with overtime of 1.5 * base pay when over 40 hours
'''

def CalcPay(pay, time):
    if time <= 40:
        gross = time * pay
    else: gross = ((40 * pay) + ((time - 40) * pay * 1.5))
    print('\nYour pay is: $' + "{:.2f}".format(gross))
        
print('This program calculates your pay based off of your pay rate and hours worked.')
while(True):
    rate = float(input('\n\nEnter your hourly pay or 0 to exit: '))
    if rate == 0:
        break
    hours = float(input('\nEnter your hours worked this week: '))
    CalcPay(rate, hours)
    