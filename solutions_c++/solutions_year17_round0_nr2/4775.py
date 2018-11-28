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

bool isTidy(int num) {
    string s = to_string(num);
    for (int i = 1; i < (int)s.size(); ++i) {
        if (s[i] < s[i - 1]) return false;
    }
    return true;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n;
        cin >> n;
        for (int i = n; i >= 0; --i) {
            if (isTidy(i)) {
                cout << "Case #" << t << ": " << i << "\n";
                break;
            }
        }
    }
    return 0;
}
