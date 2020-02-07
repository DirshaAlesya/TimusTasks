banks = [int(i) for i in input('').split(' ')]
summ = sum(banks) - 1
for bank in banks:
    print(summ-bank)