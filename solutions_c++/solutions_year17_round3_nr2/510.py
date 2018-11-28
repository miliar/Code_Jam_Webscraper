#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);//freopen("out.txt","w",stdout);
#define getfile char fin[11], fout[11]; sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define makefile char fout[11]; sprintf(fout, "%d.in", i); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;


bool ta[2000], tb[2000];
int dp[2000][2000][2][2];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas = 1;
    scanf("%d", &t);
    while(t--)
    {
        int n, m;
        scanf("%d%d", &n, &m);
        memset(ta, 0, sizeof(ta));
        memset(tb, 0, sizeof(tb));
        for(int i = 0; i < n; i++)
        {
            int x, y;
            scanf("%d%d", &x, &y);
            for(int j = x; j < y; j++)
                ta[j] = 1;
        }
        for(int i = 0; i < m; i++)
        {
            int x, y;
            scanf("%d%d", &x, &y);
            for(int j = x; j < y; j++)
                tb[j] = 1;
        }
        memset(dp, 0x3f, sizeof(dp));
        if(ta[0]==0)
            dp[0][0][0][0] = 0;
        if(tb[0]==0)
            dp[0][0][1][1] = 0;
        for(int i = 1; i <= 1440; i++)
        {
            for(int j = 0; j < i; j++)
            {
                if(ta[i] == 0)
                {
                    dp[i][j + 1][0][0] = min(dp[i - 1][j][0][0], dp[i - 1][j][1][0] + 1);
                    dp[i][j + 1][0][1] = min(dp[i - 1][j][0][1], dp[i - 1][j][1][1] + 1);
                }
                if(tb[i] == 0)
                {
                    dp[i][j][1][0] = min(dp[i - 1][j][1][0], dp[i - 1][j][0][0] + 1);
                    dp[i][j][1][1] = min(dp[i - 1][j][1][1], dp[i - 1][j][0][1] + 1);
                }
            }
        }
        cerr<<cas<<endl;
        int ans = min(dp[1440][720][0][0], dp[1440][720][1][1]);
        int ans2 = min(dp[1440][720][0][1], dp[1440][720][1][0]) + 1;
        printf("Case #%d: %d\n", cas++, min(ans, ans2));
    }
    return 0;
}

