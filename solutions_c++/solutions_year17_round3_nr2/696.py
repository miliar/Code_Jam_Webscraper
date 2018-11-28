#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

typedef long long ll;
typedef long double ld;
typedef priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pqG; // smaller first
typedef pair<int,int> pii;
typedef vector<int> vi;
#define S(a) scanf("%d",&a)
#define LS(a) scanf("%lld",&a)
#define D(a) scanf("%lf",&a)
#define LD(a) scanf("%lf",&a)
#define FOR(i,a,b) for(int i = a;i <= b;++i)
#define DOW(i,b,a) for(int i = b; i >= a;--i)
#define eb emplace_back
#define fi first
#define se second


const ld DINF = 1e45;
const ll INF = 1e17;
const ll MOD = 1e9 + 7;
ll power(ll base,ll expo,ll MOD)
{
    ll res = 1;
    while(expo > 0)
    {
        if(expo & 1) res = (res * base) % MOD;
        base = (base * base ) % MOD;
        expo>>= 1;

    }

    return res;




}
pii time1[101],time2[101];
ll dp[3][2][721][721];
ll check[1442];
ll solve(int ta,int tb,int turn,int st)
{
    if(ta + tb  == 1440) return st == turn ? -1:0;
    if(dp[turn][st][ta][tb] != -1) return dp[turn][st][ta][tb];

    ll ans = INF;
    ll time = ta + tb;
    if(check[time] != turn )
    {
        if(turn == 0 && ta + 1 <= 720)
        {
            ans = min(ans, solve(ta + 1,tb,0,st) );

        }
        if(turn == 1 && tb + 1<= 720)
        {
            ans = min(ans, solve(ta,tb + 1,1,st) );
        }
    }

    if(((turn == 0) || (turn == 2))&& tb + 1 <= 720 && check[time] != 1)
    {
        ans = min(ans, 1 + solve(ta,tb + 1,1,turn == 2 ? 1:st) );

    }
    if(((turn == 1) || (turn == 2)) && ta + 1<= 720 && check[time] != 0)
    {
        ans = min(ans, 1 + solve(ta + 1,tb,0,turn == 2 ? 0:st) );
    }
    return dp[turn][st][ta][tb] = ans;


}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    S(t);
    for(int tc = 1; tc <= t; ++tc)
    {
        int Ac,Aj;
        S(Ac),S(Aj);
        FOR(i,0,1440) check[i] = 2;
        FOR(i,0,Ac-1)
        {
            S(time1[i].first),S(time1[i].second);
            FOR(j,time1[i].first,time1[i].second - 1)
            check[j] = 0;
        }
        FOR(i,0,Aj-1)
        {
            S(time2[i].first),S(time2[i].second);
            FOR(j,time2[i].first,time2[i].second - 1)
            check[j] = 1;

        }
        FOR(k,0,1){
        FOR(i,0,720)
        {
            FOR( j,0,720)
            {

                dp[0][k][i][j] = dp[1][k][i][j] = dp[2][k][i][j] = -1;
            }
        }
        }
      //  dp[2][0][0] = -1;
        printf("Case #%d: %lld\n",tc,solve(0,0,2,1));


    }

    return 0;
}

