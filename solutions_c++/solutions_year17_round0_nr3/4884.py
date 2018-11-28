#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        long long N, K;
        cin >> N >> K;
        long long smallcnt = 1, bigcnt = 0;
        while (K > smallcnt + bigcnt) {
            K = K - smallcnt - bigcnt;
            long long newsmall = 0, newbig = 0;
            if (N % 2 == 0) {
                newsmall = smallcnt;
                newbig = smallcnt + bigcnt * 2;
            } else {
                newsmall = smallcnt * 2 + bigcnt;
                newbig = bigcnt;
            }
            N = (N - 1) / 2;
            smallcnt = newsmall;
            bigcnt = newbig;
        }
        if (K <= bigcnt) {
            N = N + 1;
        }
        long long smax, smin;
        if (N % 2 == 0) {
            smax = (N - 1) / 2 + 1;
            smin = (N - 1) / 2;
        } else {
            smax = smin = (N - 1) / 2;
        }
        printf("Case #%d: %lld %lld\n", t, smax, smin);
    }
    return 0;
}
