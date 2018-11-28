#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
using namespace std;
#define FU(i, a, b) for (int i = (a); i < (b); ++i)
#define fu(i, b) FU(i, 0, b)
#define FD(i, a, b) for (int i = (int) (b) - 1; i >= (a); --i)
#define fd(i, b) FD(i, 0, b)
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define pb push_back

int main() {
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(6);
    int T;
    cin >> T;
    FU(t, 1, T+1) {
        int d, n;
        cin >> d >> n;
        vector<int> k(n), s(n);
        fu(i, n) cin >> k[i] >> s[i];
        vector<double> time(n);
        fu(i, n) time[i] = (double) (d - k[i]) / s[i];
        auto worst = *max_element(all(time));
        double res = d / worst;
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
