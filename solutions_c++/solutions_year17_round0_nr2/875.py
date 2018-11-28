#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>

#define ull unsigned long long
#define mo 1000000007

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;

//ll moMul(ll a, ll b) {
//    return ((a % mo) * (b % mo)) % mo;
//}

ll solve(ll n) {
    vector<int> foo;
    while (n) {
        foo.push_back(n % 10);
        n /= 10;
    }
    for (int i = 0; i < foo.size() - 1; ++i) {
        if (foo[i] < foo[i + 1]) {
            for (int j = 0; j <= i; ++j) {
                foo[j] = 9;
            }
            int bar = i + 1;
            while (bar < foo.size() && foo[bar] == 0) {
                foo[bar] = 9;
                ++bar;
            }
            --foo[bar];
            if (bar == foo.size() - 1 && foo[bar] == 0) foo.pop_back();
        }
    }
    ll res = 0;
    for (int i = foo.size() - 1; i >= 0; --i) {
        res = res * 10 + foo[i];
    }
    return res;
}

int main() {
    freopen("/Users/Swing/Documents/code/googleCodeJam/B-large.in", "r", stdin);
    freopen("/Users/Swing/Documents/code/googleCodeJam/B-large.out", "w", stdout);

    int t;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        ll n;
        cin >> n;
        cout << solve(n) << endl;
//        printf("Case #%d: %.8f\n", i, res);
//        cout << "Case #" << i << ": " << tmp << endl;
//        printf("Case #%d: %.7lf\n", i, res);

    }

    return 0;
}