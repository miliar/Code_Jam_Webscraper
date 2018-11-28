#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <iomanip>
#include <functional>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;


typedef long long lint, ll;
typedef long double ldouble, ld;

#ifdef LOCAL
	#define dbg(expr) cerr << "[" << __LINE__ << "] " << #expr << " = " << (expr) << '\n';
#else
	#define dbg(expr) (void) 0;
#endif


lint div_up(lint x, lint y) {
    return (x + y - 1) / y;
}

void solve(int test_case) {
    lint n, k;
    cin >> n >> k;
    map<lint, lint> profile;
    profile[n] = 1;
    while (k > 0) {
        auto cur = *profile.rbegin();
        profile.erase(cur.first);
        lint len = cur.first;
        //cerr << len << endl;
        lint left_len = (len - 1) / 2;
        lint right_len = div_up(len - 1, 2);
        if (left_len > 0)
            profile[left_len] += cur.second;
        if (right_len > 0)
            profile[right_len] += cur.second;
        k -= cur.second;
        if (k <= 0) {
            cout << "Case #" << test_case + 1 << ": " << max(left_len, right_len) << ' ' << min(left_len, right_len) << endl;
            break;
        }
    }
    /*
    for (int i = 0; i < k; i++) {
        auto cur = *profile.begin();
        profile.erase(profile.begin());
        lint len = -cur.first;
        lint left_len = (len - 1) / 2;
        lint right_len = div_up(len - 1, 2);
        if (left_len > 0)
            profile.emplace(-left_len, cur.second);
        if (right_len > 0)
            profile.emplace(-right_len, cur.second + left_len + 1);
        if (i == k - 1) {
            cout << "Case #" << test_case + 1 << ": " << max(left_len, right_len) << ' ' << min(left_len, right_len) << endl;
            return;
        }
    }
    */
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve(i);
}
