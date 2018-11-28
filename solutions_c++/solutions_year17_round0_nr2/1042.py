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

bool tidy(ll n) {
    string s = to_string(n);
    for (size_t i = 0; i + 1 < s.size(); i++) {
        if (s[i] > s[i + 1]) return false;
    }
    return true;
}

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    ll n;
    cin >> n;
    if (tidy(n)) {
        cout << n << endl;
        return;
    }
    string s = to_string(n);
    ll ans = -1;
    forv(i, s) {
        if (s[i] > '1') {
            string t = s;
            t[i]--;
            for (int j = i + 1; j < t.size(); j++) t[j] = '9';
            ll m = stoll(t);
            if (tidy(m)) {
                ans = max(ans, m);
            }
        }
    }
    if (ans == -1) {
        ans = 0;
        forn(i, s.size() - 1) ans = ans * 10 + 9;
    }
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
