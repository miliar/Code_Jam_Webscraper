#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

int T, n, m;
string a[50];

int calc(int x1, int y1, int x2, int y2) {
    int cnt = 0;
    for (int i = x1; i <= x2; i++) {
        for (int j = y1; j <= y2; j++) {
            if (a[i][j] == '?');
            else cnt++;
        }
    }
    return cnt;
}

void print() {
    cout << "___________________" << endl;
    for (int i = 0; i < n; i++) {
        cout << a[i] << endl;
    }
    cout << "___________________" << endl;
}

void expand(int x1, int y1, int x2, int y2, char c) {
    while (y1 - 1 >= 0 && calc(x1, y1 - 1, x2, y1 - 1) == 0) {
        for (int i = x1; i <= x2; i++) a[i][y1 - 1] = c;
        y1--;
    }
    while (x1 - 1 >= 0 && calc(x1 - 1, y1, x1 - 1, y2) == 0) {
        for (int j = y1; j <= y2; j++) a[x1 - 1][j] = c;
        x1--;
    }
    while (y2 + 1 < m && calc(x1, y2 + 1, x2, y2 + 1) == 0) {
        for (int i = x1; i <= x2; i++) a[i][y2 + 1] = c;
        y2++;
    }
    while (x2 + 1 < n && calc(x2 + 1, y1, x2 + 1, y2) == 0) {
        for (int j = y1; j <= y2; j++) a[x2 + 1][j] = c;
        x2++;
    }
}

void solve() {
    vector<pair<pii, char> > v;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != '?') {
                v.pb(mp(mp(i, j), a[i][j]));
            }
        }
    }
    for (int i = 0; i < v.size(); i++) {
        int x = v[i].f.f, y = v[i].f.s;
        char c = v[i].s;
        expand(x, y, x, y, c);
    }
}

int main(){

    cin >> T;

    for (int j = 1; j <= T; j++) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        solve();
        cout << "Case #" << j << ":" << endl;
        for (int i = 0; i < n; i++) {
            cout << a[i] << endl;
        }
    }
    return 0;
}
