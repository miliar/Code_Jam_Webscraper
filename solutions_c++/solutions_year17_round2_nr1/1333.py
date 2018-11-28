#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 1005;
int d, n, k[N], s[N], idx[N];

bool cmp(int a, int b) {
    if (k[a] != k[b]) return k[a] > k[b];
    return s[a] < s[b];
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%d", &d, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", k+i, s+i);
            idx[i] = i;
        }
        sort(idx, idx+n, cmp);
        double maxt = 0;
        for (int i = 0; i < n; ++i) {
            int x = idx[i];
            double t = 1.0 * (d - k[x]) / s[x];
            maxt = max(maxt, t);
        }
        printf("Case #%d: %.8f\n", cas, d / maxt);
    }
}
