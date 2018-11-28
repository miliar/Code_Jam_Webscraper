#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>
#include <ctime>
#include <limits>
#include <tuple>
#include <complex>
#include <numeric>
#include <future>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = acos(-1.0);

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}

template<typename T>
bool chmin(T &x, T y) {
    if (x > y) {
        x = y;
        return true;
    }
    return false;
}

template<typename T>
bool chmax(T &x, T y) {
    if (x < y) {
        x = y;
        return true;
    }
    return false;
}

template<typename U, typename V>
ostream &operator<<(ostream &s, const pair<U, V> &x) {
    s << "(" << x.fst << ", " << x.snd << ")";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const vector<U> &x) {
    s << "[";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "]";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const set<U> &x) {
    s << "{";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "}";
    return s;
}

template<int sz>
ostream operator<<(ostream &s, const bitset<sz> &x) {
    for (int i = 0; i < sz; i++) {
        s << x[i];
    }
    return s;
}


//--------------------------------------------------------------------------


const int maxn = 305;
int mt[maxn];
int used[maxn];
int cu = 1;
vector<int> g[maxn];

bool dfs(int v) {
    for (int to : g[v]) {
        if (mt[to] == -1) {
            mt[to] = v;
            return true;
        }
    }
    used[v] = cu;
    for (int to : g[v]) {
        if (used[mt[to]] != cu && dfs(mt[to])) {
            mt[to] = v;
            return true;
        }
    }
    return false;
}

int main(int argc, char* argv[]) {

    srand(time(NULL));

#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("sum.in", "r", stdin);
    //freopen("sum.out", "w", stdout);
#endif

    int t;
    cin >> t;
    int tt = 0;
    while (t--) {
        tt++;
        cout << "Case #" << tt << ": ";

        int n, k;
        cin >> n >> k;
        cin.ignore();

        vector<vector<int>> a(n, vector<int>(n)), b(n, vector<int>(n));
        set<int> columns, rows, diag1, diag2;
        for (int i = 0; i < k; i++) {
            char type;
            int x, y;
            cin >> type >> x >> y;

            x--, y--;
            cin.ignore();

            if (type == 'o' || type == '+') {
                diag1.insert(x + y);
                diag2.insert(x + n - y);
                a[x][y] = 1;
            }

            if (type == 'o' || type == 'x') {
                rows.insert(x);
                columns.insert(y);
                b[x][y] = 1;
            }
        }

        set<pair<int,int>> modified;

        for (int i = 0; i < n; i++) {
            g[i].clear();
            mt[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!rows.count(i) && !columns.count(j)) {
                    g[i].pb(j);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            cu++;
            dfs(i);
        }

        for (int i = 0; i < n; i++) {
            if (mt[i] != -1) {
                b[mt[i]][i] = 1;
                modified.insert(mp(mt[i], i));
            }
        }

        for (int i = 0; i < maxn; i++) {
            mt[i] = -1;
            g[i].clear();
        }

        map<pair<int,int>, pair<int,int>> mm;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int x = i + j, y = i + n - j;
                if (!diag1.count(i + j) && !diag2.count(i + n - j)) {
                    g[x].pb(y);
                    mm[mp(x, y)] = mp(i, j);
                }
            }
        }

        for (int i = 0; i < maxn; i++) {
            cu++;
            dfs(i);
        }

        for (int i = 0; i < maxn; i++) {
            if (mt[i] != -1) {
                int x = mm[mp(mt[i], i)].fst;
                int y = mm[mp(mt[i], i)].snd;
                a[x][y] = 1;
                modified.insert(mp(x, y));
            }
        }

        int sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sum += a[i][j] + b[i][j];
            }
        }

        cout << sum << " " << modified.size() << endl;
        for (auto p : modified) {
            if (a[p.fst][p.snd] && b[p.fst][p.snd]) {
                cout << "o ";
            } else if (a[p.fst][p.snd]) {
                cout << "+ ";
            } else {
                cout << "x ";
            }
            cout << p.fst + 1 << " " << p.snd + 1 << endl;
        }



    }

    return 0;
}
