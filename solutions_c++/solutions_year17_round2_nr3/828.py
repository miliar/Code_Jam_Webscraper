#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <climits>
#include <cfloat>
//#include <functional>

using namespace std;
#define MP make_pair
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define REP (i, s, t) for (int i = (s); i < (t); i++)

LL d[105]; // d[i] is distance i and i+1
LL s[105];
LL e[105];

LL dist[105][105];

double pp[105][105];

int n;
double solve() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            pp[i][j] = DBL_MAX/100;
            dist[i][j] = -1;
        }
    }
    for (int i = 0; i < n-1; i++) {
        dist[i][i+1] = d[i];
        for (int j = i+1; j < n-1; j++) {
            dist[i][j+1] = dist[i][j] + d[j];
        }
    }
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            if (e[i] >= dist[i][j]) {
                pp[i][j] = double(dist[i][j])/double(s[i]);
                if (pp[i][j] < 0) {
                    //printf("dist[%d][%d] = %d, s[i] = %d, pp[i][j] = %.0f\n", i,j,dist[i][j],s[i],pp[i][j]);
                }
            }
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            if (i >= k) continue;
            for (int j = i+1; j < n; j++) {
                if (i >= k || k >= j) {
                    continue;
                }
                if (pp[i][j] > pp[i][k] + pp[k][j]) {
                    pp[i][j] = pp[i][k] + pp[k][j];
                    //pp[i][j] = min(pp[i][j], tt);
                }
            }
        }
    }

    return pp[0][n-1];
}
int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        int q;
        scanf("%d%d", &n, &q);
        for (int j = 0; j < n; j++) {
            scanf("%lld%lld", e+j, s+j);
        }
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                int tmp;
                scanf("%d", &tmp);
                if (k == j+1) {
                    d[j] = tmp;
                }
            }
        }
        for (int j = 0; j < q; j++) {
            int a, b;
            scanf("%d%d", &a, &b);
            printf("%.6f ", solve());
        }
        printf("\n");
    }
}
