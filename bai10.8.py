from datetime import datetime
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
Y = int(input("Nhập năm: "))
print("Ngày tháng năm vừa nhập:",d,m,Y)
if ((Y%4==0) and (Y%100!=0) or (Y%400==0)):
    print("năm", Y, "là năm nhuận")
else:
    print("năm", Y, "không phải là năm nhuận")