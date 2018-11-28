/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

const int max_n = 100 + 10;

int t;
int n, q;
LL e[max_n], s[max_n], d[max_n][max_n];
double dis[max_n];
bool in[max_n];

double get_dis(int u, int v) {
    queue<int> q;
    q.push(u);
    for (int i = 0; i < n; ++i) {
        dis[i] = 1e64;
    }
    memset(in, 0, sizeof(in));
    in[u] = true;
    dis[u] = 0;
    while (!q.empty()) {
        int k = q.front();
        q.pop();
        in[k] = false;
        for (int i = 0; i < n; ++i) {
            if (i == k) continue;
            if (d[k][i] != -1LL && d[k][i] <= e[k]) {
                double nd = dis[k] + (double)d[k][i] / s[k];
                if (nd < dis[i]) {
                    dis[i] = nd;
                    if (!in[i]) {
                        q.push(i);
                        in[i] = true;
                    }
                }
            }
        }
    }
    return dis[v];
}

void solve() {
    scanf("%d%d", &n, &q);
    for (int i = 0; i < n; ++i) {
        cin >> e[i] >> s[i];
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> d[i][j];
        }
    }
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (d[i][k] != -1LL && d[k][j] != -1LL) {
                    if (d[i][j] == -1LL || d[i][k] + d[k][j] < d[i][j]) {
                        d[i][j] = d[i][k] + d[k][j];
                    }
                }
            }
        }
    }
    printf("Case #%d:", ++t);
    for (int i = 0; i < q; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        --u;
        --v;
        printf(" %.10f", get_dis(u, v));
    }
    puts("");
}

int main() {
    freopen("C.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
