####################################################################
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
"""
####################################################################
#1_1_B
"""
l=[int(x) for x in input().split()]
while 1:
    l=sorted(l)
    n=l[1]%l[0]
    if n==0:
        break
    l=[n,l[0]]
print(l[0])
"""
####################################################################
#1_1_C
"""
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
"""
####################################################################
#1_1_D
"""
n=int(input())
#####↓変数名にminは使えない（予約語）
min_=int(input())
out_min=(-1)*(10**9)
for i in range(n-1):
    n=int(input())
    out_min=max(n-min_,out_min)
    min_=min(min_,n)
print(out_min)
"""
####################################################################
#1_2_A
"""
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
"""
####################################################################
#1_2_B
"""
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
"""
####################################################################
#1_2_C
"""
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
"""
####################################################################
#1_2_D
"""
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
#1_3_B　ラウンドロビンスケジューリング（Queue） (時間未解決)

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
#1_3_C　双方向連結リスト　（時間未解決）
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
#1_5_A 総当たり、再帰関数　（時間未解決）

"""
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
"""
########################################################################
#1_5_B 　マージソート(分割統治法)
"""
import sys

n=int(input())
#####↓.split()しないとlistになってくれない！！！
#l=[int(x) for x in sys.stdin.readline()]
l=[int(x) for x in sys.stdin.readline().split()]
#A=[int(x) for x in sys.stdin.readline().split()]
cnt=0

###統治
def merge_(A,left,mid,right):
    
    ##print("fdkafjireofjejl")
    #n1=mid-left
    #n2=right-mid
    ##print("n1",n1,"n2",n2)    #↓二つに分けた配列を比較して合併するとき、Aを参照しながらAを変更するのは困難であるので、必ず新しい配列を作る！！！
    #L=[x for x in range(n1+1)]
    #R=[x for x in range(n2+1)]

    #for i_ in range(n1):
    #   #####↓+1じゃなくて+i!!!!
    #   #L[i_]=A[left+1]
    #    L[i_]=A[left+i_]
    #for i_ in range(n2):
    #    #####↓+1じゃなくて+i!!!!
    #    #R[i_]=A[mid+1]
    #    R[i_]=A[mid+i_]
    


########↓こっちの方が処理速度遅い！！！
#######↓処理速度遅かったのはA.copy()のせい！！！ループ内で大きいリストをいちいちコピーしていたら遅くなるので要注意！！！
    #A_=A.copy()
    L=A[left:mid]
    L.append(float("inf"))
    R=A[mid:right]
    R.append(float("inf"))
#########

    #↓番兵を無限に設定しておく
    #↓二つの分割配列を比べていく中で、どちらか一方の要素がなくなったとき、別の処理を与えるのは簡潔でないので、番兵を用意しておく！！！
    #L[n1]=float("inf")
    #R[n2]=float("inf")
    #print("L",L,"R",R)

#↓これ以降では、二つに分けた部分列を一つの整列された配列に合併！
#これ以前では、二つの部分列を生成しているだけであるが、部分列の要素が二つのときから連鎖していくので、自動的に整列した配列になる。

    i=0
    j=0

    #for k in range(left,right):
    for k in range(right-left):
        global cnt
        #↓L[i]==R[j]であった場合は、左を優先→→→安定なソートになる！！！
        if L[i]<=R[j]:
            A[left+k]=L[i]
            i+=1
            #cnt+=1
        else:
            A[left+k]=R[j]
            j+=1
            #cnt+=1
        cnt+=1

    
    ###↓mergeSort()ないでは最終出力をうまく取り出せないのでここで！！！
    if right-left==n:
        #print(A)
        print(" ".join([str(x) for x in A]))
    
    

###分割
def mergeSort(A_,left,right):
    #####↓これがなくても、引数としてのAは更新されてしまう
    A=A_
    if left+1<right:
        mid=(left+right)//2
        mid=mid
        #↓再帰関数！！！　左と右に分割
        mergeSort(A,left,mid)
        mergeSort(A,mid,right)
        #↓分割した二つを統治する!!!
        merge_(A,left,mid,right)
    

mergeSort(l,0,n)
#print(*A)
print(cnt)
"""
########################################################################
#1_5_C コッホ曲線
"""
import sys
from math import sin, cos, sqrt, radians

def kock(n,p1_x,p1_y,p2_x,p2_y):
    if n==0:
        return #####関数終了！！！

    s_x=(2*p1_x+p2_x)/3
    s_y=(2*p1_y+p2_y)/3
    t_x=(2*p2_x+p1_x)/3
    t_y=(2*p2_y+p1_y)/3
    u_x=(t_x-s_x)*cos(radians(60))-(t_y-s_y)*sin(radians(60))+s_x
    #######↓+と-間違えていた！！！
    #u_y=(t_x-s_x)*sin(radians(60))-(t_y-s_y)*cos(radians(60))+s_y
    u_y=(t_x-s_x)*sin(radians(60))+(t_y-s_y)*cos(radians(60))+s_y

#######↓新しくできた４辺に対して再帰を適用する！(深さを一つ引いて継承していく！！！)
    kock(n-1,p1_x,p1_y,s_x,s_y)
    print(format(s_x,".8f"),format(s_y,".8f"))
    kock(n-1,s_x,s_y,u_x,u_y)
    print(format(u_x,".8f"),format(u_y,".8f"))
    kock(n-1,u_x,u_y,t_x,t_y)
    print(format(t_x,".8f"),format(t_y,".8f"))
    kock(n-1,t_x,t_y,p2_x,p2_y)

n=int(input())
print(0,0)
#print(format(0,".8f"),format(0,".8f"))
kock(n,0,0,100,0)
print(100,0)
#print(format(100,".8f"),format(100,".8f"))
"""
########################################################################
#1_5_D 反転数
"""
import sys

n_=int(input())
l_=list(map(int,sys.stdin.readline().split()))

def bubble(n,l):
    cnt=0
    for i in range(1,n):
        j=i-1
    ##########↓ここで、jが０以上であることを条件に入れないといけない!!!
        #while l[j+1]<l[j] :
        while l[j+1]<l[j] and j>=0:
            l[j+1],l[j]=l[j],l[j+1]
            cnt+=1
            j-=1
    
    return cnt

##########分割統治法の利用で計算量大幅削減！！！
###統治

cnt=0

def merge_(A,left,mid,right):
    global cnt

    which=False
    L=A[left:mid]
    L.append(float("inf"))
    R=A[mid:right]
    R.append(float("inf"))

    i=0
    j=0
   
    for k in range(right-left):
        if L[i]<=R[j]:
            A[left+k]=L[i]
            i+=1
            #if i==len(L)-1:
            #    which=True
        else:
            A[left+k]=R[j]
            j+=1
            #if which:
        ###########↓ここで、cntとして追加するのは１ではない！！！ +1では、Rの要素一つについて何個Lにそれより大きい要素があるのかを記録できない！！
        #############だから、Rが追加される時点でLに残っている要素数を加算していく必要がある！！！
            #    cnt+=1
            cnt+=(mid-left)-i

    

###分割
def mergeSort(A_,left,right):
    A=A_
    if left+1<right:
        mid=(left+right)//2
        mid=mid
        mergeSort(A,left,mid)
        mergeSort(A,mid,right)
        merge_(A,left,mid,right)

mergeSort(l_,0,n_)
#print(cnt)
print(cnt)
"""
########################################################################
#1_6_A　計数ソート
"""
import sys

n=int(input())
A=list(map(int,sys.stdin.readline().split()))

def countingSort():
    global n,A

    k=max(A)
    B=[0 for _ in range(n)]
    #↓ここで、Cに各要素の出現回数を記録する！！！
    C=[0 for _ in range(k+1)]
    for j in range(n):
        C[A[j]]+=1
    #print("C",C)
######↓ここで、rangeに0含めると、だめ！！！
    #for i in range(k+1):
    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]
    #print("C",C)
    #####↓後ろから入力していくことで安定なソートに！！！
    for m in reversed(range(0,n)):
        #print("M",m)
    #####↓Cには、何番目かが記録されているので、Cの数字をそのまま入力インデックスにすれば良い！！！
        #print(B,C[A[m]])
        B[C[A[m]]-1]=A[m]
        C[A[m]]-=1

    return B
B=countingSort()
print(*B)
"""
########################################################################
#1_6_B　Partition
"""
import sys

n=int(input())
A=list(map(int,sys.stdin.readline().split()))


def partition(p,r):
    global A,n

    x=A[r]
######↓最初i=-1となるが、それが正しい！！！ iは基準を挿入するインデックス!!!
    i=p-1
    #print(i)
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            ###↓i+=1で基準を一個ずらしてから交換!!(A[j]を基準の左に、A[i]を右に!!!)
            A[i],A[j]=A[j],A[i]
    #↓最後に末尾の基準となる数字を基準点に！！！
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

k=partition(0,n-1)
for i,o in enumerate(A):
    if i==k:
        print(f"[{o}]",end=" ")
    else:
        if i!=n-1:
            print(o,end=" ")
        else:
        ########↓最後は改行しないとpresentation errorが起こる!!!!!
            print(o)
"""
########################################################################
#1_6_C クイックソート
"""
import sys

n=int(input())
A=[]
for _ in range(n):
    A.append(sys.stdin.readline().rstrip("\n"))

A_=A.copy()

def partition(p,r):
    global A,n

    x=int(A[r].split()[1])
    i=p-1
    for j in range(p,r):
        if int(A[j].split()[1])<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quickSort(p,r):
    global A,n

    if p<r:
        #print(A)
        q=partition(p,r)
        quickSort(p,q-1)
        quickSort(q+1,r)

###↓安定なソート(Memory limit exceededなので使えない！！！)
def countingSort():
    global n,A_

    A__=[int(x.split()[1]) for x in A_]
    k=max(A__)
    #print(A_)
    #print(A__)
    B=[0 for _ in range(n)]
    C=[0 for _ in range(k+1)]
    for j in range(n):
        C[int(A_[j].split()[1])]+=1
    
    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]
    
    #print("C",C)
    
    for m in reversed(range(0,n)):
        B[C[int(A_[m].split()[1])]-1]=A_[m]
        C[int(A_[m].split()[1])]-=1

    return B

###↓安定なソート　マージソートは安定なので、比較対象として利用できる！！！
def merge_(left,mid,right):
    L=A_[left:mid]
    L.append(f"s {10000000000}")
    R=A_[mid:right]
    R.append(f"s {10000000000}")

    i=0
    j=0
   
    for k in range(right-left):
        if float(L[i].split()[-1])<=float(R[j].split()[-1]):
            A_[left+k]=L[i]
            i+=1
        
        else:
            A_[left+k]=R[j]
            j+=1
def mergeSort(left,right):
    if left+1<right:
        mid=(left+right)//2
        mid=mid
        mergeSort(left,mid)
        mergeSort(mid,right)
        merge_(left,mid,right)

#partition(0,n)
quickSort(0,n-1)
mergeSort(0,n)
#print(A)
#print(A_)
if A==A_:
    print("Stable")
else:
    print("Not stable")

for o in A:
    print(o)
"""
########################################################################
#1_6_D　根付き木

