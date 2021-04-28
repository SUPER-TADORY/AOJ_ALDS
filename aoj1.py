#1_1_A
"""
n=int(input())
l=[int(x) for x in input().split()]
#l=input().split()
print(" ".join([str(x) for x in l]))
for i in range(1,n):
    j=i
    v=l[i] #動かす数字
    while j>0 and l[j-1]>v:
        l[j]=l[j-1]
        j-=1
    l[j]=v
#####ここで、lに変更したlを代入してしまうと、次回以降のループでそのlが使われてしまう
    #l=[str(x) for x in l]
    #print(" ".join(l))
    a=[str(x) for x in l]
    print(" ".join(a))


#1_1_B
l=[int(x) for x in input().split()]
while 1:
    l=sorted(l)
    n=l[1]%l[0]
    if n==0:
        break
    l=[n,l[0]]
print(l[0])

#1_1_C

#####↓これだとタイムオーバー!!!
def prime(num):
    which=True
    ###↓2自身も含める
    if num%2==0 and num!=2:
        which=False
    for i in range(1,int(num//4)+2):
        ###↓not num==i*2+1自身も含める
        if num%(i*2+1)==0 and not num==i*2+1:
            which=False
    return which

n=int(input())
out=0
for i in range(n):
    m=int(input())
    if prime(m):
        out+=1 
print(out)

#from numpy import sqrt
def prime(num):
    w=True
    #m=int(sqrt(num)//1)+1
    m=int((num**(1/2))//1)+1
    for i in range(2,m+1):
        #o=bool(num%i)
        if num%i==0 and num>2:
            ####↓ここで、==に気がつかず、１時間悩んでいた!!!!!
            #w==False
            w=False
            #return False
            break
    return w
n=int(input())
out=0
for i in range(n):
    l=int(input())
    if prime(l):
        out+=1 
print(out)



#1_1_D

n=int(input())
#####↓変数名にminは使えない（予約語）
min_=int(input())
out_min=(-1)*(10**9)
for i in range(n-1):
    n=int(input())
    out_min=max(n-min_,out_min)
    min_=min(min_,n)
print(out_min)


#1_2_A

def sort(l):
    l_=l
    sorted_=0
    num=0
    for i in range(1,len(l)):
        count=0
        #print(i+1)
        #print(len(l),len(l)-count)
        while (len(l)-1)-count>sorted_:
            #l_[len(l)-count-1],l_[len(l)-count]=min(l_[len(l)-count-1],l_[len(l)-count]),max(l_[len(l)-count-1],l_[len(l)-count])
            a=l_[(len(l)-1)-count-1]
            b=l_[(len(l)-1)-count]
            if a>b:
                l_[(len(l)-1)-count-1],l_[(len(l)-1)-count]=b,a
                num+=1
            count+=1
        sorted_+=1
    return l_,num

n=input()
l=[int(x) for x in input().split()]
l_,num=sort(l)
print(" ".join([str(x) for x in l_]))
print(num)


#1_2_B

def sort(l):
    l_=l.copy()
    count=0
    for i in range(len(l)):
#########↓これだと、最小値のインデックスを保持しておけない！！！minjを設定し、最小値を持つインデックスを更新していく！！！
        #min_=l_[i]
        #for n in range(i,len(l)):
        #    min_=min(min_,l_[n])
        #    print(min_)
    ######↓ここで、先頭を最小値で更新するだけではダメ！！　あくまでも、値の交換をしないといけない！！！
        #l_[i]=min_
        minn=i
        for n in range(i,len(l)):
            #####↓ばかか！！！　これだと最終的に末尾の数とl_[i]比べているだけ。　比べるのは、そこまでの最小値と更新したインデックス!!!
            #if l_[n]<l_[i]:
            if l_[n]<l_[minn]:
                minn=n
                
        l_[i],l_[minn]=l_[minn],l_[i]
        if not minn==i:
            count+=1
        
    return l_,count

n=input()
l=[int(x) for x in input().split()]
l_,num=sort(l)
print(" ".join([str(x) for x in l_]))
print(num)


#1_2_C

def bubble(l_):
    l=l_
    for i in range(len(l)):
        num=0
        #####↓len(l)は-1しろ！！
        #while len(l)-num>i:
        while len(l)-num-1>i:
            if int(l[len(l)-num-1][-1])<int(l[len(l)-num-2][-1]):
                l[len(l)-num-1],l[len(l)-num-2]=l[len(l)-num-2],l[len(l)-num-1]
            num+=1
    return l

def select(l_):
    l=l_
    for i in range(len(l)):
        #####↓ここでminn=0としていると、選択済みのところの最小値を永遠に最小値として捉えてしまうことになる！！！
        #minn=0
        minn=i
        for n in range(i,len(l)):
            if int(l[minn][-1])>int(l[n][-1]):
                minn=n
        l[i],l[minn]=l[minn],l[i]

    return l

n=input()
l_l=input().split()
l_sub=l_l.copy()

#print("l",l_l)

#########↓この操作で、l_lは変換されてしまうので要注意！！！
l_a=bubble(l_l)
#print(l_a)
#print("l",l_l)

#########↓ここのl_lはl_a=bubble(l_l)によってl_lがすでに変換されてしまっているのでダメ！！！
#l_b=select(l_l)
l_b=select(l_sub)
#print(l_b)


print(" ".join(l_a))
print("Stable")
print(" ".join(l_b))
print("Stable" if l_a==l_b else "Not stable")


#1_2_D

def insert_(l_,g):
    l=l_.copy()
    cnt_=0
    #print(l)
    for i in range(g,len(l)):
        o=l[i]
        j=i-g
        while j>=0 and l[j]>o:
            l[j+g]=l[j]
            ####↓ここでは、l[j+g]=oをまだ行っていないので、lをみても混乱を招くだけ！！！　出力見る位置もちゃんと考えること
            #print(l)
        #####↓ここはステップを引く！！！
            #j-=1
            j=j-g
            cnt_+=1
        l[j+g]=o
        #print(l,o)
    return l,cnt_

def shell(l_):
    l=l_.copy()
    cnt_=0
#####↓ここ固定だと、計算量調節できない！！！
    #m=2 
    #f=[min(len(l),4),1]
    #for i in range(m):
     #   l,cnt=insert_(l,f[i])
    #####↓ここでcntを加算していかないといけない事に注意！！！
       #cnt_+=cnt

    g=1
    n=len(l)
    f=[]
    m=0
    ######↓本来は9が最適であるが、今回は５とした
    while g<n//5:
        g=g*3+1
    while g>0:
        l,cnt=insert_(l,g)
        cnt_+=cnt
        f.append(g)
        m+=1
        g//=3


    return m,f,l,cnt_

n=int(input())
l_=[]
for i in range(n):
    l_.append(int(input()))


m,f,l,cnt=shell(l_)

print(m)
print(" ".join([str(x) for x in f]))
print(cnt)
for k in l:
    print(k)

"""

