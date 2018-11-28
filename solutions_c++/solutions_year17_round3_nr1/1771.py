#include <cstdio>
#include <fstream>
#include <iostream>
#include <algorithm>
#define M_PI 3.141592653589793238
using namespace std;

FILE *fin  = fopen ("A.in", "r");
FILE *fout = fopen ("A.out", "w");
pair<int, int> p[1001];
long long a[1001];

void solve() {
    int n, k;
    fscanf(fin, "%d%d", &n, &k);
    for (int i = 0; i < n; i++)
        fscanf(fin, "%d%d", &p[i].first, &p[i].second);
    sort(p, p+n);
    long long ans = 0, s;
    int t = 0;
    for (int i = k-1; i < n; i++) {
        while (i+1 < n && p[i+1].first == p[i].first)
            i++;
        s = 1ll * p[i].first * p[i].first;
        s += 1ll * 2 * p[i].first * p[i].second;
        for (; t < i; t++)
            a[t] = 1ll * 2 * p[t].first * p[t].second;
        sort(a, a+t);
        for (int j = 1; j < k; j++)
            s += a[t-j];
        ans = max(ans, s);
    }
    fprintf(fout, "%I64f\n", ans*M_PI);
}

int main() {
    int T;
    fscanf(fin, "%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        fprintf(fout, "Case #%d: ", i);
        solve();
    }
    return 0;
}