########↓死ね無能
"""
from sys import stdin

n=int(input())

class Node():
    def __init__(self):
    ########↓インスタンスの持つ変数は、引数に取らなくても変更できる！！！
        self.parent=-1
        self.mostleft=None
        self.right=None
        self.root=[]

tree_dict={}
cnt=0

######↓親の方からたどる！
def get_depth_for_a_tree(nod,depth=0):
    global tree_dict,cnt

    cnt+=1
    print("###################",cnt)
    ml=tree_dict[nod].mostleft
    r=tree_dict[nod].right

    print("depth___",depth)

    if ml<0 or r<0:
        print("depth",depth)
        return 

    print("ml",ml,"r",r)

    if ml>=0:
        get_depth_for_a_tree(ml,depth=depth+1)
        print("ml")
    if r>=0:
        get_depth_for_a_tree(r,depth=depth)
        print("r")

def get_depth_for_all():
    global tree_dict

    #selected_key_dict={key:obj for key,obj in zip(tree_dict) if key>=0}
    selected_key_list=[key for key in tree_dict.keys() if key>=0]
    print("selected_key_list",selected_key_list)

    for key in selected_key_list:
        get_depth_for_a_tree(key)

D={}
def get_depth(u,p):
    global tree_dict,D

    D[u]=p
    if tree_dict[u].right is not None:
        get_depth(tree_dict[u].right,p)
    if tree_dict[u].mostleft is not None:
        get_depth(tree_dict[u].mostleft,p+1)
    

D_={}

print()

for i in range(n):
    #l=list(map(int,stdin.readline().split()))
    #a=l[0]
    #b=l[1]
    #l_children=l[2:]
######↓省略した書き方ができる！！！
    a,b,*root=list(map(int,stdin.readline().split()))

    #print(root)

    if a in tree_dict.keys():
        #print("また",a)
        if b==0:
            #type_="leaf"
            #D_[a]="leaf"
            #print("ない",a)
            pass

        else:
            tree_dict[a].mostleft=root[0]
            tree_dict[a].root=root
            #type_="internal node"
            #D_[a]="internal node"

            for m,j in enumerate(root):
####################↓ここで新たに生成しているが、すでに子についてのノードができている可能性を考慮していない！！！　要注意！！！
                #tree_dict[j]=Node() 
                #print(j,tree_dict.keys())
                if j in tree_dict.keys():
                    #print(j,"すでにある")
                    pass
                else:
                    tree_dict[j]=Node() 
                tree_dict[j].parent=a
                try:
                ###########↓root[j+1]だと正しいインデックス示ていない！！！
                    #tree_dict[j].right=root[j+1]
                    tree_dict[j].right=root[m+1]
                    #print(m,root)
                except:
                    pass
    
    else:  
        #print("新たに",a)
        tree_dict[a]=Node()
        if b!=0:
            tree_dict[a].mostleft=root[0]
            tree_dict[a].root=root
        #type_="root"
        #D_[a]="root"

    ######子供たちもtree_dictに追加しておく！！！
        #print(i,"dfzjkhglfdi")
        for m,j in enumerate(root):
            #tree_dict[j]=Node() 
    ####################↓ここで新たに生成しているが、すでに子についてのノードができている可能性を考慮していない！！！　要注意！！！
            if j in tree_dict.keys():
                #print(j,"すでにある")
                pass
            else:
                tree_dict[j]=Node() 

            tree_dict[j].parent=a
            try:
            ########↓root[j+1]だと正しいインデックス示ていない！！！
                #tree_dict[j].right=root[j+1]
                tree_dict[j].right=root[m+1]
            except:
                pass

########↓ここでprintするのであれば良いが、外でやるならtypeは逐一保存しておかないと全て同じになってしまう！！！
    #print(f"node {a}: parent {tree_dict[a].parent}, depth = {0}, {type_}, {root}")

for node in range(n):
    if tree_dict[node].parent==-1:
        get_depth(node,0)
        break

for a in range(n):
    #print(f"node {a}: parent = {tree_dict[a].parent}, depth = {D[a]}, {type_}, {root}")
    #print(f"node {a}: parent = {tree_dict[a].parent}, depth = {D[a]}, {D_[a]}, {root}")

    type_="root" if tree_dict[a].parent==-1 else "internal node" if tree_dict[a].mostleft is not None else "leaf"
    #print(f"node {a}: parent = {tree_dict[a].parent}, depth = {D[a]}, {type_}, {root}")
    print(f"node {a}: parent = {tree_dict[a].parent}, depth = {D[a]}, {type_}, {tree_dict[a].root}")
    

#print(D)
#for i,node in tree_dict.items():
#   print(i,node.parent,node.mostleft,node.right)
"""
########↓お手本
"""
from sys import stdin


class Node():
    def __init__(self,pa=-1,chs=None):
        self.pa=pa
        self.chs=chs

n=int(input())
tree={id:Node() for id in range(n)}
for _ in range(n):
    id,_,*chs=map(int,stdin.readline().split())
    tree[id].chs=chs
    ####↓子をdictに入れるときにpaを設定してしまう！！！
    for ch in chs:
        tree[ch].pa=id

def set_depths(id,depth):
    tree[id].depth=depth
    for ch in tree[id].chs:
        set_depths(ch,depth+1)

for id in tree:
    if tree[id].pa==-1:
        set_depths(id,0)
        break

for id,node in tree.items():
    kind= "root" if node.pa == -1 else "internal node" if node.chs else "leaf"
    print(f"node {id}: parent = {node.pa}, depth = {node.depth}, {kind}, {node.chs}")
"""
########################################################################
#1_6_D　二分木

import sys

class Node():
    def __init__(self,chs=[],pa=-1):
        self.pa=pa
        self.chs=chs

n=int(input())

######↓初期状態で何も入っていないと、for ch in chs：のところでエラーが起こる！！！
#tree={}
tree={id:Node() for id in range(n)}

for i in range(n):
    a,*chs=list(map(int,sys.stdin.readline().split()))
    tree[a].chs=chs

    for ch in chs:
        #print(ch)
        if ch>0:
            tree[ch].pa=a

for k,v in tree.items():
    print("id",k,"chs",v.chs,"pa",v.pa)



