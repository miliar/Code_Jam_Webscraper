#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <ctime>
#include <cstdlib>
#include <unordered_set>
#include <deque>
#include <queue>

using namespace std;

typedef long long ll;

ll ans = -1;

void rec (ll cur, ll n) {
    if (cur > n)
        return;
    ans = max(ans, cur);
    int start = cur % 10;
    if (cur == 0)
        start = 1;
    for (int i = start; i < 10; ++i) {
        if (cur <= (n - i) / 10)
            rec(cur * 1ll * 10 + i, n);
    }
}

ll getLast(ll n) {
    rec(0, n);
    return ans;
}

int main() {
    int tests;
    cin >> tests;
    for (int test_id = 0; test_id < tests; ++test_id) {
        ll n;
        cin >> n;
        ans = -1;
        cout << "Case #" << test_id + 1 << ": " << getLast(n) << endl;
    }
}
