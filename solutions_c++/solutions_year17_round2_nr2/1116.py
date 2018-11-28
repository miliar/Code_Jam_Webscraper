#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <ctime>

#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<ld, ld> point;

const int N = (int)(1e3) + 7;
const int M = (int)(32);
const ld eps = 1e-12;
const ll MOD = (ll)(1e9) + 7;
const ll INF = (ll)(1e9) + 7;

string s, ans;
int n;
int cur_t;

void rec(int num, int r, int y, int b) {
    if (clock() - cur_t > 30000) {
        return ;
    }
    if (num == n) {
        if (s[n - 1] != s[0] || n == 1) {
            ans = s;
        }
        return ;
    }
    if (r > y + b + 1 || y > r + b + 1 || b > r + y + 1)
        return ;
    //cout << r << ' ' << y << ' ' << b << endl;
    if (s[num - 1] != 'R' && r) {
        s[num] = 'R';
        rec(num + 1, r - 1, y, b);
        if (ans.size() > 0) {
            return ;
        }
    }
    if (s[num - 1] != 'Y' && y) {
        s[num] = 'Y';
        rec(num + 1, r, y - 1, b);
        if (ans.size() > 0) {
            return ;
        }
    }
    if (s[num - 1] != 'B' && b) {
        s[num] = 'B';
        rec(num + 1, r, y, b - 1);
        if (ans.size() > 0) {
            return ;
        }
    }
}

void solve(int iii) {
    cout << "Case #" << iii << ": ";
    cin >> n;
    int r, o, y, g, b, v;
    cin >> r >> o >> y >> g >> b >> v;
    s = "";
    for (int i = 0; i < n; ++i)
        s += 'q';
    ans = "";
    cur_t = clock();
    if (r) {
        s[0] = 'R';
        rec(1, r - 1, y, b);
        if (ans.size() > 0) {
            cout << ans << endl;
            return ;
        }
    }
    cur_t = clock();
    if (y) {
        s[0] = 'Y';
        rec(1, r, y - 1, b);
        if (ans.size() > 0) {
            cout << ans << endl;
            return ;
        }
    }
    cur_t = clock();
    if (b) {
        s[0] = 'B';
        rec(1, r, y, b - 1);
        if (ans.size() > 0) {
            cout << ans << endl;
            return ;
        }
    }
    cout << "IMPOSSIBLE" << endl;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    //freopen("brackets.in", "r", stdin);
    //freopen("brackets.out", "w", stdout);
    int ttt;
    cin >> ttt;
    for (int i = 0; i < ttt; ++i) {
        solve(i + 1);
    }
    return 0;
}
