#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#include <cassert>
#include <unordered_map>
#include <fstream>
#include <random>
#include <cstring>
#include <complex>
#include <bitset>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
mt19937 rr(random_device{}());

const ll INF = 1e15;

int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int tests;
    cin >> tests;
    cout.precision(12);
    cout << fixed;

    vector<char> col = {'R', 'O', 'Y', 'G', 'B', 'V'};

    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        int n, q;
        cin >> n >> q;
        vector<int> e(n), s(n);
        for (int i = 0; i < n; ++i)
            cin >> e[i] >> s[i];

        vector<vector<ll>> g(n, vector<ll>(n));
        for (int i = 0; i < n; ++i) {   
            for (int j = 0; j < n; ++j) {
                cin >> g[i][j];
                if (g[i][j] == -1)
                    g[i][j] = INF;
            }
        }

        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
                }
            }
        }

        vector<vector<double>> d(n, vector<double>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (g[i][j] > e[i]) {
                    d[i][j] = INF;
                } else {
                    d[i][j] = (double)g[i][j] / (double)s[i];
                }
            }
        }

        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }


        for (int i = 0; i < q; ++i) {
            int x, y;
            cin >> x >> y;
            --x; --y;
            cout << d[x][y] << " ";
        }
        cout << "\n";
    }
}