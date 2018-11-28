#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

long long l, r;

void h(long long n, long long m){
    if (m == 1){
        l = r = n / 2;
        if (n % 2 == 0) --r;
        return;
    }
    long long x = n/2, y = m/2;
    if (n % 2 == 0 && m % 2 == 1) --x;
    h(x, y);
}

int main(){
    freopen("/Users/eajoy/Downloads/C-large.in", "r", stdin);
    freopen("/Users/eajoy/Downloads/C-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int CASE = 1; CASE <= T; ++CASE){
        long long n, m;
        scanf("%lld%lld", &n, &m);
        h(n, m);
        printf("Case #%d: %lld %lld\n", CASE, l, r);
    }
    return 0;
}
