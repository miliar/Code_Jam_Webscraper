/*
  ------------------------- Hachiikung ---------------------------------
  ---------------------- Worrachate Bosri ------------------------------
  ------ Faculty of Computer Engineering Chulalongkorn University ------
*/
#include <bits/stdc++.h>
using namespace std;
#define REP(i,FN) for(int i=0;i<FN;i++)
#define FOR(i,ST,FN) for(int i=ST;i<=FN;i++)
#define FORD(i,FN,ST) for(int i=FN;i>=ST;i--)
#define FORX(i,c) for(typeof(c.begin())i=c.begin();i!=c.end();i++)
#define pause system("pause")
#define S scanf
#define P printf
#define X first
#define Y second
#define pb push_back
#define PII pair<int,int>
#define mp make_pair
#define sz size()
#define eps 1e-8

const int MOD(1000000007);
const int INF((1<<30)-1);
const int MAXN(105);

int a[MAXN], b[MAXN], g[MAXN][MAXN], s, t;

double dp[MAXN][MAXN];

long long dis[MAXN];

void solve(int test){

    int n,q;
    S("%d%d",&n,&q);
    REP(i,n)
        S("%d%d",&a[i],&b[i]);
    REP(i,n)
        REP(j,n)
            S("%d",&g[i][j]);
    REP(i,q)
        S("%d%d",&s,&t);

    REP(i,n)
        REP(j,n)
            dp[i][j] = -1.0;

    FOR(i,1,n-1)
        dis[i] = dis[i-1] + g[i-1][i];

    dp[0][0] = 0;

    FOR(i,1,n-1)
        FOR(j,0,i-1)
        {
            if(dp[i-1][j] >= 0 && dis[i]-dis[j] <= a[j])
            {
                if(dp[i][j] < 0) dp[i][j] = dp[i-1][j] + (dis[i]-dis[i-1])*1.0/b[j];
                else dp[i][j] = min(dp[i][j], dp[i-1][j] + (dis[i]-dis[i-1])*1.0/b[j]);

                if(dp[i][i] < 0) dp[i][i] = dp[i][j];
                else dp[i][i] = min(dp[i][i], dp[i][j]);
            }
        }

    double ans = -1.0;

    REP(j,n)
    {
        if(dp[n-1][j] < 0) continue;
        if(ans < 0) ans = dp[n-1][j];
        else ans = min(ans, dp[n-1][j]);
    }

    P("Case #%d: %.10f\n",test,ans);

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
