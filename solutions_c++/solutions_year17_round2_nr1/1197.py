#include <iostream>
#include <cstdio>

using namespace std;
typedef long long ll;


int main() {
    freopen("../A-large.in", "r", stdin);
    freopen("../A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        int n;
        double S;
        cin >> S>> n;
        double maxT = 0;
        for (int i = 1; i <= n; i++) {
            int ki, si;
            cin >> ki >> si;
            double t = (S - ki) / si;
            maxT = max(t, maxT);
        }
        double ans = S / maxT;
        printf("Case #%d: %.10f\n", cas, ans);

    }

    return 0;
}