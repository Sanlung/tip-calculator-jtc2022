"""
Python program using class sructure for calculating
a dining bill and diners' shares on any percentages
of sales tax or tip, and on any given number of diners
sharing the bill, as given per the user input
"""

class Tip_Calculator():
    """define a Tip_Calculator class"""

    def __init__(self):
        """initialize class attributes"""
        self.num_of_diners = 0
        self.food_cost = 0
        self.tax_rate = 0
        self.tip_rate = 0

    def print_header_and_usage(self):
        """print header and usage instrucitons to stdout"""
        print('\n🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪',
        '🟪🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟪',
        '🟪🟨🟨🟨🟨🟨🟨🟨Tip Calculator🟨🟨🟨🟨🟨🟨🟨🟪',
        '🟪🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟪',
        '🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪',
        sep='\n', end='\n\n')

        print('Welcome, thank you for using the Tip',
        'Calculator. This program calculates the',
        'restaurant bill after tax and tip and each',
        'diner\'s share of the bill, based on the',
        'user input as to the number of diners in',
        'the party and the percentages of sales tax',
        'and tip the diners are willing to give.',
        sep='\n', end='\n\n')

    def get_food_cost(self):
        """take input of the cost of meal from user"""
        # process only valid input
        while True:
            cost_given = input('How much does the meal cost? ')
            try:
                float(cost_given)
                if float(cost_given) > 0:
                    break
                print('\nFree meal or negative cost isn\'t calculable. Let\'s try again.\n')
            except ValueError:
                self.print_error_msg()
        # store food cost in calss after validation
        self.food_cost = float(cost_given)
        # confirm input with user
        print(f'🟡 The cost of the meal is {self.food_cost}.\n')

    def get_num_of_diners(self):
        """take input of the number of diners from user"""
        # process only valid input
        while True:
            num_given = input('How many people are dining together? ')
            try:
                int(num_given)
                if int(num_given) > 0:
                    break
                print('\nAt least one person will have been dining. Let\'s try agan.\n')
            except ValueError:
                self.print_error_msg()
        # store number of diners in class after validation
        self.num_of_diners = int(num_given)
        # confirm input with user
        print(f'🟣 You have {self.num_of_diners} diner(s).\n')

    def get_tax_rate(self):
        """take input of the percentage of tax from user"""
        # process only valid input
        while True:
            tax_percentage = input('How many percent of the bill will be taxed?\nPlease give the percentage without the percentage sign >> ')
            try:
                float(tax_percentage)
                if float(tax_percentage) >= 0:
                    break
                print('\nNegative tax is impossible. Let\'s try again.\n')
            except ValueError:
                self.print_error_msg()
        # store tax percentage in class after validation
        self.tax_rate = float(tax_percentage)
        # confirm input with user
        print(f'🟠 The sales tax for the meal is {self.tax_rate}%.\n')

    def get_tip_rate(self):
        """take input of the percentage of the tip from user"""
        # process only valid input
        while True:
            tip_percentage = input('How many percent will you give for the tip?\nPlease give the percentage without the percentage sign >> ')
            try:
                float(tip_percentage)
                if float(tip_percentage) > 0:
                    break
                print('\nThe waiters/waitresses won\'t let you get away. Let\'s try again.\n')
            except ValueError:
                self.print_error_msg()
        # store tip percentage in calss after validation
        self.tip_rate = float(tip_percentage)
        # confirm input with user
        print(f'⚪️ You are willing to give a {self.tip_rate}% tip.\n')

    def print_error_msg(self):
        """print input error message to user"""
        print('\nHmm, something is wrong with that figure. Your',
            'number should be an integer (number of diners)',
            'or a floating point numder (cost and rates), and',
            'should not have letters or else. Let\'s try again.',
            sep='\n', end='\n\n')

    def get_info_and_calculate(self):
        """get user input, calculate and output results"""
        # get necessary inputs from the user
        self.get_food_cost()
        self.get_num_of_diners()
        self.get_tax_rate()
        self.get_tip_rate()
        # if all is well, calculate total bill/diners' share
        tax = self.food_cost * self.tax_rate / 100
        tip = self.food_cost * self.tip_rate / 100
        total_with_tax_and_tip = self.food_cost + tax + tip
        each_diners_share = total_with_tax_and_tip / self.num_of_diners
        # display results of calculation
        print(f'🟨 The total bill for the meal is ${round(total_with_tax_and_tip, 2)}.',
        f'🟪 And each diner should pay ${round(each_diners_share, 2)}.',
        sep='\n', end='\n\n')

    def run_calculator(self):
        # print the header and usage instructions
        self.print_header_and_usage()
        # run calculator as many times as the user want
        while True:
            self.get_info_and_calculate()
            run_again = input('Would you like to run the calculator again? (y/n) ')
            if run_again[0:1].lower() == 'n':
                break
            print()
        # print message to end program
        print('\nThank you for using the Tip Calculator. Bye.\n')

# assign an instance of class
tip_calculator = Tip_Calculator()
# run and calculate
tip_calculator.run_calculator()
