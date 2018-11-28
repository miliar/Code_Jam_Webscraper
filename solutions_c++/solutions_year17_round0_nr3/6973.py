#include "bits/stdc++.h"

using namespace std;

typedef long long ll;
typedef pair < int, int > ii;

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;

    cin >> t;

    int test = 0;

    while(t--) {
        printf("Case #%d: ", ++test);
        ll n, k;
        scanf("%lld %lld", &n, &k);
        map < ll, int > M;
        M[n] = 1;
        ll l, r;
        while(k > 0) {
            auto it = --M.end();
            ll len = it -> first, cnt = it -> second;
            l = len / 2;
            r = len - 1 - l;
            k -= cnt;
            M.erase(it);
            M[l] += cnt;
            M[r] += cnt;
        }
        printf("%lld %lld\n", l, r);
    }

    return 0;

}

