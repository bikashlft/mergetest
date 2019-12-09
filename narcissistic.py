#This is comment by user1
#This is comment by user2
def main():

    for i in range(1,1000):
        temp = i
        power = len(str(i))
        #print(power)
        sum = 0
        while (temp != 0):
            rem = temp % 10
            #print ("rem:",rem)
            sum += rem ** power
            #print ("sum:",sum)
            temp = temp // 10
            #print ("temp:",temp)
        if (sum == i):
            print(i, "is a narcissistic no.")





if __name__ == '__main__':
    main()