#include <stdio.h>
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

#define LSOne(S) (S & (-S))
#define MOD 1000000007
#define INF 1000000000
#define EPS 1e-9

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef pair<int, string> ps;
typedef pair<ll, char> pc;
typedef pair<pi, int> pii;
typedef pair<double, double> pd;
typedef pair<ll, ll> pll;
typedef pair<double, int> pdi;

typedef
tree<
  pi,
  null_type,
  less<pi>,
  rb_tree_tag,
  tree_order_statistics_node_update>
ordered_multiset;

pll pancakes[1005];
ll dp[1005][1005];

ll DP(int take, int limiter)
{
    if(take == 0) return 0;
    if(dp[take][limiter] != 0) return dp[take][limiter];

    int limiterLeft = take;
    ll ans = 0;
    for(int i = limiterLeft; i < limiter; ++i)
    {
        ans = max(ans, pancakes[i].first * pancakes[i].second * 2 + DP(take-1, i));
    }

    return dp[take][limiter] = ans;
}

double PI() { return std::atan(1)*4; }

int main()
{
    std::ios::sync_with_stdio(false);
    ifstream is("A-large.txt");
    ofstream os("A_ans.txt");
    //cout << fixed;
    //cout << setprecision(9);
    os << fixed;
    os << setprecision(9);

    int tc;
    //cin >> tc;
    is >> tc;
    int tcnum = 1;

    while(tc--)
    {
        memset(dp, 0, sizeof(dp));
        int n, k;
        //cin >> n >> k;
        is >> n >> k;

        for(int i = 1; i <= n; ++i)
        {
            //cin >> pancakes[i].first >> pancakes[i].second;
             is >> pancakes[i].first >> pancakes[i].second;
        }

        sort(pancakes+1, pancakes+1+n);
//        for(int i = 1; i <= n; ++i)
//        {
//            cout << "rad " << i << " " << pancakes[i].first << " " << pancakes[i].second << endl;
//        }

        ll ans = 0;

        for(int i = k; i <= n; ++i)
        {
            ans = max(ans, (pancakes[i].first * pancakes[i].first + 2 * pancakes[i].first * pancakes[i].second) + DP(k-1,i));
        }
        //cout << "ans is " << ans << "\n";

        double realAns = (double)ans * PI();
        //cout << "Case #" << tcnum << ": " << realAns << "\n";
        os << "Case #" << tcnum << ": " << realAns << "\n";
        ++tcnum;
    }
    return 0;
}
