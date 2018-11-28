#include<cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for(int ca=1; ca<=T; ca++) {
        long long n, k;
        scanf("%lld%lld", &n, &k);
       long long leaf[2] = {n, n}, leafcnt[2] = {1, 0};
        while(leafcnt[0] + leafcnt[1] < k) {
            long long cnt[2] = {0};
            for(int i=0; i<2; i++) {
                if(leaf[i] & 1) {
                    cnt[i] += leafcnt[i] * 2;
                }else {
                    cnt[0] += leafcnt[i];
                    cnt[1] += leafcnt[i];
                }
            }
            if(leaf[0]&1 && leaf[1]&1) {
                leaf[0] = leaf[1] = leaf[0] / 2;
            }else {
                leaf[0] /= 2;
                leaf[1] = leaf[0] - 1;
            }
            k -= leafcnt[0] + leafcnt[1];
            leafcnt[0] = cnt[0];
            leafcnt[1] = cnt[1];
        }
        printf("Case #%d: ", ca);
        if(k > leafcnt[0])
            printf("%lld %lld\n", leaf[1]/2, leaf[1]/2 - (1^leaf[1]&1));
        else
            printf("%lld %lld\n", leaf[0]/2, leaf[0]/2 - (1^leaf[0]&1));

    }
    return 0;
}