########################################################################
#1_3_A　逆ポーランド記法
"""

def initialize(top):
    return 0

def isEmpty(top):
    return top==0

def isFull(top):
    ##########↓MAX-1なのは、push()でtopを+1するから
    return top>=MAX-1

def push(x,top,l):
    if isFull(top):
        print("error")
    top+=1
    l[top]=x
    return l,top

def pop(l,top):
    if isEmpty(top):
        print("error")
    top-=1
    return l[top+1],top

st=input().split()
top=0
MAX=len(st)
s="+-*/"
l=[0 for x in range(MAX)]

for n in st:
    if n in s:
        a,top=pop(l,top)
        b,top=pop(l,top)
    #####↓二つ目以降はl,top=いらない
        #l,top=push(a+b,top) if n=="+" else l,top=push(a-b,top) if n=="-" else l,top=push(a*b,top) if n=="*" else l,top=push(a/b,top)
    #####↓先に入っているもの（演算子）　後!!! 
        l,top=push(a+b,top,l) if n=="+" else push(b-a,top,l) if n=="-" else push(b*a,top,l) if n=="*" else push(b/a,top,l) 

    else:
        l,top=push(int(n),top,l)
    #print(l)

print(l[top])
"""

########################################################################
#1_3_B　ラウンドロビンスケジューリング（Queue）

