#include <iostream>
#include <queue>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;

int t;
ll n, k;

#define mp make_pair
#define rep(i,a,b) for(int i=a;i<b;i++)

pll calcAns(ll t) {
    if (t % 2) { // È¦¼ö
        return mp(t / 2, t / 2);
    }
    else {
        return mp(t / 2, t / 2 - 1);
    }
}

void proc(int tc) {
    cin >> n >> k;
    ll pos = 0;
    priority_queue<pll> pq;
    pll tmp;
    pq.push(mp(n, 1));

    do {
        tmp = pq.top();
        pq.pop();
        pos += tmp.second;
        if (tmp.first % 2) {
            pq.push(mp(tmp.first / 2, tmp.second * 2));
        }
        else {
            pq.push(mp(tmp.first / 2, tmp.second));
            pq.push(mp(tmp.first / 2 - 1, tmp.second));
        }
    } while (pos < k);

    pll ans = calcAns(tmp.first);
    printf("Case #%d: %lld %lld\n", tc, ans.first, ans.second);
}

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    cin >> t;
    rep(tc, 1, t + 1) {
        proc(tc);
    }
    return 0;
}