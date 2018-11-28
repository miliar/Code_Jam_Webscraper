#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>
#define pb push_back
using namespace std;

const int MAXN = 55;
const int MAX_P = 55;
const double EPS = 1e-8;

int r[MAXN];
vector <int> q[MAXN];
vector <int> v;
int next[MAXN];

int solve(int n, int p) {
    int res = 0;

    for (int i = 0; i < n; i++) {
        next[i] = 0;
    }

    while(1) {
        int done = 0;
        for (int i = 0; i < n; i++) {
            //printf("i = %d, next = %d, p = %d\n", i, next[i], p);
            if (next[i] >= p) {
                done = 1;
                break;
            }
        }

        if (done) {
            break;
        }

        double maxi = 1e20;
        double mini = 0;
        for (int i = 0; i < n; i++) {
            //printf("here\n");
            int a = q[i][next[i]];

            //printf("aux = %f\n", a / (0.9 * r[i]));
            maxi = min(maxi, a / (0.9 * r[i]));
            mini = max(mini, a / (1.1 * r[i]));
        }
        maxi = floor(maxi);
        mini = ceil(mini);
        //printf("maxi = %f, mini = %f\n", maxi, mini);
        if (maxi + EPS >= mini) {
            res++;
            for (int i = 0; i < n; i++) {
                next[i]++;
            }
        } else {
            double low = 1e38;
            double big = 0;
            int idx = -1;
            int id2 = -1;
            for (int i = 0; i < n; i++) {
                int a = q[i][next[i]];
                double aux = floor(a / (0.9 * r[i]));
                double aux2 = a / (1.1 * r[i]);
                if (aux < low + EPS) {
                    low = aux;
                    idx = i;
                }
                if (aux2 > big - EPS) {
                    big = aux;
                    id2 = i;
                }
            }
            next[idx]++;
        }
    }
    return res;
}

int main(void) {
    int t;
    int n, p;
    int x;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        scanf(" %d %d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf(" %d", &r[i]);
        }

        for (int i = 0; i < n; i++) {
            q[i].clear();
            for (int j = 0; j < p; j++) {
                scanf(" %d", &x);
                q[i].pb(x);
            }
            sort(q[i].begin(), q[i].end());
        }

        int res = solve(n, p);

        printf("Case #%d: %d\n", caso, res);
    }
    return 0;
}


