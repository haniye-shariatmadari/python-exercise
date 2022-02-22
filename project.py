# zoj va fard

# print("enter your number:")

# x=int(input())
# if (x%2 )== 0:

    # print("zoje")
# else:
    # print("fard")
# 


# # x=2
# y=4
# z=6
# print(max(x, y, z))


#  تشخیص اعداد بزرگتر
# print(" enter number 1")
# x=int (input())
# print(" enter number 2")
# y=int (input())
# print(" enter number 3")
# z=int (input())

# print(max(x,y,z))



n = int(input("enter a number:"))
for i in range (n):
    for j in range (i):
        print (" ", end = " ")
    for j in range (i,n):
        print ("*", end = " ")
    print()
    # fghjk



n = int(input("enter a number:"))
for i in range (n):
    for j in range (i,n):
        print ("*", end = " ")
    print()