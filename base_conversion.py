
def base_conversion_to_10 (number, BaseFrom, BaseTo):
    convNo = 0
    count = 0
    remainingNumber = number
    while remainingNumber / 10 != 0:
        remainder = remainingNumber % 10
        # print ("Remainder {}".format(remainder))
        remainingNumber = remainingNumber // 10
        # print ("Remaining Number {}".format(remainingNumber))
        convNo += (BaseFrom ** count) * remainder
        # print ("Conversion number {}".format(convNo))
        count += 1
    return convNo

def base_converion_from_10 (number, BaseFrom, BaseTo):
    convNo = 0
    count = 0
    remainingNumber = number
    while remainingNumber / baseTo != 0:
        remainder = remainingNumber % baseTo
        # print ("Remainder {}".format(remainder))
        remainingNumber = remainingNumber // baseTo
        # print ("Remaining Number {}".format(remainingNumber))
        convNo += (BaseFrom ** count) * remainder
        # print ("Conversion number {}".format(convNo))
        count += 1
    return convNo

def base_conversion(number, BaseFrom, BaseTo):
    if BaseTo == 10:
        return base_conversion_to_10(number,baseFrom,baseTo)
    if BaseFrom == 10:
        return base_converion_from_10(number,baseFrom,baseTo)

    #if baseFrom and baseTo != 10, the first convert baseFrom to 10 and then change it baseTo
    return base_converion_from_10(base_conversion_to_10(number,baseFrom,10),10,BaseTo)


if __name__ == '__main__':
    number = 26
    baseFrom = 7
    baseTo = 16
    print("Number {} base {} converted number {} base {}".format (number,baseFrom,base_conversion(number,baseFrom,baseTo),baseTo))
