# 500원 100원 50원 10원 
# 손님에게 거슬러 줘야 할 돈이 N원
# 거슬러줘야할 동전의 최소 개수
# 단, 거슬러 줘야 할 돈은 항상 10의 배수 
# 가장 큰 수 부터 나누고 나머지를 나누면 되지 않나. 

N = 1260

# cnt = N // 500
# a = N % 500

# cnt += a // 100
# b = a % 100

# cnt += b // 50
# c = b % 50

# cnt += c // 10
# d = c % 10 

# print(cnt)

count = 0
coinTypes = [500, 100, 50, 10]

for coin in coinTypes:
    count += N // coin
    N %= coin

print(count)