"""
###hはキューの先頭、tはキューの末尾+1(次のデータが入るポインタ)

def initialize(h,t):
    h=0
    t=0
    return h,t

def isEmpty(h,t):
    return h==t

def isFull(h,t,max_):
##########↓ここは、tがhの二個手前まで差し迫ってきたら、満杯とするということ
    return h==(t+1)%max_

def enqueue(q,h,t,x,max_):
    if isFull(h,t,max_):
        print("error")
    #print("q",q,"t",t)
    q[t]=x
    ######↓先頭を一個後ろのやつにするという事
    #####↓max_-1にしないとエラー！！！
    #if t==max_:
    if t==max_-1:
        t=0
    else:
        t+=1
    
    return q,h,t

def dequeue(q,h,t,max_):
    if isEmpty(h,t):
        print("error")
    x=q[h]
    if h+1==max_:
        h=0
    else:
        h+=1
    return x,q,h,t

h=0
t=0
n,m=map(int,input().split())
max_=n+3
#####↓キューが最初空であると、len(q)はnにしかならない事に注意！！！
# q=[]
q=[0 for _ in range(max_)]
for _ in range(n):
    s=input()
    q,h,t=enqueue(q,h,t,s,max_)

time_=0
out={}
check=0

while check<n:
    x_,q,h,t=dequeue(q,h,t,max_)
    #x=int(x_[3:])
    x=int(x_.split()[-1])
    #print(x)
    if x>m:
        time_+=m
        x-=m
    elif x<=m and x>0:
        time_+=x
        ###↓忘れるな
        x=0
        k=str(time_)
        out[x_.split()[0]]=k
        check+=1

    q,h,t=enqueue(q,h,t,x_.split()[0]+" "+str(x),max_)

for i,o in out.items():
    print(i,o)
""" 
########################################################################
#1_3_C　双方向連結リスト
"""
import sys

n=int(sys.stdin.readline())
#print("n",n)
l=[]

def insert_(l_,x):
    l=l_
    l.insert(0,x)
    #####↓insert()はlを変更する関数で、lを返しているわけではないのでダメ！！！
    #return l.insert(0,x)
    return l

def delete_(l_,x):
    l=l_
    #####pop()は引数の数が要素にないとエラー！！！
    try:
        l.pop(l.index(x))
    except:
        pass
    return l

def delete1(l_):
    l=l_
    l.pop(0)
    return l

def deletel(l_):
    l=l_
    l.pop(-1)
    return l        

for i in range(n):
    #t=input()
    t=sys.stdin.readline().rstrip("\n")
    #print(t)
    #if "insert" in t:
    if "n" in t:
        #print(t[-1])
        #m=int(t[-1])
        m=int(t[7:])
        l=insert_(l,m)
    ##### ↓deleteはdeleteFirst,deleteLastにも含まれている事に要注意！！！
    elif "F" in t:
        l=delete1(l)
        #print("F")
    elif "L" in t:
        l=deletel(l)
    elif "delete " in t:
        #m=int(t[-1])
        #print("fsgfdzg",m)
        m=int(t[7:])
        l=delete_(l,m)
    else:
        break

print(" ".join([str(x) for x in l]))
"""
########################################################################
#1_3_D
"""
import sys
l=sys.stdin.readline()

current_h=100
#標高を保存しておく
h_l=[]
for tx in l:
    if tx=="\":
        h_l.append(current_h-)
"""
########################################################################
#1_4_A 線形探索

