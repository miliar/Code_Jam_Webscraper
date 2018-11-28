#include "bits/stdc++.h"
#define puba push_back
#define ff first
#define ss second
#define bend(_x) begin(_x), end(_x)
#define szof(_x) ((int) (_x).size())
#define cmpby(_x) [](const auto& a, const auto& b) {return (a _x) < (b _x);}
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9 + 7;
const double PI = atan2(0, -1);
const int MAXN = 105;

char field[MAXN][MAXN];

int solve() {
    int n, m;
    scanf("%d%d", &n, &m);

    vector<int> rows;
    for (int i = 0; i < n; ++i) {
        scanf("%s", field[i]);
        bool flag = false;
        for (int j = 0; j < m; ++j) {
            if (field[i][j] != '?') {
                flag = true;
            }
        }
        if (flag) {
            rows.puba(i);
        }
    }
        
    rows.puba(n);
    for (int i = 0; i < szof(rows) - 1; ++i) {
        int x = rows[i];
        for (int j = 0; j < m; ++j) {
            if (field[x][j] != '?') {
                for (int k = 0; k < j; ++k) {
                    field[x][k] = field[x][j];
                }
                int prev = j;
                for (int k = j + 1; k <= m; ++k) {
                    if (k == m || field[x][k] != '?') {
                        for (int k2 = prev; k2 < k; ++k2) {
                            field[x][k2] = field[x][prev];
                        }
                        prev = k;
                    }
                }
                break;
            }
        }
        for (int j = i > 0 ? rows[i] + 1 : 0; j < rows[i + 1]; ++j) {
            for (int k = 0; k < m; ++k) {
                field[j][k] = field[x][k];
            }
        }
        /*
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                cerr << field[j][k];
            }
            cerr << endl;
        }
        cerr << endl;
        */
    }
    
    cout << "\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << field[i][j];
        }
        cout << "\n";
    }


    return 0;
}

int main() {
    //freopen(TASK_NAME ".in", "r", stdin);
    //freopen(TASK_NAME ".out", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    #ifdef LOCAL
        cerr << "time: " << clock() << endl;
    #endif
    return 0;
}