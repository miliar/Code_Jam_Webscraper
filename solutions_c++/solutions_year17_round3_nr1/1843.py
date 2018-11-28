#include <bits/stdc++.h>
#include <algorithm>
#include <cmath>

using namespace std;

#define ll long long int
vector<ll> radius, height, dummy;

bool cmp(ll i1, ll i2) {
    return radius[i1] < radius[i2];
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    cout.precision(10);
    cout << fixed;
    //cout << M_PI;

    int tests;
    cin >> tests;
    for (int tcase = 1; tcase <= tests; tcase++) {
        ll n, k;
        cin >> n >> k;
        radius.assign(n, 0);
        height.assign(n, 0);
        dummy.assign(n, 0);
        for (ll i = 0; i < n; i++) {
            dummy[i] = i;
            cin >> radius[i] >> height[i];
        }

        sort(dummy.begin(), dummy.end(), cmp);
        vector<ll> tmp(n, 0);
        for (ll i = 0; i < n; i++) {
            tmp[i] = radius[dummy[i]];
        }
        radius = tmp;
        tmp.assign(n, 0);
        for (ll i = 0; i < n; i++) {
            tmp[i] = height[dummy[i]];
        }
        height = tmp;
        reverse(radius.begin(), radius.end());
        reverse(height.begin(), height.end());

        /*for (ll i = 0; i < n; i++) {
            cout << radius[i] << " " << height[i] << "\n";
        }*/

        vector< vector<ll> > dp(n, vector<ll>(k, 0));
        for (ll i = n - 1; i >= 0; i--) {
            //cout << "Pancake " << i << "\n";
            ll r1, h1, r2, h2;
            r1 = radius[i]; h1 = height[i];
            dp[i][0] = r1 * r1 + 2 * r1 * h1;
            for (ll q = 1; q < k; q++) {
                dp[i][q] = -1;
            }

            for (ll q = 1; q < k; q++) {
                for (ll j = i + 1; j < n; j++) {
                    if (dp[j][q - 1] != -1) {
                        r2 = radius[j];
                        h2 = height[j];
                        dp[i][q] = max(dp[i][q], 2 * r1 * h1 + (r1 * r1 - r2 * r2) + dp[j][q - 1]);
                    }
                }
            }
            /*for (ll q = 0; q < k; q++) {
                if (dp[i][q] != -1) {
                    cout << "1 ";
                } else {
                    cout << "0 ";
                }
            }
            cout << "\n";*/
        }

        ll mx = 0;
        for (int i = 0; i < n; i++) {
            mx = max(mx, dp[i][k - 1]);
        }

        cout << "Case #" << tcase << ": " << mx * M_PI << "\n";
    }
    return 0;
}