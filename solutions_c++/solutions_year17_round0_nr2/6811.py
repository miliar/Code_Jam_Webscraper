#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long ll;

bool calc(ll x) {
    int dig[20], len = 0;
    memset(dig, 0, sizeof(dig));
    while(x){
        dig[len++] = x % 10;
        x /= 10;
    }
    bool flag = true;
    for (int i = 1; i < len; i++) {
        if (dig[i] > dig[i - 1]) { flag = false; break; }
    }
    return flag;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        ll n;
        scanf("%lld", &n);
        while (n) {
            if (calc(n)) {
                printf("Case #%d: %lld\n", c, n);
                break;
            }
            n--;
        }
    }
    return 0;
}