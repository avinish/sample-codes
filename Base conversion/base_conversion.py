#########################################################
#
# Base conversion algorithm
#
# Function Name : base_conversion
#
# Parameters :
#    Number : number need to be converted
#    BaseFrom : Base of current number
#    BaseTo : Base need to be converted
#
# Author : Avinish Mishra
#
# License : GPL License
#
# You can use this code for your reference. I will be more than happy.
#########################################################

def base_conversion(number, BaseFrom, BaseTo):

    def base_converion_from_10(number, BaseFrom, BaseTo):
        convno = 0
        count = 0
        remainingnumber = number
        while remainingnumber / BaseTo != 0:
            remainder = remainingnumber % BaseTo
            remainingnumber = remainingnumber // BaseTo
            convno += (BaseFrom ** count) * remainder
            count += 1
        return convno

    def base_conversion_to_10(number, BaseFrom, BaseTo):
        convNo = 0
        count = 0
        remainingNumber = number
        while remainingNumber / 10 != 0:
            remainder = remainingNumber % 10
            remainingNumber = remainingNumber // 10
            convNo += (BaseFrom ** count) * remainder
            count += 1
        return convNo

    if BaseTo == 10:
        return base_conversion_to_10(number,BaseFrom,BaseTo)
    if BaseFrom == 10:
        return base_converion_from_10(number,BaseFrom,BaseTo)

    #if baseFrom and baseTo != 10, the first convert baseFrom to 10 and then change it baseTo
    return base_converion_from_10(base_conversion_to_10(number,BaseFrom,10),10,BaseTo)


if __name__ == '__main__':
    number = 14
    baseFrom = 16
    baseTo = 7
    print("Number {} base {} converted number {} base {}".format (number,baseFrom,base_conversion(number,baseFrom,baseTo),baseTo))
