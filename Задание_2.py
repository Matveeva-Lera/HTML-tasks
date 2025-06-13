wage=int(input("Введите заработную плату в месяц: "))
p_bank=int(input("Введите ежемесячный платеж в банке: "))
p=int(input("Введите задолженность за коммунальные услуги: "))
balance=wage-p_bank-p
print("Остаток суммы: ", balance)
