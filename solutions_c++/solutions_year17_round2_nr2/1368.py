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
typedef vector<int> vi;
typedef vector<vi> vvi;

typedef pair<int, int> pii;
typedef vector<pii> vpi;

template <class T> T inline sqr(T x) {
    return x * x;
}

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;

const int n = 6;


const string C = "RYBGVO";
void dfs(vvi& g, int v, vi& s) {
    forn (to, n)
        if (g[v][to]) {
            g[v][to]--;
            g[to][v]--;
            dfs(g, to, s);
        }
    s.pb(v);
}

string solve(vi a) {
    forn (st, n)
        forn (fin, st)
              if (a[st] && a[fin]) {
                  vi b(n);
                  forn (i, n)
                        if (i == st || i == fin)
                            b[i] = a[i] * 2 - 1;
                        else
                            b[i] = a[i] * 2;
                  forn (t, b[0] + 1) {
                      int x = b[0] - b[3] - t;
                      int y = b[1] - b[4] - t;
                      if (x >= 0 && y >= 0 && x + y + b[5] == b[2]) {
                          vvi g(n, vi(n, 0));
                          forn (i, 3)
                                g[i][i + 3] = g[i + 3][i] = b[i + 3];
                          g[0][1] = g[1][0] = t;
                          g[0][2] = g[2][0] = x;
                          g[1][2] = g[2][1] = y;
                          vi s; dfs(g, st, s);
                          bool ok = true;
                          forn (i, n) forn (j, n) if (g[i][j]) ok = false;
                          if (ok) {
                              string ans;
                              for (int x: s)
                                  ans += C[x];
                              return ans;
                          }
                      }
                  }
              }
    return "IMPOSSIBLE";
}

int main() {
    //auto start = chrono::system_clock::now();
    string name = "B-small";    string path = "";

    freopen((path + name + ".in").c_str(), "r", stdin);
    freopen((path + name + ".out").c_str(), "w", stdout);

    int test_cases;
    cin >> test_cases;
    vector<future<string>> futures(test_cases);

    for (int test_case = 1; test_case <= test_cases; test_case++) {
        vi a(6);
        cin >> a[0];
        cin >> a[0] >> a[5] >> a[1] >> a[3] >> a[2] >> a[4];
        futures[test_case - 1] = async(launch::async, solve, a);
    }

    for (int test_case = 1; test_case <= test_cases; test_case++) {
        string res = futures[test_case - 1].get();
        cout << "Case #" << test_case << ": " << res << endl;
        cout.flush();
    }

    fclose(stdout);
    fclose(stdin);
    //cerr << chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now() - start).count() << endl;
    return 0;
}
