#include<bits/stdc++.h>
#define N 111111
#define M 555555
#define LL long long
#define FI(i,a,b) for(int i=(a);i<=(b);++i)
#define FD(i,a,b) for(int i=(a);i>=(b);--i)
#define RP(i,n) for(int i=0;i<(n);++i)
#define CR(a,b) memset(a,b,sizeof(a))
#define AL(a) a.begin(),a.end()
#define LC(x) (x<<1)
#define RC(x) (lc(x)|1)
#define INF 0x3f3f3f3f
#define SI(n) scanf("%d",&n)
#define SI2(a,b) scanf("%d %d",&a,&b)
#define SF(n) scanf("%lf",&n)
#define PB push_back
#define MP make_pair
#define VI vector<int>
using namespace std;
int t,n,m,q,k,ans,cs=0;
int d[33];
char pk[33];
int main(){
    scanf("%d",&t);
    while(t--){
        ++cs;
        scanf("%s",pk);
        int sl=strlen(pk);
        for(int i=0; i<sl;++i) d[i] = pk[i] - '0';
        for(int i=sl-1;i>0;--i){
            int fp=-1;
            for(int j=i-1;j>=0;--j){
                if(d[j]>d[i]){
                    fp=j;
                    break;
                }
            }
            if(fp!=-1){
                --d[fp];
                for(int j=fp+1;j<sl;++j)d[j]=9;
            }
        }
        for(int i=sl-1;i>0;--i){
            if(d[i]<0){
                d[i]+=10;
                d[i-1]-=1;
            }
        }
        int hv=-1;
        for(int i=0;i<sl;++i){
            if(d[i]>0){
                hv=i;
                break;
            }
        }
        printf("Case #%d: ",cs);
        for(int i=hv;i<sl;++i)printf("%d",d[i]);
        puts("");
    }
	return 0;
}

