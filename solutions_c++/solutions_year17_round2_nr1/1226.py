/**

**/
#include <bits/stdc++.h>
using namespace std;
#define N 2000
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test;
pair <ll, ll> a[2000];
long long D;
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> D >> n;
        for (int i = 0; i < n; i++) cin >> a[i].first >> a[i].second;
        sort(a, a + n);
        cout << setprecision(6) << fixed;
        long long k = n - 1;
        for (int j = 0; j < n - 1; j++) {
            int i = n - (j + 1) - 1;
            if ((D - a[i].first) * a[k].second > (D - a[k].first) * a[i].second) {
                k = i;
            }
        }
        double ans = double(D) * double(a[k].second) / double(D - a[k].first);
        cout << "Case #" << te << ": " << ans << "\n";

    }
}
int main() {
    freopen("main.in", "r", stdin);
    //freopen("main.in", "w", stdout);
    freopen("main.out", "w", stdout);
    solve();
    //fclose(stdin);
    //fclose(stdout);
}
///CTKB1997
