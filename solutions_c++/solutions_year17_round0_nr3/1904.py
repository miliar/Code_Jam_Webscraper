#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#include <cassert>
#include <unordered_map>
#include <fstream>
#include <random>
#include <cstring>
#include <complex>
#include <bitset>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;
mt19937 rr(random_device{}());

ll C(ll n, ll k) {
    ll ans = 1;
    for (int i = 1; i <= k; ++i) {
        ans *= n - i + 1;
        ans /= i;
    }
    return ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int q;
    cin >> q;
    for (int t = 0; t < q; ++t) {
        cout << "Case #" << t + 1 << ": ";

        ll n, k;
        cin >> n >> k;
        map<ll, ll> mp;
        mp[n] = 1;
        for (; ; ) {
            auto it = mp.end();
            --it;
            ll x = it->first;
            ll cnt = it->second;
            if (cnt >= k) {
                cout << x / 2 << " " << (x - 1) / 2 << endl;
                break;
            }
            k -= cnt;
            mp[(x - 1) / 2] += cnt;
            mp[x / 2] += cnt;
            mp.erase(x);
        }
    }
    
}
