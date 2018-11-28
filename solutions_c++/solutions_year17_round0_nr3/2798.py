#include <algorithm>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <set>
#include <map>
#include <memory>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
#include <cassert>
#include <fstream>

using namespace std;

using LL = long long;


int main () {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout.setf(ios_base::fixed);
    cout.precision(24);
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        LL n, k;
        cin >> n >> k;
        map < LL, LL > cnt;
        cnt[n] = 1;
        while (k > 1) {
            auto mx = cnt.rbegin();
            LL len = mx->first;
            LL x = mx->second;
            LL d = min(x, (k - 1));
            len--;
            if (len % 2 == 0) {
                cnt[len / 2] += 2 * d;
            } else {
                cnt[len / 2] += d;
                cnt[len / 2 + 1] += d;
            }
            len++;
            if (d == x) {
                cnt.erase(len);
            } else {
                cnt[len] -= d;
            }
            k -= d;
        }
        auto mx = cnt.rbegin();
        LL len = mx->first - 1;
        LL x = mx->second;
        LL l = len / 2, r = len / 2 + (len % 2);
        cout << "Case #" << tt + 1 << ": " << max(r, l) << " "  << min(r, l) << "\n";
    }
    return 0;
}