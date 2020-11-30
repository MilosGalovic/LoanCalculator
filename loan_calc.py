import math
import argparse


parser = argparse.ArgumentParser(usage="This program calculates your loan monthly payments.")


parser.add_argument("-t", "--type", choices = ["diff", "annuity"], type = str)
parser.add_argument("-p", "--principal", type = float)
parser.add_argument("-n", "--periods", type = int)
parser.add_argument("-i", "--interest", type = float)
parser.add_argument("-mp", "--payment", type = float)


args = parser.parse_args()


args_list = [args.type, args.principal, args.periods, args.interest, args.payment]
for arg in args_list:
    if arg != None and type(arg) != str:
        if arg < 0:
            print("Incorrect Parameters.")
            exit(0)

if args.type == "diff":
    if args.type and args.principal and args.periods and args.interest:
        d_sum = 0

        i = (args.interest / 100) / ((12 * 100) / 100)
        for m in range(1, args.periods + 1):
            d = math.ceil(args.principal / args.periods + i * (args.principal - (args.principal * (m - 1) / args.periods)))
            d_sum += d
            print(f"Month {m}: payment is {d}")            
        overpayment = math.ceil(d_sum - args.principal)
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters.")
        exit(0)


elif args.type == "annuity":
    if args.type and args.principal and args.payment and args.interest :
        i = (args.interest / 100) / ((12 * 100) / 100)
        n = math.log((args.payment / (args.payment - i * args.principal)), (1 + i))

        years = math.floor(round(n) / 12)
        months = (math.ceil(n) % 12)

        if years == 0:
            if months != 1:
                print(f"It will take {months} months to repay this loan!")
            else:
                print(f"It will take {months} month to repay this loan!")
        elif months == 0:
            if years != 1:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} year to repay this loan!")

        else:
            if months == 1 and years == 1:
                print( f"It will take {years} year and {months} month to repay this loan!")
            elif months == 1:
                print( f"It will take {years} years and {months} month to repay this loan!")
            elif years == 1:
                print( f"It will take {years} year and {months} months to repay this loan!")
            else:
                print( f"It will take {years} years and {months} months to repay this loan!")
                    
        overpayment = math.ceil((math.ceil(args.payment) * math.ceil(n)) - args.principal)
        print(f"Overpayment = {overpayment}")

                        
    elif args.type and args.principal and args.periods and args.interest:
        i = (args.interest / 100) / ((12 * 100) / 100)
        a = args.principal * (i * ((1 + i) ** args.periods)) / (((1 + i) ** args.periods) - 1)
        print(f"Your annuity payment = {math.ceil(a)}!")
        overpayment = math.ceil((math.ceil(a) * args.periods) - args.principal)
        print(f"Overpayment = {overpayment}")


            
    elif args.type and args.payment and args.periods and args.interest :
        i = (args.interest / 100) / ((12 * 100) / 100)
        p = args.payment / ((i * ((1 + i) ** args.periods)) / (((1 + i) ** args.periods) - 1))
        print(f"Your loan principal = {math.floor(p)}!")

        overpayment = math.ceil((args.payment * args.periods) - (math.floor(p)))
        print(f"Overpayment = {overpayment}")

    else:
        print("Incorrect parameters.")
        exit(0)

else:
    print("Incorrect parameters.")
    exit(0)
    
