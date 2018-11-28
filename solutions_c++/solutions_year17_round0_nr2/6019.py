#include <bits/stdc++.h>

#define FOR(i, p, n) for(int i = (int)(p); i < (int)(n); ++i)
#define FORD(i, p, n) for(int i = (int)(p); i >= (int)(n); --i)
#define UMAP unordered_map

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;

const int N = 1e2 + 5;

char str[N];

int to_dig(char c) {
    return (c - '0');
}

char to_sym(int i) {
    return (i + '0');
}

bool solve() {
    scanf("%s", str);
    int len = strlen(str);
    FOR(i, 1, len) if (to_dig(str[i]) < to_dig(str[i - 1])) {
        int p = i - 1;
        while (p && str[p - 1] == str[i - 1]) --p;
        if (p == 0 && str[p] == '1') {
            str[--len] = 0;
            FOR(j, 0, len) str[j] = '9';
            break;
        } else {
            --str[p];
            FOR(j, p + 1, len) str[j] = '9';
        }
    }
    printf("%s\n", str);

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
