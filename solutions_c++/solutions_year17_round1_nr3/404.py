#include<bits/stdc++.h>

typedef long long lnt;
struct ele{
    int hd,ad,hk,ak,d;
};
struct qq{
    int a,b,c,d;
};
std::map<qq,bool>mp;
std::queue<ele>Q;
int main(){
    //freopen("C.txt","r",stdin);
    //freopen("C-out.txt","w",stdout);
    int T,t=0;
    scanf("%d",&T);
    while(T--){
        t++;
        int a,b,c,d,B,D;
        scanf("%d%d%d%d%d%d",&a,&b,&c,&d,&B,&D);
        int hh=a;
        while(Q.size()) Q.pop();
        mp.clear();
        int ans=-1;
        Q.push(ele{a,b,c,d,0});
        while(Q.size()){
            ele x=Q.front();
            Q.pop();
            int now=x.d;
            a=x.hd,b=x.ad,c=x.hk,d=x.ak;
            qq y;
            if(b>=c){
                ans=now+1;
                break;
            }
            if(a>d){
                y.a=a-d,y.b=b,y.c=c-b,y.d=d;
                if(!mp[y]){
                    Q.push(ele{a-d,b,c-b,d,now+1});
                    mp[y]=true;
                }
                y.a=a-d,y.b=b+B,y.c=c,y.d=d;
                if(!mp[y]){
                    Q.push(ele{a-d,b+B,c,d,now+1});
                    mp[y]=true;
                }
            }
            if(hh>d){
                y.a=hh-d,y.b=b,y.c=c,y.d=d;
                if(!mp[y]){
                    Q.push(ele{hh-d,b,c,d,now+1});
                    mp[y]=true;
                }
            }
            int td=d-D;
            if(td<0) td=0;
            if(a>td){
                y.a=a-td,y.b=b,y.c=c,y.d=td;
                if(!mp[y]){
                    Q.push(ele{a-td,b,c,td,now+1});
                    mp[y]=true;
                }
            }
        }
        printf("Case #%d: ",t);
        if(ans==-1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}
