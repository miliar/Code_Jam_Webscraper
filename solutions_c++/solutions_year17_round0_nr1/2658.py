#include <cstdio>
#include <cstring>

int n, k;
char a[1024];

void read() {
    scanf("%s%d", a, &k);
    n = strlen(a);
}

void solve() {
    int ans = 0;
    int i;
    for (i = 0; i < n - k + 1; i++) {
        if (a[i] == '-') {
            ans ++;

            for (int j = 0; j < k; j++) {
                char &c = a[i + j];
                if (c == '+') c = '-';
                else c = '+';
            }
        }
    }
    for (; i < n; i++) {
        if (a[i] == '-') {
            printf ("IMPOSSIBLE\n");
            return;
        }
    }
    printf ("%d\n", ans);
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

