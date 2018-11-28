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
const double PI = acos(-1.0);

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
int n,k;
vector<pii> ck;
double dp[1002][1002];
bool done[1002][1002];
double solve(int i ,int last)
{
    if(i == k + 1) return 0;
    if(done[i][last] != 0) return dp[i][last];
    double ans = 0.0;
    for(int j = last + 1; j <=  n;++j)
    {
       double area = (PI * ck[j].first) *ck[j].first + 2.0 * PI * ck[j].first *ck[j].second ;
       if(last != 0) area -= (PI * ck[last].first) * ck[last].first;
       ans = max(ans, area + solve(i + 1,j));
    }
    done[i][last] = 1;
    return dp[i][last] = ans;

}
void reset()
{
   FOR(i,0,1001)
    FOR(j,0,1001)
      dp[i][j] = -1.0,done[i][j] = 0;

}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    S(t);
    for(int tc = 1; tc <= t; ++tc)
    {
       S(n),S(k);
       ck.assign(n + 1,{0,0});
       FOR(i,1,n) S(ck[i].first),S(ck[i].second);
       sort(ck.begin(),ck.end());
       reset();
       printf("Case #%d: %0.16lf\n",tc,solve(1,0));


    }

    return 0;
}

