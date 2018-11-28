#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

string get_solution(ll n, ll k) {
    map<ll, ll> count_by_l;
    count_by_l[n] = 1;
    stringstream ans;
    for (;;) {
        auto it = count_by_l.end();
        it--;
        ll cur_max_l = (*it).first;
        cur_max_l--;
        ll cur_max_count = (*it).second;
        if (cur_max_count >= k) {
            ans << cur_max_l / 2 + cur_max_l % 2 << ' ' << cur_max_l / 2;
            return ans.str();
        } else {
            k -= cur_max_count;
        }
        count_by_l.erase(it);
        if (count_by_l.find(cur_max_l / 2) == count_by_l.end()) {
            count_by_l[cur_max_l / 2] = cur_max_count;
        } else {
            count_by_l[cur_max_l / 2] += cur_max_count;
        }
        if (count_by_l.find(cur_max_l / 2 + cur_max_l % 2) == count_by_l.end()) {
            count_by_l[cur_max_l / 2 + cur_max_l % 2] = cur_max_count;
        } else {
            count_by_l[cur_max_l / 2 + cur_max_l % 2] += cur_max_count;
        }
    }
}

int main() {

    ios::sync_with_stdio(false);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
//#else
//    freopen(".in", "r", stdin);
//    freopen(".out", "w", stdout);
#endif

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        ll n, k;
        cin >> n >> k;
        cout << "Case #" << i + 1 << ": " << get_solution(n, k) << endl;
    }

    return 0;
}
