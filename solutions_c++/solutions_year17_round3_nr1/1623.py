#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
#define debug(a) cout<<a<<endl
#define clr(a) memset(a,0,sizeof(a))
#define clrne(a) memset(a,-1,sizeof(a))
#define clrinf(a) memset(a,0x3f,sizeof(a))
#define clrneinf(a) memset(a,0xc0,sizeof(a))
#define pb(a) push_back(a)
#define maxn 1010
#define mod 1000000007
#define eps 1e-9
#define inf 0x7fffffff
#define mp(a,b) make_pair(a,b)
const double pi = acos(-1.);
struct node
{
    int R;
    int H;
};
double dp[maxn][maxn];
bool cmp(node a,node b) {return a.R>b.R;}
node a[maxn];
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int caseno = 0;
    while (T--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for (int i = 1; i<=n; i++)
            scanf("%d%d",&a[i].R,&a[i].H);
        sort(a+1,a+1+n,cmp);
        clr(dp);
        double ans = 0;
        for (int i = 1; i<=n; i++)
        {
            dp[i][1] = 2*pi*a[i].R*a[i].H + pi * a[i].R * a[i].R;
            for (int j = 1;j<=k;j++)
            {
                dp[i][j] = max(dp[i][j],dp[i-1][j-1] + 2*pi*a[i].R*a[i].H);
            }
            for (int j = 0;j<=k;j++)
                dp[i][j] = max(dp[i][j],dp[i-1][j]);
            ans = max(ans,dp[i][k]);
        }
        printf("Case #%d: %.12f\n",++caseno,ans);
    }
    return 0;
}
