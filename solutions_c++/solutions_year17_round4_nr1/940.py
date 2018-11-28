#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstdlib>
#include<string>
#include<bitset>
#include<iomanip>
#include<deque>
#include<utility>
#include<functional>
#include<sstream>
#define INF 1000000000
#define fi first
#define se second
#define N 100005
#define P 1000000007
#define debug(x) cerr<<#x<<"="<<x<<endl
#define MP(x,y) make_pair(x,y)
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;
int dp[105][105][105][4];
int c[5];
void upd(int &x, int y)
{
    if (x == -1)
        x = y;
    else if (y > x)
        x = y;
}
int main()
{
    int i, j,k ,l,s, T, test = 0, n, p, x, ans = 0,tdp;
    
    freopen("Alarge.in", "r", stdin);
    freopen("Alarge.out", "w", stdout);
    cin >> T;
    while (T--)
    {
        ans = 0;
        memset(c, 0, sizeof(c));
        printf("Case #%d: ", ++test);
        cin >> n >> p;
        for (i = 1; i <= n; i++)
            cin >> x, c[x%p]++;
        ans += c[0];
        //debug(ans);
        memset(dp, -1, sizeof(dp));
        dp[0][0][0][0] = 0;
        for(i=0;i<=c[1];i++)
            for(j=0;j<=c[2];j++)
                for(k=0;k<=c[3];k++)
                    for(l=0;l<p;l++)
                        if (dp[i][j][k][l] != -1)
                        {
                            tdp = dp[i][j][k][l]+(l==0);
                            for (s = 1; s < p; s++)
                            {
                                if (s == 1 && i < c[1])
                                    upd(dp[i + 1][j][k][(l + s) % p], tdp);
                                if (s == 2 && j < c[2])
                                    upd(dp[i][j+1][k][(l + s) % p], tdp);
                                if (s == 3 && k < c[3])
                                    upd(dp[i][j][k+1][(l + s) % p], tdp);
                            }
                        }
        int rel = -1;
        for (l = 0; l < p; l++)
            upd(rel, dp[c[1]][c[2]][c[3]][l]);
        cout << ans + rel << endl;
    }
    return 0;
}
// davidlee1999WTK 2017/
// ios::sync_with_stdio(false);
//#pragma comment(linker, "/STACK:102400000,102400000") compiler c++,not g++
/*

*/
