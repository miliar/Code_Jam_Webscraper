#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for(int NCASE=1; NCASE<=T; ++NCASE) {
        long long N, K;
        scanf("%lld%lld", &N, &K);
        long long n1 = N, n2 = 0;
        long long i1 = 1, i2 = 0;
        while( K > i1 + i2 ) {
            //printf("%lld %lld / %lld %lld\n", n1, i1, n2, i2);
            K -= i1 + i2;
            if( n2 == 0 ) {
                if( n1%2 == 1 ) {
                    n1 = (n1 - 1) / 2;
                    i1 = i1 * 2;
                    n2 = 0, i2 = 0;
                }
                else {
                    n2 = n1 / 2;
                    i2 = i1;
                    n1 = n1 / 2 - 1;
                }
            }
            else {
                long long nn1, nn2, ii1, ii2;
                if( n1%2 == 1 ) {
                    nn1 = (n1 - 1) / 2;
                    nn2 = (n2/2 == nn1) ? n2/2 - 1 : n2/2;
                    ii1 = i1 * 2;
                    ii2 = 0;
                }
                else {
                    nn1 = n1 / 2 - 1;
                    nn2 = n1 / 2;
                    ii1 = i1;
                    ii2 = i1;
                }
                if( n2%2 == 1 ) {
                    if( (n2 - 1) / 2 == nn1 ) {
                        ii1 += i2 * 2;
                    }
                    else {
                        ii2 += i2 * 2;
                    }
                }
                else {
                    ii1 += i2;
                    ii2 += i2;
                }
                n1 = nn1;
                n2 = nn2;
                i1 = ii1;
                i2 = ii2;
            }
            if( n2 > n1 ) {
                swap(n1, n2);
                swap(i1, i2);
            }
        }
        //printf("%lld %lld / %lld %lld\n", n1, i1, n2, i2);
        long long a, b;
        if( K <= i1 ) {
            if( n1%2 == 1 )
                a = b = (n1-1) / 2;
            else
                a = n1/2, b = n1/2 - 1;
        }
        else {
            if( n2%2 == 1 )
                a = b = (n2-1) / 2;
            else
                a = n2/2, b = n2/2 - 1;
        }
        printf("Case #%d: %lld %lld\n", NCASE, a, b);
    }
    return 0;
}
