// jimjam
#include <cstdio>
using ll = long long;

int T, a[20], l;
ll N;

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lld", &N);
        l = 0;
        for (; N; N /= 10) a[l++] = N%10;

        for (int i = 0; i+1 < l; i++) if (a[i] < a[i+1]) a[i] = 9, a[i+1]--;
        if (!a[l-1]) l--;
        printf("Case #%d: ", t);
        for (int i = l-1; i >= 0; i--) {
            if (i+1 < l && a[i] < a[i+1]) a[i] = a[i+1];
            printf("%d", a[i]);
        }
        printf("\n");
    }
}



