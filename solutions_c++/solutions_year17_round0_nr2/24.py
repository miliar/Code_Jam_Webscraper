#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <bitset>

using namespace std;

#define FOR(a, b) for (int a = 0; a < (b); ++a)
#define clr(a) memset(a, 0, sizeof(a))
#define pb push_back
#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)
#ifdef LOCAL
#define debug(a) cerr << #a << ": " << a << '\n';
#else
#define debug(a)
#endif

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;
const ld PI = acos(-1.0L);
const int MAXN = 1e5;

void solve() {
    string s;
    cin >> s;
    for (int i = 0; i < s.length(); ++i) {
        int j = i;
        while (j < s.length() && s[j] == s[i]) {
            j++;
        }
        if (j < s.length() && s[j] < s[i]) {
            s[i]--;
            for (j = i + 1; j < s.length(); ++j) {
                s[j] = '9';
            }
            break;
        }
    }
    cout << stoll(s);
}

int main() {
#ifdef LOCAL
    freopen("b.in", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    forn(i, T) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }

    return 0;
}

