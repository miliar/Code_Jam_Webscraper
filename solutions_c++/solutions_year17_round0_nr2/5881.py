#include <bits/stdc++.h>

using namespace std;


bool check(long long n) {
    auto s = to_string(n);
    for(int i=0; i+1<s.length(); ++i) {
        if(s[i] > s[i+1]) return true;
    }
    return false;
}

long long gao(long long n) {
    auto s = to_string(n);
    for(int i=0; i+1<s.length(); ++i) {
        if(s[i] > s[i+1]) {
            -- s[i];
            for(int j=i+1; j<s.length(); ++j) {
                s[j] = '9';
            }
            long long ret = 0;
            sscanf(s.c_str(), "%lld", &ret);
            return ret;
        }
    }
    return n;
}

void solve() {
    long long n;
    scanf("%lld", &n);
    while(check(n)) {
        n = gao(n);
    }
    printf("%lld\n", n);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T, cas = 0;
    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++cas);
        solve();
    }
    return 0;
}
