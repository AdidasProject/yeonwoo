# import pymysql
# import matplotlib.pyplot as plt
# import numpy as np

# db = pymysql.connect(host='localhost', 
#                      port=3306, 
#                      user='root', 
#                      passwd='3306', 
#                      db='progammers_da', 
#                      charset='utf8')

# cursor = db.cursor()


# # 필요 리스트 및 딕셔너리 생성
# city_product_OperatingMargin_SalesMethod = []
# cities = dict()
# products = dict()
# SalesMethods = dict()


# # 영업이익률이 70% 이상인 지역, 제품, 판매방법을 추출
# sql = "SELECT city, product, OperatingMargin, SalesMethod FROM adidas WHERE OperatingMargin >= 70 ORDER BY 1, 2;"
# cursor.execute(sql)


# # 영업이익률이 70% 이상인 지역, 제품, 판매방법 2차원 리스트 생성
# for line in cursor:
#     city_product_OperatingMargin_SalesMethod.append(list(line))


# # decimal을 int형으로 변환
# for line in range(len(city_product_OperatingMargin_SalesMethod)):
#     city_product_OperatingMargin_SalesMethod[line][2] = float(str(city_product_OperatingMargin_SalesMethod[line][2]))


# # 지역 딕셔너리 (지역 항목 개수)
# for city in city_product_OperatingMargin_SalesMethod:
#     if city[0] in cities:
#         cities[city[0]] += 1
#     else:
#         cities[city[0]] = 1


# # 제품 딕셔너리 (제품 항목 개수)
# for product in city_product_OperatingMargin_SalesMethod:
#     if product[1] in products:
#         products[product[1]] += 1
#     else:
#         products[product[1]] = 1


# # 판매방법 딕셔너리 (판매방법 항목 개수)
# for SalesMethod in city_product_OperatingMargin_SalesMethod:
#     if SalesMethod[3] in SalesMethods:
#         SalesMethods[SalesMethod[3]] += 1
#     else:
#         SalesMethods[SalesMethod[3]] = 1


# # 지역, 제품, 판매방법 딕셔너리의 키와 값 추출
# cities_key = list(cities.keys())
# cities_values = list(cities.values())

# products_key = list(products.keys())
# products_values = list(products.values())

# SalesMethods_key = list(SalesMethods.keys())
# SalesMethods_values = list(SalesMethods.values())


# # 각 항목별로 막대 그래프를 나란히 그리기
# width = 0.25
# bar_positions = np.arange(len(cities_key) + len(products_key) + len(SalesMethods_key))

# plt.bar(bar_positions[:len(cities_key)], cities_values, width, color='r', label='City')
# plt.bar(bar_positions[len(cities_key):len(cities_key)+len(products_key)], products_values, width, color='g', label='Product')
# plt.bar(bar_positions[len(cities_key)+len(products_key):], SalesMethods_values, width, color='b', label='SalesMethod')

# # 축 및 레이블 설정
# plt.xlabel('Category')
# plt.ylabel('Count')
# plt.title('Daily Operating Margin Analysis')

# # x축 레이블 설정
# all_labels = cities_key + products_key + SalesMethods_key
# plt.xticks(bar_positions, all_labels, rotation=15)

# # 범례 표시
# plt.legend()

# # 그래프 표시
# plt.show()



































import pymysql
import matplotlib.pyplot as plt
import numpy as np

# MySQL 데이터베이스 연결 설정
db = pymysql.connect(host='localhost', 
                     port=3306, 
                     user='root', 
                     passwd='3306', 
                     db='progammers_da', 
                     charset='utf8')

cursor = db.cursor()

# 필요한 리스트 및 딕셔너리 생성
city_product_OperatingMargin_SalesMethod = []

# 영업이익률이 70% 이상인 지역, 제품, 판매방법을 추출하는 SQL 쿼리
sql = "SELECT city, product, AVG(OperatingMargin) as avg_margin, SalesMethod FROM adidas WHERE OperatingMargin >= 70 GROUP BY city, product, SalesMethod ORDER BY 1, 2;"
cursor.execute(sql)

# 영업이익률이 70% 이상인 지역, 제품, 판매방법 정보를 리스트에 저장
for line in cursor:
    city_product_OperatingMargin_SalesMethod.append(list(line))

# decimal을 float형으로 변환
for line in range(len(city_product_OperatingMargin_SalesMethod)):
    city_product_OperatingMargin_SalesMethod[line][2] = float(str(city_product_OperatingMargin_SalesMethod[line][2]))

# 지역별 평균 영업이익률을 계산하여 딕셔너리에 저장
cities = dict()
for city in city_product_OperatingMargin_SalesMethod:
    if city[0] in cities:
        cities[city[0]] += city[2]
    else:
        cities[city[0]] = city[2]

# 제품별 평균 영업이익률을 계산하여 딕셔너리에 저장
products = dict()
for product in city_product_OperatingMargin_SalesMethod:
    if product[1] in products:
        products[product[1]] += product[2]
    else:
        products[product[1]] = product[2]

# 판매방법별 평균 영업이익률을 계산하여 딕셔너리에 저장
SalesMethods = dict()
for SalesMethod in city_product_OperatingMargin_SalesMethod:
    if SalesMethod[3] in SalesMethods:
        SalesMethods[SalesMethod[3]] += SalesMethod[2]
    else:
        SalesMethods[SalesMethod[3]] = SalesMethod[2]

# 지역, 제품, 판매방법 딕셔너리의 키와 값 추출
cities_key = list(cities.keys())
cities_values = list(cities.values())

products_key = list(products.keys())
products_values = list(products.values())

SalesMethods_key = list(SalesMethods.keys())
SalesMethods_values = list(SalesMethods.values())

# 각 항목별로 막대 그래프를 나란히 그리기
width = 0.25
bar_positions = np.arange(len(cities_key) + len(products_key) + len(SalesMethods_key))

plt.bar(bar_positions[:len(cities_key)], cities_values, width, color='r', label='City')
plt.bar(bar_positions[len(cities_key):len(cities_key)+len(products_key)], products_values, width, color='g', label='Product')
plt.bar(bar_positions[len(cities_key)+len(products_key):], SalesMethods_values, width, color='b', label='SalesMethod')

# 축 및 레이블 설정
plt.xlabel('Category')
plt.ylabel('Average Operating Margin')
plt.title('Average Operating Margin Analysis for Regions with Margin >= 70%')

# x축 레이블 설정
all_labels = cities_key + products_key + SalesMethods_key
plt.xticks(bar_positions, all_labels, rotation=15)

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()












