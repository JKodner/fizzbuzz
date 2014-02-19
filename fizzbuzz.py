"""FizzBuzz is a commonThe "Fizz-Buzz test" is an interview question designed to help filter out the 99.5% of programming job candidates who can't seem to program their way out of a wet paper bag. The text of the programming assignment is as follows:
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

I managed to come up with two of my own solutions. I had absolutely no help. It took a few tries but I finally got it to work!"""

# Here is my First Program:
i = range(1, 101)
for x in i:
    if x % 3 == 0:
        if x % 5 == 0:
            print "FizzBuzz"
        else:
            print "Fizz"
    elif x % 5 == 0:
        print "Buzz"
    else:
        print x

# Here is my Second Program:
i = range(1, 101)
for x in i:
    if x % 3 == 0:
        if x % 5 == 0:
            x = "FizzBuzz"
            print x
        else:
            x = "Fizz"
            print x
    elif x % 5 == 0:
        x = "Buzz"
        print x
    else:
        print x