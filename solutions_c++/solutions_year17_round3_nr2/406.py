#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int inf=0x3f3f3f3f;
const int maxn=2555;
int t,ac,aj,l,r,dp[maxn][maxn][2],res;
bool a[maxn],b[maxn];
inline void updMin(int &a,int b) {
    a=min(a,b);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        res=inf;
        memset(a,0,sizeof a);
        memset(b,0,sizeof b);
        scanf("%d%d",&ac,&aj);
        for (int i=0;i<ac;++i) {
            scanf("%d%d",&l,&r);
            for (int j=l+1;j<=r;++j)
                a[j]=1;
        }
        for (int i=0;i<aj;++i) {
            scanf("%d%d",&l,&r);
            for (int j=l+1;j<=r;++j)
                b[j]=1;
        }
        memset(dp,0x3f,sizeof dp);
        dp[0][0][0]=0;
        for (int i=1;i<=1440;++i)
            for (int j=1;j<=i;++j) {
                if (!a[i])
                    dp[i][j][0]=min(dp[i][j][0],min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1));
                if (!b[i])
                    dp[i][j][1]=min(dp[i][j][1],min(dp[i-1][j][1],dp[i-1][j][0]+1));
            }
        res=min(dp[1440][720][0],dp[1440][720][1]+1);
        memset(dp,0x3f,sizeof dp);
        dp[0][0][0]=0;
        for (int i=1;i<=1440;++i)
            for (int j=1;j<=i;++j) {
                if (!b[i])
                    dp[i][j][0]=min(dp[i][j][0],min(dp[i-1][j-1][0],dp[i-1][j-1][1]+1));
                if (!a[i])
                    dp[i][j][1]=min(dp[i][j][1],min(dp[i-1][j][1],dp[i-1][j][0]+1));
            }
        res=min(res,min(dp[1440][720][0],dp[1440][720][1]+1));
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
