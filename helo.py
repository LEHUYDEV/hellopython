# #nn= 'r'
# #print('hellopython')
# #print(5+1)
# #n = 't'
# #a,b= 1
# #print(a)
# #print(b)
# a = int(input("chieudai:"))
# b= int(input("chieurong"))
# c= a*b
# d= (a+b)*2
# #print('chuvila',end='*')
# print('dientich:', c,'dientich:',d,end='*')
# #print('chuvi',end=)
# from turtle import *
# shape('turtle')
# #forward(100)
# for v in range(100):
#     forward(50)
#     left(50)
# forward(100)
# mainloop()
#####################################################
# a = int(input("NHẬP BÁN KHÍNH HÌNH TRÒN :"))
# b= 3.14
# c= 2*a*b
# d= b*a**2
# print('Hình tronfcos bán khính là 3 xẽ có dien tich là',d)
# print('Hình tròn có bán kính là 3 xẽ có chi vi là ',c,)
# #########################################

# # ve hinh tam giac 
# from turtle import *
# shape('turtle')
# for v in range(1):
#     forward(200)
#     left(120)
#     forward(200)
#     left(120)
#     forward(200)
#     circle(60)
# mainloop()
#################
 # hinh tron 
# from turtle import *
# shape('turtle')
# for v in range(10):
#     a= 180 -50
#     circle(60)
#     left(a)
# mainloop()
# ############# lech if 
# age = 8
# if age < 10:
#     print("baby")
# ###################lenh if

# a = int (input("nhap so:"))
# print("tri tuyet doi a:",abs(a))
# if a>0:
#     print(a)
# if a<0:
#     print(-a)    
# if a == 0:
#     print(0)    
#####################
# age = 5
# is_baby = age<10
# print(is_baby)
##################
# num = 101
# is_odd = num % 2 ==1
########### tinh do dai bien chuoi
# text = "xinchao"
# text_is_not_empty = len(text)>0
# print(text_is_not_empty)
###################  lenh for // for <bien> in <day lien tiep >
##################                   <body>
################## renge ()
# for v in [1,3,5,7,9]:
#     print("hi",v)
# for x in range(36):
#     for y in range(36):
#         if x + y ==36 and 2*x + 4*y == 100:
#             print("x",  ,"y",)
################### 
# chieu_cao = int(input("nhập chiều cao của bạn (cm) :"))
# can_nang  = int(input("nhập cân nặng của bạn(kg):"))
# don_vi    = 100
# cm_cv_m   = chieu_cao/don_vi
# BMI       = can_nang / (cm_cv_m*2)
# print(cm_cv_m)
# print(BMI)
# if BMI < 16:
#     print("Thiếu cân nặng ")
# elif 18.5 > BMI >=16:
#      print("Thiếu cân")    
# elif 25 > BMI >=18.5:
#     print("Bình thường ")
# elif 25 >= BMI < 30:
#     print("Thừa cân")
# else:
#     print("Béo phì")
##############################

# for v in ["Hello","my name is"," B-max"]:
#     print(v, end=" ")
# print("Hello", end=" ") 
# print(",my name", end=" ")
# print("is B-max", end=" ")
############################################
# a = int(input("nhập một số :"))
# for v in range(1,a,1):
#     if v < a/2:
#         print("X" ,"*",end ="  ")
# print("X",)
############################
# m = int (input("nhập m: "))
# n = int (input("nhập n: "))
# for b in range(0,m,1):
#     for v in range(0,n,1):
#         print("*",end=" ")
#     print()
    ####################
# number  = int (input("nhập số : "))
# if number >= 0:
#     if number == 0:
#        print("số không ")
#     else:
#         print("số dương")
######################################
# for v in range(n)
#     print("x"if v % 2==0 else "*",end =" ")
############################ while
# a = 0
# while a<10:
#     a= a +1 
#     print("hi")
######### thoat while  break
####################################### nhập pasword 
# a = input("nhập pasword:")
# while len(a) <8:
#     print("bạn nhập lại pasword")
#     a = input("nhập pasword:")
# if len(a) > 8:
#     print("pasword oki")
    
# ################################## list
# colors = ["red", "blue", "green"]
# print([colors[1]])
# tong = tong + v
# ############################# bài nhập password 
# password = input(  'bạn nhập password :')
# a =0 
# while not password.isdigit():
#     a = 1
#     break
# print(a)    
# while len(password) < 8:
#     print("passwor nhập sai xin nhập lại")
#     password = input("nhập password")
# while a == 0 :
#     print("passwor nhập sai xin nhập lại ")
#     password = input("nhập password")
# print("password oki")

# ############################### bài lãi xuát ngân hang 
# tien = int(input("bạn nhập số tiền: "))
# tien_lai1 =( (tien * 6.5) /100) 
# tien_lai2 = tien_lai1 * 9
# a= 0
# print(" số tiền bạn gửi trong 9 năm là: ",tien_lai2)
# while tien_lai1 < 1200000000:
#     a = a + 1
#     tien_lai = tien_lai1 * a
  
#     if tien_lai >  1200000000:
#         print("số năm bạn cần gửi là :", a)
#         break
#   ##################################
# bài tập quản lý kho t

# shop = [ "áo phông","áo len ",]
# print("chào mừng bạn đến với cửa hàng của chúng tôi bạn muốn gì",shop)
# print("các mặt hàng của cúng tôi :", shop[0],shop[1])
# a = input("nhập mục mới : ")
# shop.append(a) # thêm mục mới vào list
# print("chào mừng bạn đến với cửa hàng của chúng tôi bạn muốn gì",shop)
# shop[1]= 'váy'# cập nhập mới vào vị trí sô 1 
# print("chào mừng bạn đến với cửa hàng của chúng tôi bạn muốn gì",shop)
# del shop[2]# xóa vị trí  số 2 
# print("chào mừng bạn đến với cửa hàng của chúng tôi bạn muốn gì",shop)
######################### đo khích thước trong list 
# shop = ["1234","123hh","aaaaa"]
# print([len(shop[0]),len(shop[1]),len(shop[2])])
import random
word = 'hello'
ls =[]
for v in word:
    ls.append(v)
print(ls)
random.shuffle(ls)# random các chử trong 
print(ls)
a = input("nhập : ")
if word == a:
    print("oki")

