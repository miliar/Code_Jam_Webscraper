#include<bits/stdc++.h>
using namespace std;

int T,cs;
typedef long long ll;
ll n,k,s,x,y,a,b,d;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.ou","w",stdout);
    scanf("%d",&T);
    while(T--){
        cin>>n>>k;
        s=n;
        x=y=n;
        for(int i=0; 1; ++i){
            d=1LL<<i;
            a=s-d*x;
            b=d-a;
            if(k>d){
                k-=d;
                x=y=n/2;
                if(n%2==0)--x;
                if(x&1)n=y;
                else n=x;
                s-=d;
            }else{
                ll mx,mn,t;
                if(a>=k){
                    t=y;
                }else t=x;
                mx=mn=t/2;
                if(t%2==0)--mn;
                printf("Case #%d: %lld %lld\n",++cs,mx,mn);
                break;
            }
        }
    }
}
