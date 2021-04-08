import pandas as pd
import matplotlib.pyplot as plt

#doc file csv bang pandas.read_csv
dataFrame = pd.read_csv("Thursday-15-02-2018_TrafficForML_CICFlowMeter.csv")

#su dung dataFrame.head/tail de in bao nhieu hang dau tien hoac cuoi cung
tmp1 = dataFrame.head(5)
tmp2 = dataFrame.tail(5)

#Thao tac voi pandas
#1. Xem chieu dai df
print("Len:", len(dataFrame))
#2. Xem thong tin df
dataFrame.info()
#3. Xem kich thuoc
print("Shape:", dataFrame.shape)

#Truy xuat du lieu 1 cot
print(dataFrame['Protocol'])
#Truy xuat nhieu cot + head
print(dataFrame[['Protocol', 'Timestamp']].head(5))
#Truy xuat hang theo chi so (giong head)
print(dataFrame[0:5])
#Truy xuat long dieu kien
tmp5 = dataFrame[dataFrame['Protocol'] == 0]
print(tmp5)

#Chieu pandas ve numpy
tmp4 = dataFrame.values[:5, :5]
print(tmp4)

#Them vao dataframe
#Để thêm cột vào một dataframe có sẵn.
# Trước tiên, bạn cần có 1 list dữ liệu tương ứng với cột mà bạn muốn thêm.
# Tức là chiều dài của list phải tương ứng với số bản ghi của dataframe bạn muốn thêm.

#Xoa cot
# dataFrame.drop('tên cột cần xóa', axis=1) # Xóa 1 cột
# dataFrame.drop(['cột 1', 'cột 2'], axis=1) # Xóa nhiều cột
# dataFrame.drop(columns=['B', 'C']) # Xóa các cột có tên là B và C


#Thong ke co ban ve du lieu
print("Thong ke dataframe\n", dataFrame.describe())
print("Thong ke cu the cot protoco\n", dataFrame['Protocol'].value_counts())

#sap xep trong dataframe
sort = dataFrame.sort_values('Protocol', ascending=False) #true la tang dan, false la giam dan
print(sort.head(5))

#luu dataframe ve file
#dataFrame.to_csv(<duong dan>)