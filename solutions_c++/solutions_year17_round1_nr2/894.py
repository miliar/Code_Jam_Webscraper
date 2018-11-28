#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

FILE *fout = fopen ("B.out", "w");
FILE *fin  = fopen ("B.in", "r");

int ans, n, p, rb[50][50], lb[50][50];
double r[50], q[50][50];
int t[50], tt[50];

int solve() {
    memset(t, 0, sizeof(t));
    memset(tt, 0, sizeof(tt));
    ans = 0;
    fscanf(fin, "%d %d\n", &n, &p);
    for (int i = 0; i < n; ++i)
        fscanf(fin, "%d", &r[i]);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j)
            fscanf(fin, "%d", &q[i][j]);
        sort(q[i], q[i]+p);
        for (int j = 0; j < p; ++j) {
            rb[i][j] = floor(q[i][j]/(r[i]*0.9));
            lb[i][j] = ceil(q[i][j]/(r[i]*1.1));
        }
    }
/*
    fprintf(fout, "\n%d %d\n", n, p);
    for (int i = 0; i < n; ++i)
        fprintf(fout, "%d ", r[i]);
    fprintf(fout, "\n");
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j)
            fprintf(fout, "%d ", q[i][j]);
        fprintf(fout, "\n");
    }
*/
    bool b;
    for (int z = 0; z < p; ++z) {
        if (lb[0][z] > rb[0][z]) continue;
        if (n == 1) {
            ans++;
            continue;
        }
        for (int c = lb[0][z]; c <= rb[0][z]; ++c) {
            for (int i = 1; i < n; ++i) {
                b = false;
                for (int j = t[i]; j < p; ++j)
                    if  (lb[i][j] <= c && c <= rb[i][j]) {
                        b = true;
                        tt[i] = j;
                        break;
                    }
                if (!b) break;
            }
            if (b) {
                ans++;
                for (int i = 1; i < n; ++i) {
                    t[i] = tt[i]+1;
                    if (t[i] == p) return ans;
                }
                break;
            }
        }
    }
    return ans;
}

int main() {
    int T;
    long long n, k;
    fscanf(fin, "%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        fprintf(fout, "Case #%d: %d\n", i, solve());
    }
    return 0;
}
