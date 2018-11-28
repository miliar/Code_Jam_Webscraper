#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int maxn = 1000 + 5;

int n, d, k[maxn], s[maxn];

int main() {
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        scanf("%d %d", &d, &n);
        double maximum_time = 0.0;
        for (int i = 0; i < n; i++) {
            scanf("%d %d", &k[i], &s[i]);
            maximum_time = max(maximum_time, double(d - k[i]) / double(s[i]));
        }
        double sol = double(d) / maximum_time;
        printf("Case #%d: %.6lf\n", t, sol);
    }
    return 0;
}
