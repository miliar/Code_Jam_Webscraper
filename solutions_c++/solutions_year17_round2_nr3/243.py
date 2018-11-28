#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#ifdef __linux__
    #define I64d "%lld"
#else
    #define I64d "%I64d"
#endif

typedef long long int int64;

const int maxn = 100;
const int maxq = 100;

int n, q;
int64 e[maxn], s[maxn];
int64 d[maxn][maxn];
int qu[maxn], qv[maxn];

void floyd() {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            if (d[i][k] == -1)
                continue;
            for (int j = 0; j < n; j++) {
                if (d[k][j] == -1)
                    continue;
                if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                }
            }
        }
    }
}


const double inf = 1e100;

double t[maxn];
bool cool[maxn];

double path(int start, int finish) {
    //cerr << "path " << start << " " << finish << "\n";
    //cerr << n << "\n";
    for (int i = 0; i < n; i++) {
        t[i] = inf;
        cool[i] = false;
    }
    t[start] = 0.0;
    for (int i = 0; i < n; i++) {
        int min_id = -1;
        for (int j = 0; j < n; j++) {
            if (cool[j] || t[j] == inf)
                continue;
            if (min_id == -1 || t[j] < t[min_id]) {
                min_id = j;
            }
        }
        if (min_id == -1)
            break;
        cool[min_id] = true;
        //cerr << "t[" << min_id << "] = " << t[min_id] << "\n";
        for (int j = 0; j < n; j++) {
            if (cool[j] || d[min_id][j] == -1 || d[min_id][j] > e[min_id])
                continue;
            //cerr << min_id << " -> " << j << " :" << d[min_id][j] * 1.0 / s[min_id] << "\n";
            double tn = t[min_id] + d[min_id][j] * 1.0 / s[min_id];
            if (t[j] > tn) {
                t[j] = tn;
            }
        }
    }
    return t[finish];
};


int main() {
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        scanf("%d %d", &n, &q);
        for (int i = 0; i < n; i++) {
            scanf("%lld %lld", &e[i], &s[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%lld", &d[i][j]);
            }
        }
        floyd();
        /*
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cerr << d[i][j] << " ";
            }
            cerr << "\n";
        }*/
        printf("Case #%d: ", test + 1);
        for (int i = 0; i < q; i++) {
            scanf("%d %d", &qu[i], &qv[i]);
            qu[i]--; qv[i]--;
            printf("%.15lf%c", path(qu[i], qv[i]), " \n"[i == q - 1]);
        }
    }

    return 0;
}
