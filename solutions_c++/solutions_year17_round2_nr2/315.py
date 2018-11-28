#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
#define _USE_MATH_DEFINES
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>
#include<map>
#include<ctime>
#include<cstdio>
#include<cassert>
#include<functional>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<char, char> pcc;
typedef pair<double, double> pdd;

#define show(x) cerr << x
#define debug(x) show(#x << ": " << (x) << endl)

const long double PI = 3.14159265358979323846;
const long double gammama = 0.57721566490153286060;
const long double eps = 1e-5;
const int INF = 1000 * 1000 * 1000 + 1;
const ll LINF = (ll)1000 * 1000 * 1000 * 1000 * 1000 * 1000;
const ll mod = 1000 * 1000 * 1000 + 7;
const int N = 1000000;


string solve(int r, int b, int y) {
    vector<pair<int, char> > a;
    a.emplace_back(r, 'r');
    a.emplace_back(b, 'b');
    a.emplace_back(y, 'y');
    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());

    string s = "";
    int n = r + b + y;
    char lst = 'x';
    for (int i = 0; i < n; ++i) {
        int m = 0, id = -1;
        for (int j = 0; j < 3; ++j) {
            if (a[j].second == lst)
                continue;
            if (a[j].first > m) {
                id = j;
                m = a[j].first;
            }
        }
        if (id == -1)
            return "";
        --a[id].first;
        s.push_back(a[id].second);
        lst = a[id].second;
    }
    if (s[0] == s[n - 1])
        return "";
    return s;
}

void solve() {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    if ((r == g) && (r + g == n)) {
        string res = "";
        for (int i = 0; i < n / 2; ++i) {
            res += "rg";
            
        }
        cout << res;
        return;
    }
    if ((b == o) && (b + o == n)) {
        string res = "";
        for (int i = 0; i < n / 2; ++i) {
            res += "bo";
            
        }
        cout << res;
        return;
    }
    if ((v == y) && (v + y == n)) {
        string res = "";
        for (int i = 0; i < n / 2; ++i) {
            res += "vy";
        }
        cout << res;
        return;
    }
    int ok = 1;
    if ((g > 0) && (r <= g))
        ok = 0;
    if ((v > 0) && (y <= v))
        ok = 0;
    if ((o > 0) && (b <= o))
        ok = 0;
    if (!ok) {
        cout << "IMPOSSIBLE";
        return;
    }
    int rr = r - g;
    int bb = b - o;
    int yy = y - v;
    string s = solve(rr, bb, yy);
    if (s == "") {
        cout << "IMPOSSIBLE";
        return;
    }
    int fr = 0, fb = 0, fy = 0;
    string res = "";
    for (int i = 0; i < s.size(); ++i) {
        res += s[i];
        if ((fr == 0) && (s[i] == 'r')) {
            for (int j = 0; j < g; ++j) {
                res += "gr";
            }
            fr = 1;
        }

        if ((fb == 0) && (s[i] == 'b')) {
            for (int j = 0; j < o; ++j) {
                res += "ob";
            }
            fb = 1;
        }

        if ((fy == 0) && (s[i] == 'y')) {
            for (int j = 0; j < v; ++j) {
                res += "vy";
            }
            fr = 1;
        }
    }
    cout << res;
    
    
}


int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
		std::cerr << i << endl;
	}
	return 0;
}
