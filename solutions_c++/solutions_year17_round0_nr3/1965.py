#include <bits/stdc++.h>
using namespace std;

typedef vector<int> veci;
typedef pair<int,int> pii;
typedef vector<pii> vecii;
typedef long long ll;
typedef vector<ll> vecl;
typedef pair<ll,ll> pll;
typedef vector<pll> vecll;
#define EPS (1e-15)
#define MOD (int(1e9+7))
#define INF (int(1e9+9))
#define fi first
#define se second

int main()
{
    ios::sync_with_stdio(false);
    int tcases;
    cin >> tcases;
    for (int tc=1; tc<=tcases; ++tc)
{
    ll n, k;
    cin >> n >> k;
    map<ll,ll> mp;
    mp[n]++;
    ll cnt = 0;
    ll tot = 0;
    ll big=n, small=n;
    while (true) {
        tot += (1LL<<cnt);
        if (tot>=k)
            break;

        auto it = mp.find(n>>cnt);
        auto it2 = mp.find((n>>cnt)-1);
        big = small = n>>(cnt+1);
        if (it2!=mp.end()) {
            if (it2->fi%2) {
                mp[it2->fi/2] += 2*it2->se;
            } else {
                mp[it2->fi/2] += it2->se;
                mp[it2->fi/2-1] += it2->se;
                small = big - 1;
            }
        }
        if (it!=mp.end()) {
            if (it->fi%2) {
                mp[it->fi/2] += 2*it->se;
            } else {
                mp[it->fi/2] += it->se;
                mp[it->fi/2-1] += it->se;
                small = big-1;
            }
        }
        cnt++;
    }

    ll l, r;
    ll rem = tot-k;
    if (mp[small]>rem) {
        l = r = small/2;
        if (small!=0 && small%2==0) {
            r -= 1;
        }
    } else {
        l = r = big/2;
        if (big!=0 && big%2==0) {
            r -= 1;
        }
    }

    cout << "Case #" << tc << ": " << l << " " << r << endl;
}
    return 0;
}
