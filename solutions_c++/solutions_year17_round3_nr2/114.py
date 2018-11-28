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

const int MXN = 1504;
int dp[MXN][MXN][2];
bool zaj[MXN][2];
int MXT = 720;

void calcdp(int mode)
    {
    FOR(i, 0, MXT)
        FOR(j, 0, MXT)
            dp[i][j][0] = dp[i][j][1] = 1e9;
            
    if(mode == 0) if(!zaj[0][0])dp[1][0][0] = 0;
    if(mode == 1) if(!zaj[0][1])dp[0][1][1] = 0;
    FOR(i, 0, MXT)
        {
        FOR(j, 0, MXT)
            {
            int time = i + j - 1;
            if(!zaj[time][0] && i)
                {
                mini(dp[i][j][0], dp[i-1][j][0]);
                mini(dp[i][j][0], dp[i-1][j][1] + 1);
                }
            if(!zaj[time][1] && j)
                {
                mini(dp[i][j][1], dp[i][j-1][1]);
                mini(dp[i][j][1], dp[i][j-1][0] + 1);
                }
//            cerr<<i<<" "<<j<<" "<<dp[i][j][0]<<" "<<dp[i][j][1]<<endl;
            }
        }
    }

void solve()
    {
    int n, k;
    scanf("%d%d", &n, &k);
    
    FOR(i, 0, MXT*2)
        zaj[i][0] = zaj[i][1] = 0;
    
    FOR(i, 1, n)
        {
        int a, b;
        scanf("%d%d", &a, &b);
        FOR(j, a, b-1)
            zaj[j][0] = 1;
        }
    FOR(i, 1, k)
        {
        int a, b;
        scanf("%d%d", &a, &b);
        FOR(j, a, b-1)
            zaj[j][1] = 1;
        }
    int result = 1e9;
    calcdp(0);
    mini(result, dp[MXT][MXT][0]);
    mini(result, dp[MXT][MXT][1] + 1);
    calcdp(1);
    mini(result, dp[MXT][MXT][1]);
    mini(result, dp[MXT][MXT][0] + 1);

    
    printf("%d\n", result);
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
