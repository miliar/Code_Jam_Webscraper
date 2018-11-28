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
const int MAXN(1005);

PII a[MAXN];

double dp[MAXN][MAXN], PI = 2*acos(0);

void solve(int test){

    int n,k;
    S("%d%d",&n,&k);
    REP(i,n)
        S("%d%d",&a[i].X,&a[i].Y);

    sort(a,a+n,greater<PII>());

    FOR(i,0,n)
        FOR(j,0,n)
            dp[i][j] = -1.0;

    REP(i,n)
        dp[i][1] = PI*a[i].X*1.0*a[i].X + 2.0*PI*a[i].X*1.0*a[i].Y;

    FOR(j,2,k)
        REP(i,n)
            REP(l,i)
            {
                if(dp[l][j-1] == -1.0) continue;
                double area = 2.0*PI*a[i].X*1.0*a[i].Y;
                dp[i][j] = max(dp[i][j], dp[l][j-1]+area);
            }

    double ans = -1.0;

    REP(i,n)
        ans = max(ans, dp[i][k]);

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
