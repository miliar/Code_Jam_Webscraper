#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    for (int testCase = 0; testCase < T; ++testCase) {
        long long d;
        int n;
        cin >> d >> n;
        long long k, s;
        cin >> k >> s;
        long double max_v = (d * s) / 1.0l / (d - k);
        for (; n > 1; --n) {
            cin >> k >> s;
            max_v = min(max_v, (d * s) / 1.0l / (d - k));
        }
        cout << "Case #" << testCase + 1 << ": ";
        cout << fixed << setprecision(20) << max_v;
        cout << endl;
    }
    return 0;
}
