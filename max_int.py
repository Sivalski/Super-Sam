num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0
num = 0
while num >= 0:
    #Max number, if number is higher then current max, we are going to store num as new max_num
    if num_int > max_int:
        max_int = num_int
        num_int = int(input("Input a number: "))
    print("The maximum is", max_int)    # Do not change this line
else: