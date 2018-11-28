#include <cstdio>

const int maxN = 1024;
char t[maxN];

void prog() {
    int n = 0, k;
    scanf("%s%d", t, &k);
    while(t[n]) n++;

    int res = 0;
    for(int i = 0; i < n - k + 1; ++i) if(t[i] == '-') {
        res++;
        for(int j = 0; j < k; ++j) t[i + j] ^= '+' ^ '-';
    }

    bool ok = 1;
    for(int i = 0; i < n; ++i) ok &= t[i] == '+';

    if(ok) printf("%d\n", res);
    else printf("IMPOSSIBLE\n");
}

int main() {
    int x; scanf("%d", &x);
    for(int i = 1; i <= x; ++i) {
        printf("Case #%d: ", i);
        prog();
    }
}
