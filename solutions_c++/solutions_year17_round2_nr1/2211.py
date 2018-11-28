#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double ld;

int main() {
#define TASK "A-large"
    freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cs = 1; cs <= t; ++cs){
        int d, n;
        scanf("%d %d", &d, &n);
        ld maxTime = 0;
        for(int i = 0; i < n; ++i){
            int k, s;
            scanf("%d %d", &k, &s);
            maxTime = max(maxTime, (ld) (d - k) / (ld) s);
        }
        printf("Case #%d: %.7lf\n", cs, (ld) d / maxTime);
    }
    return 0;
}
