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
const int MAXN();

int dp[805][805][2][2], t[24*60+5];

void solve(int test){

    int n,m;
    S("%d%d",&n,&m);

    REP(i,24*60+1)
        t[i] = 0;

    REP(i,n)
    {
        int x,y;
        S("%d%d",&x,&y);
        FOR(j,x,y-1)
            t[j] = 1;
    }

    REP(i,m)
    {
        int x,y;
        S("%d%d",&x,&y);
        FOR(j,x,y-1)
            t[j] = 2;
    }

    FOR(i,0,720)
        FOR(j,0,720)
            REP(k,2)
                REP(l,2)
                    dp[i][j][k][l] = INF;

    if(t[0] != 1)
        dp[1][0][0][0] = 0;

    if(t[0] != 2)
        dp[0][1][1][1] = 0;

    FOR(i,0,720)
        FOR(j,0,720)
        {
            if(i == 0 && j == 0) continue;

            if(t[i+j] != 1)
            {
                dp[i+1][j][0][0] = min(dp[i+1][j][0][0], min(dp[i][j][0][0], dp[i][j][0][1]+1));
                dp[i+1][j][1][0] = min(dp[i+1][j][1][0], min(dp[i][j][1][0], dp[i][j][1][1]+1));
            }

            if(t[i+j] != 2)
            {
                dp[i][j+1][0][1] = min(dp[i][j+1][0][1], min(dp[i][j][0][0]+1, dp[i][j][0][1]));
                dp[i][j+1][1][1] = min(dp[i][j+1][1][1], min(dp[i][j][1][0]+1, dp[i][j][1][1]));
            }

        }

    int ans = dp[720][720][0][0];

    ans = min(ans, dp[720][720][1][1]);
    ans = min(ans, dp[720][720][0][1]+1);
    ans = min(ans, dp[720][720][1][0]+1);

    P("Case #%d: %d\n",test,ans);

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
