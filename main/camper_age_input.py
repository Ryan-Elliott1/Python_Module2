"""
Program: camper_age_input.py
Author: Ryan Elliott
Last date modified: 06/03/2020

The purpose of this program is to use the convert_to_months function to convert the users input into a number of months
input number of years
outputs users years into months
"""


def convert_to_months(years):
    months_in_year = 12
    months = years * months_in_year
    return months


if __name__ == '__main__':
    print('Enter a number:')
    # get user input
    age_in_years = input()
    # convert user input
    age_in_months = convert_to_months(int(age_in_years))
    print(age_in_years, "years is equal to", age_in_months, "months.")

