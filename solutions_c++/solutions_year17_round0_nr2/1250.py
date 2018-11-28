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


lint conv(const string & s) {
    lint x = 0;
    for (auto c : s) {
        x *= 10;
        x += c - '0';
    }
    return x;
}

bool check(const string & s) {
    if (s[0] == '0')
        return false;
    for (int i = 1; i < (int)s.length(); i++) {
        if (s[i] < s[i - 1])
            return false;
    }
    return true;
}

void solve(int test_case) {
    unsigned long long int n;
    cin >> n;
    cout << "Case #" << test_case + 1 << ": ";
    if (n < 10) {
        cout << n << endl;
        return;
    }
    unsigned long long max_number = 0;
    while (max_number * 10 + 9 <= n)
        max_number = max_number * 10 + 9;
    auto s = to_string(n);
    while (!check(s)) {
        if (s[0] == '0')
            break;
        for (int i = 1; i < (int)s.length(); i++) {
            if (s[i] < s[i - 1]) {
                s[i - 1]--;
                for (int j = i; j < (int)s.length(); j++)
                    s[j] = '9';
                break;
            }
        }
    }
    if (check(s))
        max_number = max(max_number, (unsigned long long)conv(s));
    cout << max_number << endl;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve(i);
}
