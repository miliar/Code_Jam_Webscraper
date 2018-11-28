#include <stdio.h>
#include <string.h>


const int N = 1000000;

long long cnt[N], num[N], n, k;

int main() {
    int t;
    scanf("%d", &t);
    for (int o=1; o<=t; o++) {
        long long l, r;
        int lst, nw;
        scanf("%lld %lld", &n, &k);
        for (int i=0; i<N; i++) {
            cnt[i] = 0;
            num[i] = -1;
        }
        lst = 2;
        nw = 1;
        num[nw] = n;
        cnt[nw] = 1;
        while (num[nw]>=1) {
            l = (num[nw]-1)/2;
            r = num[nw]/2;
            if (num[lst-1]!=r && num[lst-2]!=r) {
                num[lst] = r;
                cnt[lst] = cnt[nw];
                lst++;
            } else {
                cnt[(num[lst-1]==r ? lst-1 : lst-2)] += cnt[nw];
            }
            if (num[lst-1]!=l && num[lst-2]!=l) {
                num[lst] = l;
                cnt[lst] = cnt[nw];
                lst++;
            } else {
                cnt[(num[lst-1]==l ? lst-1 : lst-2)] += cnt[nw];
            }
            nw++;
        }
        /*
        for (int i=1; i<lst; i++) {
            printf("%lld:%lld  ", num[i], cnt[i]);
            puts("");
        }
        */
        for (int i=1; i<lst; i++)
            cnt[i] += cnt[i-1];
        for (int i=0; i<lst; i++) {
            if (k<=cnt[i]) {
                printf("Case #%d: %lld %lld\n", o, num[i]/2, (num[i]-1)/2);
                break;
            }
        }
        
        //printf("%d %lld\n", lst, sum);
    }
}
