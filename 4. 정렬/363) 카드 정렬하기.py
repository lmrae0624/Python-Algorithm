import heapq
n=int(input())

heap=[]
for _ in range(n):
    heapq.heappush(heap,int(input()))

result=0
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    
    sum=a+b
    heapq.heappush(heap,sum)
    result+=sum

print(result)

# 3
# 10
# 20
# 40
# sum을 최소로해서 더해 나가는 게 최소 비교 횟수