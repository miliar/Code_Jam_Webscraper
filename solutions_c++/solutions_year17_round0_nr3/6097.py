#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

bool f(long long t, long long N) {
    if(pow(2, t)-1 < N && N <= pow(2, t+1)-1) {
        return true;
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        long long N, K, ans, ans2;
        cin >> N >> K;
        long long t = log(K+1) / log(2);
        if(f(t, K));
        else if(f(t-1, K)) t = t-1;
        else if(f(t+1, K)) t = t+1;
        else {printf("err\n");}

        //printf("%d\n", t);
        long long prev = pow(2, t) - 1;
        N = N - prev;
        long long q = N / pow(2, t);
        long long mod = N - pow(2, t)*q;
        long long key;
        if(K - prev <= mod) {
            key = q + 1;
        } else {
            key = q;
        }
        if((key-1) % 2 == 0) {
            ans = ans2 = (key-1) / 2;
        } else {
            ans = (key-1) / 2 + 1;
            ans2 = ans - 1;
        }

        printf("Case #%d: %lld %lld\n", tc, ans, ans2);
    }
    return 0;
}
