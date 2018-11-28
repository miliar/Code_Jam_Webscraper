#include <bits/stdc++.h>

#define FOR(i, p, n) for(int i = (int)(p); i < (int)(n); ++i)
#define FORD(i, p, n) for(int i = (int)(p); i >= (int)(n); --i)
#define UMAP unordered_map

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;

const int N = 1e3 + 5;

char buf[N];

UMAP <char, char> mapper = { { '+', '-' }, { '-', '+' } };

bool solve() {
    int k;
    scanf("%s %d", buf, &k);
    int len = strlen(buf);
    int last = len;
    FOR(i, 0, len) if (buf[i] == '-') {
        last = i;
        break;
    }
    if (last == len) {
        printf("0\n");
        return 0;
    }
    int res = 0;
    while (true) {
        if (len - last < k) {
            printf("IMPOSSIBLE\n");
            return 0;
        }
        FOR(i, 0, k) buf[i + last] = mapper[buf[i + last]];
        ++res;
        last = len;
        FOR(i, 0, len) if (buf[i] == '-') {
            last = i;
            break;
        }
        if (last == len) {
            printf("%d\n", res);
            return 0;
        }
    }

    return 0;
}

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    int t;
    cin >> t;
    FOR(i, 1, t + 1) {
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
