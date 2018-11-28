#include <bits/stdc++.h>
using namespace std;

long long arr[50];

long long solve (long long x) {

    for (int i=0; i<20; i++) {
        arr[i] = x%10;
        x/=10;
    }

    bool ok = 0;

    while (true) {

        ok = 1;
        for (int i=19; i>0; i--) {
            if ( arr[i] > arr[i-1] ) {
                ok = 0;

                arr[i]--;
                for (int j=i-1; j>=0; j--) {
                    arr[j] = 9;
                }

                break;
            }

        }

        if (ok) break;
    }

    long long ans = 0, mul = 1;
    for (int i=0; i<20; i++) {
        ans += arr[i] * mul;
        mul *= 10;
    }

    return ans;
}

int main () {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int cas = 1; cas <= t; cas++) {
        long long n; cin >> n;
        cout << "Case #" << cas << ": " << solve(n) << endl;
    }
}
