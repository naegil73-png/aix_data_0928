# 오늘 집에서 책을 읽어 볼 것

# 데이터프레임에서의 인덱스
import pandas as pd

# # 1차원 - Series:()안에 리스트를 넣으면 됨 -> 리스트를 시리즈로 만들어줌
# temp = pd.Series([-20,-10,0,10,20],index=["1월","2월","3월","4월","5월"]) # 인덱스 수가 자료 수와 다르면 에러
# print(temp)
# print(temp["1월"])
# print(temp[["1월","2월"]]) # 인덱스 2개 이상이면, []가 2개 여야 함

# 2차원 = DataFrame : 구조는 딕셔너리타입의 리스트형태

data = {
    '이름':['강나래','강태원','강호림','김수찬','김재욱','박동현','박혜정','승근열'],
    '학교':['신림고','신림고','신림고','신림고','신림고','디지털고','디지털고','디지털고'] ,
    '키':[197,184,168,187,188,202,188,190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']}

# dataFrame데이터 프레임으로 만드는 이유: 파이썬 리스트타입보다 계산이 더 용이
df = pd.DataFrame(data) # 데이터프레임으로 변환
# print(df)

# # # 이름을 index로 하려면.. 
# print(df.set_index("이름"))
# print(df)

# # # index 지정 및 index컬럼 이름 지정
# # df = pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# # df.index.name = "지원번호" # 인덱스의 이름 지정
# # print(df)

# # index 지정해제
# df = pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# df.index.name = "지원번호" 
# print(df.reset_index(drop=True, inplace=True)) 
# print(df)

# sort_index : index정렬, inplace=True: 완전지정되어 저장
# ascending=True:순차정렬, False는 역순정렬
df = pd.DataFrame(data)
df.set_index("이름",inplace=True)
df.sort_index(inplace=True,ascending=False) # 역순 정렬
print(df)

