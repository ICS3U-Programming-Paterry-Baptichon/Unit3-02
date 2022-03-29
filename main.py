# Created by: Paterry Baptichon
# Created on : 2022-03-28
# This program checks if there is over 30 students


import constants


def main():
    # this function checks if there is over 30 students

    # input
    Lucky_number = int(input("Enter the number between 1-9: "))
    print("")

    # process & output
    if Lucky_number == constants.MY_LUCKY_NUMBER:
        print("correct")
    else:
      print("Not correct!!")


if __name__ == "__main__":
    main()
  