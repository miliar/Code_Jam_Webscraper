#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

ifstream input("/Users/dwang/Downloads/C-small-attempt0.in");

//int N, R, O, Y, G, B, V;
int N, Q;
vector<double> e;
vector<double> s;
vector<int> u;
vector<int> v;
double a[110][110];

void init() {
    input >> N >> Q;
    e.clear();
    s.clear();
    u.clear();
    v.clear();
    memset(a, 0, sizeof(a));
    for (int i = 0; i < N; ++i) {
        double ee, ss;
        input >> ee >> ss;
        e.push_back(ee);
        s.push_back(ss);
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            input >> a[i][j];
        }
    }
    for (int i = 0; i < Q; ++i) {
        int uu, vv;
        input >> uu >> vv;
        uu--;
        vv--;
        u.push_back(uu);
        v.push_back(vv);
    }
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            for (int t = 0; t < N; ++t) {
                if (a[i][t] > 0 && a[t][j] > 0) {
                    if (a[i][j] == -1) {
                        a[i][j] = a[i][t] + a[t][j];
                    } else if (a[i][j] > a[i][t] + a[t][j]) {
                        a[i][j] = a[i][t] + a[t][j];
                    }
                }
            }
        }
    }
    //input >> N >> R >> O >> Y >> G >> B >> V;
}

double g[110];
int checked[110];
double solve(int u, int v) {
    memset(g, 0, sizeof(g));
    memset(checked, 0, sizeof(checked));
    int c = u;
    while (c != v) {
        checked[c] = 1;
        for (int i = 0; i < N; ++i)
            if (a[c][i] > 0 && a[c][i] <= e[c]) {
                if (g[i] == 0 || g[i] > a[c][i] / s[c] + g[c]) {
                    g[i] = a[c][i] / s[c] + g[c];
                }
            }
        
        for (int i = 0; i < N; ++i)
            if (checked[i] == 0 && g[i] > 0) {
                if (checked[c] == 1 || g[c] > g[i]) {
                    c = i;
                }
            }
    }
    return g[v];
}

int main() {
    freopen("/Users/dwang/Documents/test/test/out2.txt", "w", stdout);
    int T;
    
    input >> T;
    for (int i = 0; i < T; ++i) {
        init();
        printf("Case #%d:", i + 1);
        for (int j =0; j < Q; ++j) {
            printf(" %.8f", solve(u[j], v[j]));
        }
        printf("\n");
    }
    input.close();
    return 0;
}
