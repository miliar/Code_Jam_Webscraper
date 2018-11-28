#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define debug printf
typedef long long ll;

void solve(int t) {
    char pc[1001];
    int k;
    scanf(" %s %d", pc, &k);
    int n = strlen(pc);
    int flips = 0;
    for (int i = 0; i < n; i++) {
        if (pc[i] != '+') {
            if (i > n - k) {
                printf("Case #%d: IMPOSSIBLE\n", t);
                return;
            }
            flips += 1;
            for (int j = 0; j < k; j++) {
                pc[i+j] = pc[i+j] == '-' ? '+' : '-';
            }
        }
    }
    printf("Case #%d: %d\n", t, flips);
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve(t);
    return 0;
}
