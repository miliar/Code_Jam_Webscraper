#include<bits/stdc++.h>
#define PII pair<int,int>
#define f first
#define s second
#define VI vector<int>
#define LL long long
#define MP make_pair
#define LD long double
#define PB push_back
#define ALL(V) V.begin(),V.end()
#define abs(x) max((x),-(x))
#define PDD pair<LD,LD> 
#define VPII vector< PII > 
#define siz(V) ((int)V.size())
#define FOR(x, b, e)  for(int x=b;x<=(e);x++)
#define FORD(x, b, e) for(int x=b;x>=(e);x--)
#define REP(x, n)     for(int x=0;x<(n);x++)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define VVI vector<VI>
using namespace std;

const int MXN = 1004;
LD dp[MXN][MXN];
void solve()
    {
    int n, k;
    scanf("%d%d", &n, &k);
    FOR(i, 0, n)
        FOR(j, 0, k)
            dp[i][j] = 0;
    VPII V;
    FOR(i, 1, n)
        {
        int a, b;
        scanf("%d%d", &a, &b);
        V.PB(MP(a, b));
        }
    V.PB(MP(1e9, -1));
    sort(ALL(V));
    reverse(ALL(V));
    FOR(i, 1, n)
        {
        dp[i][1] = M_PI * V[i].f * V[i].f + 2 * M_PI * V[i].f * V[i].s;
        maxi(dp[i][1], dp[i-1][1]);
        }
    FOR(i, 1, n)
        {
        FOR(j, 1, k)
            {
            maxi(dp[i][j], dp[i-1][j-1] + 2 * M_PI * V[i].f * V[i].s);
            maxi(dp[i][j], dp[i-1][j]);
            }
        }
    printf("%.8Lf\n", dp[n][k]);
    }
int main()
{
int z;
scanf("%d",&z);
    FOR(iii,1,z)
    {
    printf("Case #%d: ",iii);
    solve();
    }
}
