#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iomanip>
#include <queue>
#include <utility>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, char> pci;

void Solve(int test_index) {
    ll n, k;
    cin >> n >> k;
    map<ll, ll> cnt = {{-n, 1}};
    ll min_res, max_res;
    while (true) {
        pll curr = *cnt.begin();
        cnt.erase(cnt.begin());
        if (curr.second >= k) {
            min_res = (-curr.first - 1) / 2;
            max_res = -curr.first / 2;
            break;
        }
        cnt[-((-curr.first - 1) / 2)] += curr.second;
        cnt[-(-curr.first / 2)] += curr.second;
        k -= curr.second;
    }
    cout << "Case #" << test_index << ": " << max_res << ' ' << min_res << '\n';
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        Solve(test_index + 1);
    }
    return 0;
}
