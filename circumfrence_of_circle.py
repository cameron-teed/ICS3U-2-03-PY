#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# This program calculates the area and perimeter of a circle with the
#   radius of 20mm

import constants


def main():

    # this function calculates circumfrence

    # input
    radius = int(input("enter radius of the circle (mm): "))

    # procces

    circumfrence = constants.TAU*radius

    # output

    print("")
    print("circumfrence is {}mm^2".format(circumfrence))


if __name__ == "__main__":
    main()
