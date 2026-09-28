import pandas as pd

# pandas에는 
# 1차원 : Series, 2차원 : DataFrame
# [] 리스트 구조 -> 데이터분석에 용이하게 만든 라이브러리
# 리스트 구조를 Series, DataFrame으로 변환

temp = pd.Series([-20, -10, 10, 20])
print(temp)
print(temp[0])
print(type(temp))
print(type(1))
print(type([]))

# index추가
temp = pd.Seires([-20,-10,10,20],index=['Jan','Feb','Mar','Apr'])
print(temp)
print(temp[0]) # index주어졌을 때는 0주소로 찾을 수 있음
print(temp['Jan'])