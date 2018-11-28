#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

typedef long long ll;

#define rep(i,a,b) for(int i=a;i<b;i++)

int t;
ll n, ans;

ll proc() {
    ll pos = 1;
    int a, b;

    while (pos < n) {
        a = n / pos % 100 / 10;
        b = n / pos % 10;
        if (a > b) {
            n -= (1 + n % (pos * 10));
        }
        pos *= 10;
    }
    return n;
}

int main() {
    freopen("B-large.in", "r", stdin);
    cin >> t;
    rep(tc, 1, t + 1) {
        cin >> n;
        printf("Case #%d: %lld\n", tc, proc());
    }
    return 0;
}