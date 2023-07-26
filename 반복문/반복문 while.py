# while 문제 1

# num = int(input("정수를 입력하세요:"))
# a = 1
# sum = 0
# while a < num+1:
#     sum += a
#     a += 1
    
# print(sum)


#while  문제 2

# count = 0

# while count < 10:
#     print("Hello, Python")
#     count += 1

#while 문제 3

# sum = 0
# num = 1

# while num != 0:
#     num = int(input("정수를 입력하시오:"))
#     sum += num
# print(sum)


sumlist = []
result = 0

while True:
    num = int(input("정수를 입력하세요:"))
    if num == 0:
        break
    sumlist.append(num)
for i in sumlist:
    result += i
print(result)
