# i = 0
# while i <= 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# else:
#     print('done')
    # break


# i = 0
# while i <= 5:
#     if i == 3:
#         print(i)
#         i += 1
#         continue
#     print(i)
#     i += 1
# else:
#     print('finished')

#    continuee
# i=0
# while i<5:
#     i+=1
#     if i==3:
#         continue
#     print(i)

# num=int(input('enter an number:'))
# if num<=0:
#     print('it is not a primmee!!!')
# else:
#     for i in range(2,num):
#      if num%i==0:
#         print('not a prime')
#         break
  
#     else:
#      print('prime aaane')    
num=int(input('enter an number:'))
i=2
while num>2:
    if num%i==0:
        print('not prime')
        i+=1
        break
    else:
        print('primeee')
else:
      print('not prime')        
