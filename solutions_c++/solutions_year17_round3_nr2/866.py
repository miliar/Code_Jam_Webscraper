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

pair<int, int> a[103], b[103];


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; ++i) cin >> a[i].FI >> a[i].SI;
        for (int i = 0; i < m; ++i) cin >> b[i].FI >> b[i].SI;
        if (n < m) {
            swap(n, m);
            swap(a, b);
        }
        sort(a, a + n);
        int ans = 0;
        if (n + m == 1) {
            ans = 2;
        } else if (n + m == 2 && n == 2) {
            ans = a[1].SI - a[0].FI <= hf || a[0].SI + 2 * hf - a[1].FI <= hf ? 2 : 4;
        } else if (n + m == 2 && n == 1) {
            ans = 2;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
