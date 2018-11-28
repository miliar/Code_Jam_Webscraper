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
char pk[1111];
int main(){
    scanf("%d",&t);
    while(t--){
        scanf("%s %d",pk,&n);
        int sl=strlen(pk);
        int ans=0;
        // printf("%s\n",pk);
        for (int i=0;i<sl; ++i){
            if(i+n > sl)break;
            if(pk[i]!='+'){
                ++ans;
                for(int j=0;j<n;++j){
                    pk[i+j]= pk[i+j] == '+' ?'-':'+';
                }
                // printf("%s\n",pk);
            }
        }
        bool ok = true;
        for(int i=0;i<sl;++i)if(pk[i]!='+')ok=false;
        if(ok) printf("Case #%d: %d\n", ++cs, ans);
        else printf("Case #%d: IMPOSSIBLE\n", ++cs);
    }
	return 0;
}
