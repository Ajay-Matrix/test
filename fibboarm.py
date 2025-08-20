# n=int(input('enter the limit:'))
# a,b=0,1
# print('fibonacci series')
# for _ in range(n):
#  print(a,end='')
#  a,b=b,a+b
# limit=int(input('enter your limit:'))
# count=0
# n1=0
# n2=1  
# while count<=limit:
#  print(n1,end='')
#  x=n1+n2
#  n1=n2
#  n2=x
#  count+=1

# num = int(input("Enter a number: "))

# Step 1: Count the digits
# count = 0
# temp = num
# while temp > 0:
#     count += 1
#     temp //= 10  
    # last digit removal

# Step 2: Calculate the Armstrong sum
# temp = num
# sum_of_powers = 0
# while temp > 0:
#     digit = temp % 10
#     # %- last digit edukkan
#     sum_of_powers += digit ** count
#     temp //= 10

# Step 3: Check if Armstrong
# if sum_of_powers == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")

# num=int(input('enter a no:'))
# sum=0
# x=num
# count=0
# n=num
# while n>0:
#     count+=1
#     n //= 10
# x=num
# while x>0:
#     digit=x % 10
#     sum+=digit**count
#     x //10
# if num==sum:
#     print('no is armstrong')       
# else:
#     print('no is not armstrong')    




num = int(input('Enter a number: '))
sum_digits = 0
count = 0
n = num

# Count digits
while n > 0:
    count += 1
    n //= 10

# Armstrong sum
x = num
while x > 0:
    digit = x % 10
    sum_digits += digit ** count
    x //= 10  # Fixed here

# Check
if num == sum_digits:
    print('Number is Armstrong')
else:
    print('Number is not Armstrong')














