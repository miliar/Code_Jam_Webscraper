// Nurbakyt Madibek
// Look at my code! IT'S AWESOME

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;
const double eps = 1e-6;

const int MAX_N = (int)1e5 + 123;

int n, m;
char a[30][30];

void solve() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> a[i][j];
    int id = -1;
    for (int i = 1; i <= n; i++) {
        bool good = 0;
        for (int j = 1; j <= m; j++) {
            if (a[i][j] != '?') {
                good = 1;
                break;
            }
        }
        if (good) {
            id = i;
            break;
        }
    }
    assert(id != -1);
    for (int i = id; i <= n; i++) {
        bool good = 0;
        for (int j = 1; j <= m; j++) {
            if (a[i][j] != '?') {
                good = 1;
                break;
            }
        }
        if (good) {
            for (int j = 1; j <= m; ) {
                int k = j;
                while(k <= m && a[i][k] == '?')
                    k++;
                char tp = (k == m + 1 ? a[i][j - 1] : a[i][k]);
                for (int it = j; it < k; it++)
                    a[i][it] = tp;
                j = k + 1;
            }
        }
        else {
            for (int j = 1; j <= m; j++)
                a[i][j] = a[i - 1][j];
        }
    }
    for (int i = 1; i < id; i++)
        for (int j = 1; j <= m; j++)
            a[i][j] = a[id][j];
    for (int i = 1; i <= n; i++, cout << endl)
        for (int j = 1; j <= m; j++)
            cout << a[i][j];
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int tests;
    cin >> tests;
    for (int it = 1; it <= tests; it++) {
        cout << "Case #" << it << ':' << endl;
        solve();
    }
    return 0;
}
