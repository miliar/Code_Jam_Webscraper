#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <random>
#include <bitset>
#include <cassert>
#include <tuple>
#include <list>
#include <iterator>
#include <unordered_set>
#include <unordered_map>
#include <numeric>

using namespace std;

typedef long long ll;
typedef long double ld;

template<class htpe, class cmp>
using heap = priority_queue<htpe, vector<htpe>, cmp>;

template<class htpe>
using min_heap = heap<htpe, greater<htpe> >;

template<class htpe>
using max_heap = heap<htpe, less<htpe> >;

#define mp make_pair
#define pb push_back
#define mt make_tuple
#define ff first
#define ss second

#define forn(i, n) for (int i = 0; i < ((int)(n)); ++i)
#define forrn(i, s, n) for (int i = (int)(s); i < ((int)(n)); ++i)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define PYMOD(a, m) ((((a) % (m)) + (m)) % (m))

const int INF = 1791791791;
const ll INFLL = 1791791791791791791ll;

void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> s(n), e(n);
    forn(i, n)
        cin >> e[i] >> s[i];
    vector<vector<int> > d(n, vector<int>(n, 0));
    forn(i, n) {
        forn(j, n) {
            cin >> d[i][j];
        }
    }
    vector<vector<ll> > dist(n, vector<ll>(n, INFLL));
    forn(i, n) {
        forn(j, n) {
            if (d[i][j] != -1)
                dist[i][j] = d[i][j];
        }
    }
    forn(k, n) {
        forn(i, n) {
            forn(j, n) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    vector<vector<ld> > sdist(n, vector<ld>(n, INFLL));
    forn(i, n) {
        forn(j, n) {
            if (dist[i][j] <= e[i]) {
                sdist[i][j] = min(sdist[i][j], (ld)dist[i][j] / (ld)s[i]);
            }
        }
    }
    forn(k, n) {
        forn(i, n) {
            forn(j, n) {
                sdist[i][j] = min(sdist[i][j], sdist[i][k] + sdist[k][j]);
            }
        }
    }
    forn(i, q) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        cout << " " << sdist[u][v];
    }
    cout << endl;
}

int main() {
    // Code here:
   
    int t;
    cin >> t;
    cout.precision(20);
    forn(i, t) {
        cout << "Case #" << i + 1 << ":";
        solve();
    }

    return 0;
}

