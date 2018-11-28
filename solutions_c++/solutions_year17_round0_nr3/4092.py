#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef pair < ll, ll > pll;

ll n, k;
map < ll, ll > q;

void add(ll len, ll add) {
    if (len == 0) return;
    if (q.find(len) != q.end())
        q[len] += add;
    else q[len] = add;
}

void solve (int caseNum) {

    cin >> n >> k;
    q.clear();
    q.emplace(n, 1);
    ll mn = -1, mx = -1;
    while ( !q.empty() ){
        auto it = q.end(); it --;
        ll len = it -> first;
        ll cnt = it -> second;
        if (cnt >= k) {
            mn = (len - 1) / 2;
            mx = (len - 1) - mn;
            break;
        }
        k -= cnt;
        q.erase(it);
        ll l1 = (len - 1) / 2;
        ll r1 = len - 1 - l1;
        add(l1, cnt);
        add(r1, cnt);
    }
    cout << "Case #" << caseNum << ": " << mx << " " << mn << "\n";
}

int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t;
    scanf ("%d", &t);
    for (int i = 1; i <= t; i ++)
        solve(i);
    return 0;
}
