items = ['1', '2', '3', '4', '5'] 

# 순열: 순서가 존재
from itertools import permutations 
list(permutations(items, 2)) 
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '1'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '5'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4')]

# 조합: 순서 없음
from itertools import combinations 
list(combinations(items, 2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

#범위 넣기
it = list(combinations(range(1, 8), 6)) # 1부터 7까지 중 6개 조합 추출
print(it)

#바로 반복문 사용
for item in permutations(items,3):
    print(item)
