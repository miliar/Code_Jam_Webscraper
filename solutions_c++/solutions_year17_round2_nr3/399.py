#pragma comment (linker, "/STACK:128000000")
#include <iostream>
#include <cstdio>
#include <fstream>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <ctime>
#include <sstream>
#include <stack>
#include <cassert>
#include <list>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
    string s = FILENAME;
#ifdef YA
    //assert(!s.empty());
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //cerr<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock();
#else
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout);
    cin.tie(0);
#endif
    cout.sync_with_stdio(0);
    cout.precision(10);
    cout << fixed;
    int t = 1;
    
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        //++timer;
        cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}

#define int li

const int INF = 2000000000000LL;

void solve() {
    int n, q;
    cin >> n >> q;
    vector <int> e(n);
    vector <ld> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> e[i] >> s[i];
    }
    
    vector <vector <int> > g(n, vector <int> (n));
    for (int i =0; i < n; ++i) {
        for (int j = 0;j < n; ++j) {
            cin >> g[i][j];
        }
    }
    
    vector <vector <int> > dists;
    dists = g;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == j) {
                dists[i][j] = 0;
            }
            if (dists[i][j] == -1) {
                dists[i][j] = INF;
            }
        }
    }
    
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dists[i][k] < INF && dists[k][j] < INF) {
                    dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j]);
                }
            }
        }
    }
    
    vector <vector <ld> > dists2 = vector <vector <ld> > (n, vector <ld> (n, ld(INF)));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == j) {
                dists2[i][j] = 0;
            }
            if (dists[i][j] <= e[i]) {
                dists2[i][j] = min(dists2[i][j], dists[i][j] / s[i]);
            }
        }
    }
    
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dists2[i][k] < INF && dists2[k][j] < INF) {
                    dists2[i][j] = min(dists2[i][j], dists2[i][k] + dists2[k][j]);
                }
            }
        }
    }
    
    
    cerr << q << endl;
    for (int i = 0; i < q; ++i) {
        int start, end;
        cin >> start >> end;
        --start;
        --end;
        cout << dists2[start][end] << " ";
    }
    cout << "\n";
}
