#include <algorithm>
#include <iterator>
#include <iostream>
#include <utility>
#include <string>
#include <vector>
#include <queue>

using namespace std;

typedef long long ll;

struct segment
{
    ll left, right, len; // [l, r]
    segment(ll left, ll right):
        left(left), right(right), len(right - left + 1)
    { }
};

bool operator < (const segment& x, const segment& y)
{
    if(x.len == y.len) {
        return x.left < y.left;
    }
    return x.len < y.len;
}

pair<ll, ll> solve(ll n, ll k)
{
    std::priority_queue<segment> pq;

    pq.push(segment(0, n - 1));
    ll out_left = -1, out_right = -1;

    for(int i = 0; i < k; i++) {
        segment s = pq.top();
        pq.pop();
        ll m = s.left + (s.right - s.left) / 2;
        // cout << "get: [" << s.left << ", " << s.right << "]" << endl;
        // cout << "mid = " << m << endl;


        ll cur_left = m - s.left;
        ll cur_right = s.right - m;

        // cout << m << endl;
        // cout << cur_left << " " << cur_right << endl;

        out_left = min(cur_left, cur_right);
        out_right = max(cur_left, cur_right);
        if(s.left <= m - 1) {
            // cout << "push: [" << s.left << ", " << m - 1 << "]" << endl;
            pq.push(segment(s.left, m - 1));
        }
        if(m + 1 <= s.right) {
            // cout << "push: [" << m + 1 << ", " << s.right << "]" << endl;
            pq.push(segment(m + 1, s.right));
        }
    }

    return make_pair(out_left, out_right);
}

int main()
{
    int t;
    cin >> t;

    for(int test = 1; test <= t; test++) {
        ll n, k;
        cin >> n >> k;
        pair<ll, ll> p = solve(n, k);
        cout << "Case #" << test << ": " << p.second << " " << p.first << endl;
    }

    return 0;
}
