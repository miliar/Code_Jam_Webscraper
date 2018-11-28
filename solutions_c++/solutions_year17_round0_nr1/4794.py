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
string s;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int k;
        cin >> s >> k;
        int n = (int)s.size();
        reverse(s.begin(), s.end());
        int f = 0;
        for (int i = 0; i <= (n - k); ++i) {
            if (s[i] == '+') continue;
            for (int j = i; j < (i + k); ++j)
                s[j] = (s[j] == '+' ? '-' : '+');
            f += 1;
        }
        for (int i = (n - k); i < n; ++i) {
            if (s[i] == '-') {
                f = -1;
                break;
            }
        }
        cout << "Case #" << t << ": ";
        if (f == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << f << "\n";
        }
    }
    return 0;
}
