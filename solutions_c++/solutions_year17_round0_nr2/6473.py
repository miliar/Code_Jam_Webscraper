
#include <cstdio>

int n, d[20];
long long a;

int main() {
    scanf("%d", &n);
    for (int x = 1; x <= n; x++) {
        scanf("%lld", &a);
        int c = 0;
        while (a != 0) {
            d[c++] = a % 10;
            a /= 10;
        }
        for (int i = 0; i < c - 1; i++) {
            if (d[i] < d[i + 1]) {
                d[i + 1]--;
                for (int j = i; j >= 0; j--) {
                    d[j] = 9;
                }
            }
        }
        for (int i = c - 1; i >= 0; i--) {
            a = 10 * a + d[i];
        }
        printf("Case #%d: %lld\n", x, a);
    }
}
