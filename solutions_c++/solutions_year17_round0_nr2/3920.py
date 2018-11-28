#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int digits[20];

int main() {
    int T; scanf("%d", &T);
    for (int Cas = 1; Cas <= T; Cas++) {
        long long x; scanf("%lld", &x);
        int len = 0;
        while(x > 0) {
            digits[len++] = x % 10;
            x /= 10;
        }
        int i;
        for (i = len - 1; i > 0; i--) {
            if (digits[i] > digits[i-1]) {
                digits[i]--;
                break;
            }
        }
        for (int j = i + 1; j < len; j++) {
            if (digits[j] > digits[j-1]) {
                digits[j]--;
                digits[j-1] = 9;
            }
        }
        for (i = i - 1; i >= 0; i--) {
            digits[i] = 9;
        }
        printf("Case #%d: ", Cas);
        bool flag = false;
        for (int i = len - 1; i >= 0; i--) {
            if (digits[i] > 0) flag = true;
            if(flag) printf("%d", digits[i]);
        }
        puts("");
    }
}
