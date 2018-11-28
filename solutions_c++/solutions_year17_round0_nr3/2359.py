#include <cstdio>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

typedef long long ll;

pair<ll, ll> solve(ll n, ll k) {
    priority_queue<pair<ll,ll>> q;
    ll passed = 0;
    q.push(make_pair(n, 1));

    //cout << "N = " << n << ", K = " << k << endl;
    while (!q.empty()) {
        ll size = q.top().first;
        ll count = 0;

        while (!q.empty() && q.top().first == size) {
            count += q.top().second;
            q.pop();
        }

        //cout << size << " " << count << endl;

        passed += count;
        if (passed >= k) {
            return make_pair(size / 2, (size-1)/2);
        }

        if (size % 2 == 1) {
            q.push(make_pair(size / 2, count * 2));
        } else {
            q.push(make_pair(size / 2, count));
            q.push(make_pair((size-1)/2, count));
        }
    }
}

int main() {
    int testCases;
    cin >> testCases;

    for (int test = 1; test <= testCases; test++) {
        ll n, k;
        cin >> n >> k;
        pair<ll,ll> ans = solve(n, k);
        cout << "Case #" << test << ": " << ans.first << " " << ans.second << endl;
    }
}
