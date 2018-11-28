#include <iostream>
using namespace std;
void output(int digits[20], int len) {
    for (int i = len - 1; i >= 0; --i) {
        printf("%d", digits[i]);
    }
    printf("\n");
}
int main() {
    int T;
    long long n;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%lld", &n);
        int digits[20], len = 0;
        while (n) {
            digits[len++] = n % 10;
            n /= 10;
        }
        printf("Case #%d: ", ca);
        if (len <= 1) {
            output(digits, len);
            continue;
        }
        int i = len - 2;
        for (; i >= 0; --i) {
            if (digits[i + 1] > digits[i]) {
                break;
            }
        }
        if (i == -1) {
            output(digits, len);
            continue;
        }
        i++;
        while (i + 1 < len && digits[i] == digits[i + 1]) i++;
        for (int j = len - 1; j > i; --j) {
            printf("%d", digits[j]);
        }
        if (digits[i] > 1) printf("%d", digits[i] - 1);
        for (int j = i - 1; j >= 0; --j) {
            printf("9");
        }
        printf("\n");

    }
    return 0;
}
