#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000000;
// double EPS = 1e-12;
const int MOD = 1000000007;

struct Package {
    int l, h;
    int data;
}packages[101][101];
int recipe[1001];
int run[105];

bool cmp(struct Package a, struct Package b) {
    if (a.l == b.l) return a.h < b.h;
    return a.l < b.l;
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    int n, p;
    scanf("%d", &t);
    for (int tt=0 ; tt<t ; tt++) {
        scanf("%d %d", &n, &p);
        for (int i=0 ; i<n ; i++) {
            scanf("%d", &recipe[i]);
        }
        int tmp;
        for (int i=0 ; i<n ; i++) {
            for (int j=0 ; j<p ; j++) {
                scanf("%d", &tmp);
                int lower_b = (int)ceil(1.0 * tmp / recipe[i] / 1.1);
                double upper_bu = (1.0 * tmp / recipe[i] / 0.9) + 1e-12;
                int upper_b = (int)upper_bu;
//                printf("L U: %d %d\n", lower_b, upper_b);
//                printf("L U: %lf %lf %d %d\n", 1.0 * tmp / recipe[i] / 1.1, upper_bu, tmp, recipe[i]);
                packages[i][j].data = tmp;
                if (lower_b > upper_b) {
                    packages[i][j].l = 2*INF;
                    packages[i][j].h = INF;
                }
                else {
                    packages[i][j].l = lower_b;
                    packages[i][j].h = upper_b;
                }
            }
        }
        for (int i=0 ; i<n ; i++) {
            sort(packages[i], packages[i]+p, cmp);
        }

        int ans = 0;
        for (int i=0 ; i<=n ; i++) run[i] = 0;

        while (1) {
            int accept_l=packages[0][run[0]].l, accept_h=packages[0][run[0]].h;
//            printf("first: %d %d %d\n", run[0], accept_l, accept_h);
            if (accept_l > accept_h) {
                run[0]++;
                if (run[0] >= p) break;
            }
            int min_rec = 0;
            for (int i=1 ; i<n ; i++) {
                int j = run[i];
                accept_l = max(accept_l, packages[i][j].l);
                accept_h = min(accept_h, packages[i][j].h);
                if (packages[i][j].l < packages[min_rec][run[min_rec]].l) {
                    min_rec = i;
                }
                else if (packages[i][j].l == packages[min_rec][run[min_rec]].l &&
                         packages[i][j].h < packages[min_rec][run[min_rec]].h) {
                    min_rec = i;
                }
            }
//            printf("second: %d %d %d\n", run[0], accept_l, accept_h);
            if (accept_l <= accept_h) {
//                printf("Sol: ");
                for (int i=0 ; i<n ; i++) {
//                    printf("%d ", run[i]);
                    run[i]++;
                }
//                printf("\n");
//                printf("Sol path: ");
//                for (int i=0 ; i<n ; i++) {
//                    printf("%d ", packages[i][run[i]-1].data);
//                }
//                printf("\n");
                ans++;
            }
            else {
                run[min_rec]++;
            }

            if (run[min_rec] >= p) break;
        }

        printf("Case #%d: %d\n", tt+1, ans);
    }
}
