# -*- coding: utf8 -*-

#현금 카드 모튤을 불러 들임
import CashCard as CashCard_module


def chk_bal(message, account)
    """
    Print message and value
    :param message:
    :param account:
    :return:
    """
    print("%s : %d" % (message, account.check_balance()))


#현금 카드 모듈의 잔액 확인
chk_bal("CashCard_module 잔액 확인", CashCard_module)
# 현금 카드에 10000원 입금
print "10000원 입금"


CashCard_module.deposit(10000)



chk_bal("입금 후 잔고 확인", CashCard_module)

print ("1000원 출금")


CashCard_module.withdraw(1000)



chk_bal("출금 후 잔고 확인", CashCard_module)



import CashCard as mySistersCard_module

chk_bal("CashCard_module 잔액 확인", CashCard_module)
