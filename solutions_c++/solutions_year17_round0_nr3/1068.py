#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

typedef long long ll;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

using namespace std;

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    ll n, k;
    cin >> n >> k;
    map<ll, ll> cnt;
    cnt[n] = 1;
    ll mx = 0, mn = 0;
    while (true) {
        auto m = *cnt.rbegin();
        mx = m.first / 2;
        mn = (m.first - 1) / 2;
        if (m.second >= k) {
            
            break;
        }
        
        k -= m.second;
        cnt.erase(m.first);
        if (mx) {
            cnt[mx] += m.second;
        }
        if (mn) {
            cnt[mn] += m.second;
        }
    }
    cout << mx << " " << mn << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
