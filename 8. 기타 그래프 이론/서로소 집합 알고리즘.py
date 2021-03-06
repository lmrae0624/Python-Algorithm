# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료 구조

def find_parent(parent,x): #루트 노드 찾기
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e=map(int,input().split()) #노드, 간선(union 연산)
parent=[0]*(v+1)

for i in range(1,v+1): # 부모 테이블에서 부모를 자기 자신으로 설정 
    parent[i]=i

for i in range(e): # union 연산 수행 
    a,b=map(int,input().split())
    union_parent(parent,a,b)


print('각 원소가 속한 집합:')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()


print('부모 테이블:')
print(parent[1:])

# 6 4
# 1 4
# 2 3
# 2 4
# 5 6