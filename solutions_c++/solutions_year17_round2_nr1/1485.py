#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int d, n;
        cin >> d >> n;

        double time = 0;
        for (int j = 0; j < n; j++) {
            int k, s;
            cin >> k >> s;
            time = max(time,((double) (d-k))/s);
        }
        cout << "Case #" << i+1 << ": " << fixed << setprecision(6) << (double) d/time << "\n";
    }
    return 0;
}
