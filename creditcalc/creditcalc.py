import math
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Credit calculator!")
    parser.add_argument("-t", "--type", choices=["diff","annuity"], help="indicates the type of payments")
    parser.add_argument("-p", "--payment",type = int, help="monthly payment", default= 0)
    parser.add_argument("-pr", "--principal", type = int, help="principal value", default= 0)
    parser.add_argument("-per","--periods",type = int, help="number of months and/or years needed to repay the credit", default= 0)
    parser.add_argument("-i", "--interest", type = float, help="interest rate",default=0)
    args = parser.parse_args()

    if len(sys.argv) - 1 != 4:
        print("Incorrect parameters")
        exit()
    if not args.type:
        print("Incorrect parameters")
        exit()
    if args.type == "diff" and args.payment != 0:
        print("Incorrect parameters")
        exit()
    if args.interest == 0:
        print("Incorrect parameters")
        exit()
    if args.payment < 0 or args.principal < 0 or args.periods < 0 or args.interest < 0:
        print("Incorrect parameters")
        exit()
    if args.type == "annuity":
        if args.payment == 0:
            count_monthly_payment_annuity(args.principal, args.periods, args.interest)
        if args.principal == 0:
            count_credit_principal_annuity(args.payment, args.periods, args.interest)
        if args.periods == 0:
            count_period_annuity(args.principal, args.payment, args.interest)
    elif args.type == "diff":
        differentiate_payment(args.principal, args.interest, args.periods)



def count_period_annuity(principal, payment, interest):
    interest = (float(interest) / 100) * (1 / 12)
    number_payments = math.log((float(payment) / (float(payment) - interest * float(principal))), 1 + interest)
    if number_payments == 12:
        print("You need {} year to repay this credit!".format(int(number_payments / 12)))
    elif number_payments > 12:
        number_payments = math.ceil(number_payments)
        if number_payments // 2 == 0:
            print("You need {} years to repay this credit!".format(int(number_payments / 12)))
        else:
            result_ = math.ceil(((number_payments / 12) % 2) * 10) + 1
            print("You need {} years and {} months to repay this credit!".format(int(number_payments / 12), result_))
    elif number_payments < 12:
        if number_payments == 1:
            print("You need {} month to repay this credit!".format(int(number_payments)))
        else:
            print("You need {} months to repay this credit!".format(int(number_payments)))
    overpayment = (payment * number_payments) - principal
    print("Overpayment  = {}".format(math.ceil(overpayment)))

def count_monthly_payment_annuity(principal, periods, interest):
    interest = (float(interest) / 100) * (1 / 12)
    annuity_payment = int(principal) * float((interest * (1 + interest) ** int(periods))) / float((((1 + interest) ** int(periods)) - 1))
    overpayment = (math.ceil(annuity_payment) * periods) - principal
    print("Your annuity payment = {}!".format(math.ceil(annuity_payment)))
    print("Overpayment  = {}".format(math.ceil(overpayment)))


def count_credit_principal_annuity(payment, periods, interest):
    interest = (float(interest) / 100) * (1 / 12)
    principal = float(payment) / ((float(interest) * (1 + float(interest)) ** int(periods)) / ((1 + float(interest)) ** int(periods) - 1))
    overpayment = (payment * periods) - principal
    print("Your credit principal = {}!".format(int(principal)))
    print("Overpayment  = {}".format(math.ceil(overpayment)))

def differentiate_payment(principal, interest, periods):
    interest = (float(interest) / 100) * (1 / 12)
    current_period = 1
    result = 0
    while current_period <= periods:
        payment = principal / periods + interest * (principal - (principal * (current_period - 1)) / periods)
        result += math.ceil(payment)
        print("Month {}: paid out {}".format(current_period, math.ceil(payment)))
        current_period += 1
    result = result - principal
    print("Overpayment  = {}".format(math.ceil(result)))

main()
