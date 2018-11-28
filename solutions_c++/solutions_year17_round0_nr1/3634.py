#include <cstdio>
#include <cstring>

char s[1024];

void solve() {
    int n, k;
    scanf("%s%d", s, &k);
    n = strlen(s);
    int ops = 0;
    for(int i = 0; i < n - k + 1; ++i) 
    if (s[i] == '-'){
        ++ops;
        for(int j = 0; j < k; ++j)
            s[i + j] = (s[i + j] == '+' ? '-' : '+');
    }
    for(int i = 0; i < n; ++i)
        if (s[i] == '-') {
            printf("IMPOSSIBLE\n");
            return;
        }
    printf("%d\n", ops);
}

int main() {
    int ntests;
    scanf("%d", &ntests);
    for(int tc = 1; tc <= ntests; ++tc) {
        printf("Case #%d: ", tc);
        solve();
    }
    return 0;
}