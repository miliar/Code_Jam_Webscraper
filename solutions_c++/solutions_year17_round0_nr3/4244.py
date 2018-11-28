/** @xigua */
#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<cstring>
#include<queue>
#include<set>
#include<string>
#include<map>
#include<climits>
#define PI acos(-1)
using namespace std;
typedef long long ll;
typedef double db;
const int maxn = 2e2 + 5;
const int mod = 1e9 + 7;
const int INF = 1e8 + 5;
const ll inf = 1e15 + 5;
const db eps = 1e-6;

void solve() {
   // priority_queue<ll, vector<ll>, greater<ll> > pq;
   priority_queue<ll> pq;
    ll n, k; cin >> n >> k;
    pq.push(n); k--;
    while (k--) {
        ll tmp = pq.top();
        pq.pop();
        ll n1 = tmp / 2;
        pq.push(n1), pq.push(tmp - n1 - 1);
       // cout << n1 << ' ' << tmp << endl;
    }
    ll tmp = pq.top();
   // cout << tmp << endl;
    ll maxx = tmp >> 1;
    ll minn = tmp - maxx - 1;
    cout << maxx << ' ' << minn << endl;
}

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int t = 1, cas = 1;
    cin >> t;
    //init();
    while(t--) {
        printf("Case #%d: ", cas++);
        solve();
    }
    return 0;
}
