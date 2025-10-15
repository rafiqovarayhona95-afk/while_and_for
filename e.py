# davlatlar=[
#     "Uzbekiston","Koreya","Rossiya","AQSH","Xitoy","Yaponiya","Turkiya"]
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# davlatlar.sort(reverse=True)
# print(davlatlar)
# davlatlar.sort(reverse=False)   
# print(davlatlar)
# juft_sonlar=list(range(120,1200,2))
# print(juft_sonlar)
# print(sum(juft_sonlar))

# ismlar=['Rayxona','Munosha','Iroda']
# print(ismlar[0])


# for i in range(2,102,2):
#  print(i)

#  for i in range(1,101,2):
#   print(i)
# for i in range(1,101):
#    if i%2==0:
#        print("juft sonlar",i)

# for i in range(1,101):
#    if i%2==0:
#        print("toq sonlar",i)


# ismalar= ["rayhona","munosha","iroda","dilnoza","muhabbat"]
# for i in ismalar:
#  print("hello",i)
# print(len(ismalar), 'marta takrorlandi')

# for i in range(10,100):
#  print(i**3)
 
 

ps='09876'
a = True
while a:
    password = input("parolni kiriting:")
    if password==ps:
        print("xush kelibsiz")
        a = False
    else:
        print("parol xato qaytadan urinib ko'ring")