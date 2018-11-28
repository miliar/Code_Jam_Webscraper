#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <numeric>
#include <list>
#include <deque>
#include <string>
#include <sstream>
#include <tuple>
using namespace std;
void go(vector<string> &a, int x, int y) {
    int n = a.size();
    int m = a[0].size();
    char ch = a[x][y];
    int x1 = x;
    int x2 = x;
    while (x1-1 >= 0) {
        if (a[x1-1][y] == a[x][y] || a[x1-1][y] == '?') {
            x1 -= 1;
        } else {
            break;
        }
    }
    while (x2+1 < n) {
        if (a[x2+1][y] == a[x][y] || a[x2+1][y] == '?') {
            x2 += 1;
        } else {
            break;
        }
    }
    for (int j=y; j<=m; j++) {
        bool ok = true;
        for (int i=x1; i<=x2; i++) {
            if (a[i][j] == '?' || a[i][j] == ch) {
            } else {
                ok = false;
            }
        }
        if (ok) {
            for (int i=x1; i<=x2; i++) {
                a[i][j] = ch;
            }
        } else {
            break;
        }
    }
    for (int j=y-1; j>=0; j--) {
        bool ok = true;
        for (int i=x1; i<=x2; i++) {
            if (a[i][j] == '?' || a[i][j] == ch) {
            } else {
                ok = false;
            }
        }
        if (ok) {
            for (int i=x1; i<=x2; i++) {
                a[i][j] = ch;
            }
        } else {
            break;
        }
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int tc=1; tc<=t; tc++) {
        int n, m;
        cin >> n >> m;
        vector<string> a(n);
        for (int i=0; i<n; i++) {
            cin >> a[i];
        }
        set<char> s;
        for (int j=0; j<m; j++) {
            for (int i=0; i<n; i++) {
                if (a[i][j] == '?') continue;
                if (s.count(a[i][j])) continue;
                go(a, i, j);
                s.insert(a[i][j]);
            }
        }
        cout << "Case #" << tc << ":" << '\n';
        for (int i=0; i<n; i++) {
            cout << a[i] << '\n';
        }
    }
    return 0;
}
