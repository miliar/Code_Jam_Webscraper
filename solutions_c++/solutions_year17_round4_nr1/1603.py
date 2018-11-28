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


lint div_up(int n, int k) {
    return (n + k - 1) / k;
}

void solve(int test_number) {
    int n, p;
    cin >> n >> p;
    vector<int> number(p);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        number[x % p]++;
    }
    cout << "Case #" << test_number + 1 << ": ";
    if (p == 2)
        cout << number[0] + div_up(number[1], 2);
    if (p == 3)
        cout << number[0] + min(number[1], number[2]) + div_up(max(number[1], number[2]) - min(number[1], number[2]), 3);
    cout << endl;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve(i);
}
