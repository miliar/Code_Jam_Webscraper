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
typedef pair<double, int> pdi;

#define show(x) cerr << x
#define debug(x) show(#x << ": " << (x) << endl)

const long double PI = 3.14159265358979323846;
const long double gammama = 0.57721566490153286060;
const long double eps = 1e-5;
const int INF = 1000 * 1000 * 1000 + 1;
const ll LINF = (ll)1000 * 1000 * 1000 * 1000 * 1000 * 1000;
const ll mod = 1000 * 1000 * 1000 + 7;
const ll N = 1001;

double solve(int u, int v, const vector<vector<ll> >& dist, int n, const vector<int>& e, const vector<int>& s) {
    vector<double> res(n, 1e15);
    res[u] = 0;
    vector<int> used(n, 0);
    used[u] = 1;
    for (int i = 0; i < n; ++i) {
        if (i == u)
            continue;
        if (dist[u][i] <= e[u])
            res[i] = 1.0 * dist[u][i] / s[u];
    }
    while (used[v] == 0) {
        int id = -1;
        double curMin = 1e16;
        for (int i = 0; i < n; ++i) {
            if (used[i])
                continue;
            if (res[i] < curMin) {
                curMin = res[i];
                id = i;
            }
        }
        used[id] = 1;
        for (int j = 0; j < n; ++j) {
            if (used[j])
                continue;
            if (dist[id][j] <= e[id])
                res[j] = min(res[j], res[id] + 1.0 * dist[id][j] / s[id]);
        }
        

    }
    return res[v];
}


void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> e(n), s(n);
    for (int i = 0; i < n; ++i)
        cin >> e[i] >> s[i];
    vector<vector<ll> > d(n, vector<ll>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> d[i][j];
            if (d[i][j] == -1)
                d[i][j] = LINF;
        }
    }
    vector<int> u(q), v(q);
    for (int i = 0; i < q; ++i) {
        cin >> u[i] >> v[i];
    }
    vector<vector<ll> > dist(d);
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    cout.precision(18);
    for (int i = 0; i < q; ++i) {
        cout << solve(u[i] - 1, v[i] - 1, dist, n, e, s) << " ";
    }
}


int main() {
    //freopen("C-small-2-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
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
