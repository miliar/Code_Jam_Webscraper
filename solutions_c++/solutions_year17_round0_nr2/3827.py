#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

int dig[20];

long long qpow(long long a, long long b) {
    long long ans = 1;
    while (b) {
        if (b & 1) ans = ans * a;
        a = a * a;
        b >>= 1;
    }
    return ans;
}

long long dfs(int len, bool ismax, int last) {
    if (len < 0) return 0;
    int m = ismax ? dig[len] : 9;
    // cout<<dig[len]<<endl;
    long long ans = -1;
    for (int i = m; i >= last; i --) {
        long long res = dfs(len - 1, ismax && i == dig[len], i);
        // cout<<res<<endl;
        if (res != -1) 
            ans = max(ans, qpow(10, len) * i + res);
    }
    return ans;
}

int main(int argc, char const *argv[]) {
    freopen("B-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int T, kase = 1; cin>>T;
    while (T --) {
        int p = 0;
        long long x; cin>>x;
        while (x) {
            dig[p ++] = x % 10;
            x /= 10;
        }
        long long ans = dfs(p - 1, true, 0);
        printf("Case #%d: %lld\n", kase ++, ans);
    }
    return 0;
}