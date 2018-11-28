#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int d, n;
        cin >> d >> n;
        double anst = 0;
        for (int i = 0; i < n; i++) {
            double k, s;
            cin >> k >> s;
            anst = max(anst, (d - k) / s);
        }
        cout << fixed << setprecision(6) << "Case #" << t << ": " << d / anst << endl;
    }
}
