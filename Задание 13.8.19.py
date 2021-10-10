bileti=int(input("nazovite kolichestvo biletov:"))
vozrast= (int(i) for i in input("vvedite vozrast kazhdogo uchastnika cherez probel").split())
stoimost1=0
stoimost2=990
stoimost3=1390
obshaya_stoimost=0
for i in vozrast:
    if i<18:
        obshaya_stoimost=obshaya_stoimost+stoimost1
    elif 18<=i<=25:
        obshaya_stoimost=obshaya_stoimost+stoimost2
    elif i>25:
        obshaya_stoimost=obshaya_stoimost+stoimost3
if bileti<=3:
    print("Obshaya stoimost biletov:",obshaya_stoimost)
else:
    obshaya_stoimost_so_skidkoy=obshaya_stoimost*0.9
    print("Obshaya stoimost biletov so skidkoy:",obshaya_stoimost_so_skidkoy)