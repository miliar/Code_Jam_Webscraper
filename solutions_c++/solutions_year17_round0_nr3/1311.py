// jimjam
#include <cstdio>
using ll = long long;

int T;

ll N, K;
ll b, t;
ll freq[100005], freq2[100005];

void go() {
    b = t = N;
    for (int i = 0; i < 2; i++) freq[i] = freq2[i] = 0;
    freq[0] = 1;
    while (K) {
        for (int i = t-b; i >= 0; i--) {
            if (freq[i] >= K) {
                printf("%lld %lld\n", (b+i)/2, (b+i-1)/2);
                return;
            }
            K -= freq[i];
            freq2[(b+i-1)/2-(b-1)/2] += freq[i];
            freq2[(b+i)/2-(b-1)/2] += freq[i];
        }
        b = (b-1)/2;
        t /= 2;
        for (int i = 0; i <= t-b; i++) freq[i] = freq2[i], freq2[i] = 0;
    }
}

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%lld %lld", &N, &K);
        go();
        fprintf(stderr, "case %d\n", t);
    }
}

