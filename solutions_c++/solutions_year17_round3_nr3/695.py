#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <bitset>
#include <unordered_map>
#include <iomanip>
#include <queue>

#define mp make_pair
#define pb push_back
#define FI first
#define SI second


#ifdef _MSC_VER
#define ALIGN(x) __declspec(align(x))
#else
#define ALIGN(x) __attribute__((aligned(x)))
#endif

using namespace std;

typedef long long ll;

const int maxn = 100007;
const int hf = 720;

double x[57];


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, k;
        cin >> n >> k;
        double u;
        cin >> u;
        for (int i = 0; i < n; ++i) cin >> x[i];
        sort(x, x + n);
        x[n] = 1.0;
        int l = 0;
        double c = 0, p = 0;
        for (int i = 1; i <= n; ++i) {
            double nc = c + (x[i] - x[i - 1]) * i;
//            cout << "I = " << i << ": x = " << x[i] << endl;
            if (nc > u) {
                l = i;
                p = x[i - 1] + (u - c) / (double)i;
//                cout << "p will " << p << endl;
                c = u;
                break;
            } else {
                l = i + 1;
                c = nc;
                p = x[i];
//                cout << "p will " << p << endl;
            }
        }
        double ans = 1;
        for (int i = 0; i < l; ++i) ans *= p;
        for (int i = l; i < n; ++i) ans *= x[i];
        cout << std::fixed << std::setprecision(6) << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
