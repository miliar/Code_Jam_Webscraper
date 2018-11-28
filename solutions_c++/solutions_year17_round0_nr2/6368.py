#include<bits/stdc++.h>
#define LL long long
using namespace std;
LL mul(int a, int n) {
    LL sum = 0;
    for(int i = 0; i < n; i++)
        sum = sum * 10 + a;
    return sum;
}
int main() {
    // freopen("B-large.in", "r", stdin);
    // freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int cnt = 1; cnt <= t; cnt++) {
        LL n;
        cin >> n;
        int len = 18;
        LL ans = 0;
        for(int i = len; i >= 0; i--) {
            for(int j = 9; j >= 1; j--) {
                if(ans + mul(j, i) <= n) {
                    ans += mul(j, i) - mul(j, i - 1);
                    break;
                }
            }
        }
        cout << "Case #" << cnt << ": ";
        cout << ans << endl;
    }

    return 0;
}
