#include <bits/stdc++.h>

#define LL long long
#define mp make_pair
#define ii pair<LL, LL>

using namespace std;

ii solve(LL n, LL k) {
    // printf("%lld %lld\n", n, k);

    if(n == 0) return {0, 0};
    if(k > 0) {
        if(k / 2 >= 1) {
            if(k % 2 == 1 && n % 2 == 0) {
                return solve((n - 2) / 2, k / 2);
            } else {
                return solve(n / 2, k / 2);
            }
        } else {
            // if(n % 2 == 0) return { n / 2, n / 2 + 1};
            // return { (n + 1) / 2, (n + 1) / 2};
            if(n % 2 == 1) {
                return { (n - 1) / 2, (n - 1) / 2 };
            } else {
                // cout << "HI" << endl;
                return { n / 2, n / 2 - 1 };
            }
        }
    } else {
        return {n, n};
    }
}

int main() {

    int t;
    cin >> t;
    for(int i = 1; i <= t; i++) {
        LL n, k;
        cin >> n >> k;
        
        ii d = solve(n, k);
        printf("Case #%d: %lld %lld\n", i, d.first, d.second);
    }

    return 0;
}