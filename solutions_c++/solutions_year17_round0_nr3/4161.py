#include<bits/stdc++.h>
using namespace std;

struct lr{
    int l,r;
    lr(int l,int r):l(l),r(r){
        assert(l-1<=r);
    }
    bool operator<(const lr& rhs)const{
        return dis()<rhs.dis();
    }
    int dis()const{
        return r-l+1;
    }
    int mid(){
        return (l+r)/2;
    }
};

typedef priority_queue<lr> pqlr;

void work(int n,int k){
    pqlr p;
    p.push(lr(1,n));
    while(k--){
        lr cur=p.top();p.pop();
        int m=cur.mid();
//        cout<<cur.l<<ends<<cur.r<<ends<<m<<endl;

        lr l=lr(cur.l,m-1);
        lr r=lr(m+1,cur.r);

        if(k==0){
            int dl=l.dis();
            int dr=r.dis();
            printf("%d %d\n",max(dl,dr),min(dl,dr));
            return;
        }

        p.push(l);
        p.push(r);
    }
}

int main(){
    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("C-small-2-attempt1.out","w",stdout);
    int T;scanf("%d",&T);
    for(int t=1;t<=T;t++){
        int n,k;scanf("%d%d",&n,&k);
        printf("Case #%d: ",t);
        work(n,k);
    }
}


