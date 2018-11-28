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

pair<double, pair<int, int>> x[1003];


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            cin >> x[i].SI.FI >> x[i].SI.SI;
            x[i].FI = (double)2 * M_PI * (double)x[i].SI.FI * (double)x[i].SI.SI;
        }
        sort(x, x + n);
        reverse(x, x + n);
        double ths = 0;
        int mr = 0;
        for (int i = 0; i < k - 1; ++i) {
            ths += x[i].FI;
            mr = max(mr, x[i].SI.FI);
        }
        double ts = 0;
        for (int i = k - 1; i < n; ++i) {
            double mrc = (double)max(mr, x[i].SI.FI);
            ts = max(
                    ts,
                    ths + M_PI * mrc * mrc + (double)2 * M_PI * (double)x[i].SI.FI * (double)x[i].SI.SI
            );
        }
        cout << std::fixed << std::setprecision(6) << "Case #" << t << ": " << ts << endl;
    }

    return 0;
}
