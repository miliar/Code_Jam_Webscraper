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
        ll n;
        cin >> n;
        vector<int> d;
        for (; n > 0; n /= 10) 
            d.push_back(n % 10);
        reverse(all(d));
        
        bool f = false;
        for (int i = 0; i < sz(d); ++i) {
            if (f) {
                d[i] = 9;
            } else {
                bool fl = true;
                for (int j = i + 1; j < sz(d); ++j) {
                    if (d[j] != d[i]) {
                        if (d[j] < d[i])
                            fl = false;
                        break;
                    }
                }
                if (!fl) {
                    --d[i];
                    f = true;
                }
            }
        }

        for (int i = 0; i < sz(d); ++i) {
            if (i != 0 || d[i] != 0)
                cout << d[i];
        }
        cout << endl;

    }
    
}
