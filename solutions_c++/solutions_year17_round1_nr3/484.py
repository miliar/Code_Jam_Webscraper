#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
#define zero(x) (((x)>0?(x):-(x))<eps)
typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int>PII;
typedef pair<double,int>PDI;
const double eps=1e-8;
const double pi=acos(-1.0);
const int inf=0x3f3f3f3f;
const int INF=2e9+7;
const int mod=1e9+7;
LL powmod(LL a,LL b) {LL res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
int q[110][110],r[110],num[110];
int n,p,hd,ad,hk,ak,b,d;
int solve(){
    int ans=inf;
    for(int i=0;i<=100;i++){
        for(int j=0;j<=100;j++){
            int num1=i,num2=j,ret=0,f=0,gg=0;
            int hd1=hd,ad1=ad,hk1=hk,ak1=ak,b1=b,d1=d;
            while(1){
                ret++;
                if(num1){
                    if(hd1-(ak1-d1)<=0){
                        if(gg==0){
                            gg=1;
                            hd1=hd;
                            hd1-=ak1;
                        }
                        else{
                            f=1;
                            break;
                        }
                    }
                    else{
                        ak1=max(ak1-d1,0);
                        gg=0;
                        hd1-=ak1;
                        num1--;
                    }
                }
                else if(num2){
                    if(hd1-ak1<=0){
                        if(gg==0){
                            gg=1;
                            hd1=hd;
                            hd1-=ak1;
                        }
                        else {
                            f=1;
                            break;
                        }
                    }
                    else{
                        ad1+=b1;
                        gg=0;
                        hd1-=ak1;
                        num2--;
                    }
                }
                else{
                    if(hk1-ad1<=0){
                        break;
                    }
                    if(hd1-ak1<=0){
                        if(gg==0){
                            gg=1;
                            hd1=hd;
                            hd1-=ak1;
                        }
                        else{
                            f=1;
                            break;
                        }
                    }
                    else{
                        hk1-=ad1;
                        hd1-=ak1;
                        gg=0;
                    }
                }
            }
            if(!f) ans=min(ans,ret);
        }
    }
    return ans;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--){
        cin>>hd>>ad>>hk>>ak>>b>>d;
        printf("Case #%d: ",cas++);
        int res=solve();
        if(res==inf) printf("IMPOSSIBLE\n");
        else printf("%d\n",res);
    }
    return 0;
}
