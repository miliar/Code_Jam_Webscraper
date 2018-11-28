#include <cstdio>
#include <cstring>

int n;
char a[32];

void read() {
    scanf("%s", a);
    n = strlen(a);
}

void solve() {

    while (1) {
        int ok = 1;

        for (int i = 1; i < n; i++) {
            if (a[i] < a[i - 1]) {
                ok = 0;
                -- a[i - 1];
                for (int j = i; j < n; j++) {
                    a[j] = '9';
                }
                break;
            }
        }
        if (a[0] == '0') {
            for (int i = 1; i < n; i++) {
                printf ("9");
            }
            printf("\n");
            return ;
        }

        if (ok) {
            printf ("%s\n", a);
            break;
        }
    }
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

