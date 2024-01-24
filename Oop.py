    # program to print multiplication table of any number
class mul():
    def table(self):
        n = int(input("Enter any number:"))
        for i in range(1,11):
            ans = n*i
            print(f"{n} x {i} = {ans}")
            i+=1

    # program to find factorial of any number
class factorial():
    def facty(self):
        num = int(input("Enter any number:"))
        def fact(num):
            if num == 0:
                return 1
            else:
                return (num*fact(num-1))
        print(fact(num))

    # program to find whether the number is prime or not
class primeyy():
    def isprime(self):
        num = int(input("enter your number:"))
        if num == 1:
            print("it is not a prime number")
        if num > 1:
            for i in range(2,num):
                if num%i == 0:
                    print("it is not a prime number")
                    break
        else:
            print("it is a prime number")

    # #  or
    # num = int(input("enter the range:"))
    # for n in range(2,num):
    #     for i in range(2,n):
    #         if n%i == 0:
    #             break
    #     else:
    #         print(n)

class all_classes(mul,factorial,primeyy):
    pass
final = all_classes()
final.table()
final.facty()
final.isprime()



