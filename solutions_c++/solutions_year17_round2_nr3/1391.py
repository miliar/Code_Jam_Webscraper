#include <cassert>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <numeric>
#include <bitset>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <functional>
#include <cstring>
#include <ctime>
#include <memory.h>
#include <future>
#include <iomanip>

#define y1 AAA_BBB
#define y0 AAA_AAA

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef double ld;
typedef vector<i64> vi64;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<pair<double, double>> vdd;

typedef vector<vi64> vvi64;

template <class T> T inline sqr(T x) {
    return x * x;
}

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;
const i64 inf  = 1e18;

template<typename T>
bool uin(T& x, T y) {
    if (x > y) { x = y; return 1;}
    return 0;
}


vector<ld> solve(int n, vvi64 dist, vdd horses, vpi qs) {
    forn (t, n)
        forn (i, n) forn (j, n)
                uin(dist[i][j], dist[i][t] + dist[t][j]);
    vector<vector<ld>> g(n, vector<ld>(n, inf));
    forn (i, n) {
        forn (j, n) {
            if (i == j) g[i][j] = 0;
            else {
                if (dist[i][j] <= horses[i].fi)
                    g[i][j] = dist[i][j] / horses[i].se;
            }
        }
    }
    forn (t, n)
        forn (i, n) forn (j, n)
                uin(g[i][j], g[i][t] + g[t][j]);
    vector<ld> res;
    for (auto x: qs) {
        res.pb(g[x.fi][x.se]);
    }
    return res;
}

int main() {
    //auto start = chrono::system_clock::now();
    string name = "C-large";    string path = "";

    freopen((path + name + ".in").c_str(), "r", stdin);
    freopen((path + name + ".out").c_str(), "w", stdout);

    int test_cases;
    cin >> test_cases;
    vector<future<vector<ld> >> futures(test_cases);

    for (int test_case = 1; test_case <= test_cases; test_case++) {
        int Q, N;
        cin >> N >> Q;
        vdd horses(N); vvi64 dist(N, vi64(N, inf)); vpi qs(Q);
        forn (i, N) cin >> horses[i].fi >> horses[i].se;
        forn (i, N) forn (j, N) {cin >> dist[i][j]; if (dist[i][j] == -1) dist[i][j] = inf;}
        forn (i, Q) {cin >> qs[i].fi >> qs[i].se; -- qs[i].fi, --qs[i].se;}
        futures[test_case - 1] = async(launch::async, solve, N, dist, horses, qs);
    }

    for (int test_case = 1; test_case <= test_cases; test_case++) {
        vector<ld>  res = futures[test_case - 1].get();
        cout << "Case #" << test_case << ":" << fixed << setprecision(6);
        for (auto x: res) {
            if (x < 1e14)
                cout << " " << x;
            else
                cout << " IMPOSSIBLE";
        } cout << endl;
        cout.flush();
    }

    fclose(stdout);
    fclose(stdin);
    //cerr << chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now() - start).count() << endl;
    return 0;
}