"""
import sys

a=int(input())
al=sys.stdin.readline().split()
m=len(al)+1
b=int(input())
bl=sys.stdin.readline().split()

out=0
which=True

for i in range(b):
    which=True
    key=bl[i]
    #####↓これだと末尾に追加されない！！
    #al.insert(-1,key)
    al.append(key)
    #print(al)
    n=0
    while al[n]!=key:
        n+=1
    ######↓ループ内にifを入れると番兵法の意味がない！！！
        #if n==m:
         #   which=False
    if n>=m-1:
        which=False
    if which:
        out+=1
print(out)
            
"""
########################################################################
#1_4_B　二分探索法
"""

import sys

a=int(input())
#####↓alにもintの処理必要！！！
#al=sys.stdin.readline().split()
al=[int(x) for x in sys.stdin.readline().split()]
m=len(al)+1
b=int(input())
#####↓blにもintの処理必要！！！
#bl=sys.stdin.readline().split()
bl=[int(x) for x in sys.stdin.readline().split()]

def binary(l,x,max_):
    left=0
    right=max_

    while left<right:
        mid=(left+right)//2
        #print("mid",mid,l[mid])
        if l[mid]==x:
        ######↓mid見つかったら返り値出力して終了
            #print("True",x)
            return True
    ##########↓l[mid]とxがstrだったから、文字数で比べられていた！！！
        elif l[mid]>x:
        ######↓逆！！！
            #left=mid+1
            right=mid
            #print("right",right)
        else:
            ######↓逆！！！
            #right=mid
            left=mid+1
            #print("left",left)
    
    #print(x,l)
    #print("False",x)

    return False

cnt=0
for i in bl:
    #print("i",i)
    if binary(al,i,a):
        cnt+=1

print(cnt)
"""
########################################################################
#1_4_C　辞書
""""

import sys

class dict_():
    def __init__(self):
    #######同じ要素が重複する場合もあるので、リストではなく、集合の方が良い！！！
        #self.l=[]
        self.d=set()

    def insert_(self,tx):
        #self.l.append(tx)
        self.d.add(tx)
    
    def find_(self,tx):
        #if tx in self.l:
        if tx in self.d:
            print("yes")
        else:
            print("no")

n=int(input())
dic=dict_()
for i in range(n):
    inp=sys.stdin.readline().rstrip("\n")
    #m=inp.split()
    if inp[0]=="i":
        dic.insert_(inp[7:])
    else:
        #print("inp[7:]",inp[7:])
        dic.find_(inp[5:])
"""
########################################################################
#1_4_D Allocation

"""
###↓題意を取り間違えていた！！！
import sys
n,k=map(int,sys.stdin.readline().split())
l=[]
track=[0 for _ in range(k)]
for i in range(n):
    l.append(int(sys.stdin.readline().rstrip("\n")))
l=sorted(l,reverse=True)

for s in l:
    i=track.index(min(track))
    track[i]+=s

print(l)
print(track)
print(max(track))

###↓トラックには連続する荷物しか入れることができない！！！

"""
########################################################################
#1_5_A 総当たり、再帰関数

import sys

#def solve(i,m,n,l):
    #print("i,m",i,m)
    #print("i,m",i,m)
 #   if m==0:
        #print("Trueで終了")
#        return True ###←再帰関数を含まないものをreturnするので、関数が終了する
#    elif i>=n:
        #print("Falseで終了")
 #       return False ###←再帰関数を含まないものをreturnするので、関数が終了する
    
 #   res=solve(i+1,m,n,l) or solve(i+1,m-l[i],n,l)
    #print("res",res)

  #  return res

n=int(input())
A=[int(x) for x in sys.stdin.readline().split()]
q=int(input())
ml=[int(x) for x in sys.stdin.readline().split()]

def solve(i,m):
    if m==0:
        return True
    elif i>=n:
        return False
    
    res=solve(i+1,m) or solve(i+1,m-A[i])

    return res

#print("ml",ml)

#####↓このmは0,1,2,3,,,の数字だろアホか！！！！！！　for文で回すのがindexかobjectかちゃんと意識すること！！！
#for m in range(q):
for m in ml:
    #print("yes" if solve(0,m,n,A) else "no")
    print("yes" if solve(0,m) else "no")

    




        

        
    
  



