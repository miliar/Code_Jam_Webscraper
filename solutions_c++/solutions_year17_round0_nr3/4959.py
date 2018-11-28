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

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll n, k, p = 1, cp = 1;
        cin >> n >> k;
        while (cp < k) {
            p *= 2;
            cp += p;
        }
        cp -= p;
        k -= cp;
        ll r = (n - cp);
        ll m = r / p;
        if (m == 0) {
            cout << "Case #" << t << ": ";
            cout << 0 << " " << 0 << "\n";
            continue;
        }
        ll b = r - m * p;
        ll mn = (m - 1) / 2;
        ll mx = m - 1 - mn;
        if (k <= b) mn += 1;
        cout << "Case #" << t << ": ";
        cout << max(mn, mx) << " " << min(mn, mx) << "\n";
    }
    return 0;
}
