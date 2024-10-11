
import random



a=[0,1,2]
b=[0,1,2]

random_a=random.sample(a,1)[0]
random_b=random.sample(b,1)[0]





def font(data):
    if data==0:
        str="グー"
    elif data==1:
        str="チョキ"
    elif data==2:
        str="パー"
        
    return str

def judge(adata,bdata):
    if adata==bdata:
        str="引き分け"
    if adata==0:
        if bdata==1:
            str="Aの勝ち"
        elif bdata==2:
            str="Aの負け"
    if adata==1:
        if bdata==2:
            str="Aの勝ち"
        elif bdata==0:
            str="Aの負け"
    if adata==2:
        if bdata==0:
            str="Aの勝ち"
        elif bdata==1:
            str="Aの負け"
            
    return str








print("Aの手: "+font(random_a)+" v.s. "+" Bの手: "+font(random_b)+" -> " +judge(random_a,random_b))
            
        
    

