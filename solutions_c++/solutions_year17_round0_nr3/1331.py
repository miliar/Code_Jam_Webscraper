#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

void Split(long long a[][2], int &num) {
    long long b[2][2];
    memset(b, 0, sizeof(b));

    if (a[0][0] % (long long)2 == 1) {
        b[0][0] = a[0][0] / (long long)2;
        b[0][1] = a[0][1] + a[0][1];
        if (num == 2) {
            b[0][1] += a[1][1];
            b[1][1] = a[1][1];
            b[1][0] = b[0][0] + (long long)1;
        }
    } else {
        b[0][0] = a[0][0] / (long long)2 - (long long)1;
        b[0][1] = a[0][1];
        b[1][0] = a[0][0] / (long long)2;
        b[1][1] = a[0][1];
        if (num == 2) {
            b[1][1] += a[1][1] + a[1][1];
        }
        num = 2;
    }

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) {
            a[i][j] = b[i][j];
        }
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        long long n, k, y, z;
        scanf("%lld%lld", &n, &k);
        long long a[2][2];
        int num = 1;
        a[0][0] = n;
        a[0][1] = 1;
        long long p = 1;
        while (true) {
            if (p < k) {
                k -= p;
                Split(a, num);
            } else {
                if (num == 2 && a[1][1] >= k) {
                    y = a[1][0] / (long long)2;
                    z = y - (((a[1][0] % (long long)2) == 1) ? 0 : 1);
                } else {
                    y = a[0][0] / (long long)2;
                    z = y - (((a[0][0] % (long long)2) == 1) ? 0 : 1);
                }
                break;
            }
            p = p + p;
        }
        printf("Case #%d: %lld %lld\n", t, y, z);
    }
    return 0;
}
