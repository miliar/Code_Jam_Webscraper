#include <iostream>
#include <vector>
#include <utility>
#include <map>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;

P slow(ll n, ll k)
{
    vector<bool> v(n + 2, false);
    v[0] = v[n+1] = true;
    int bestmi, bestma, best;
    for (int i = 0; i < k; ++i) {
        bestmi = -1;
        bestma = -1;
        best = -1;
        for (int j = 1; j < n+1; ++j) {
            if (!v[j]) {
                int ls = 0;
                while (!v[j - ls - 1]) {
                    ++ls;
                }
                int rs = 0;
                while (!v[j + rs + 1]) {
                    ++rs;
                }
                int mi = min(ls, rs);
                int ma = max(ls, rs);
                if (mi > bestmi || (mi == bestmi && ma > bestma)) {
                    best = j;
                    bestmi = mi;
                    bestma = ma;
                }
            }
        }
        v[best] = true;
    }
    return {bestma, bestmi};
}

P fast(ll n, ll k)
{
    ll k2 = k;
    map<P, ll> nodes;
    ll n1 = n/2LL;
    ll n2 = (n-1LL)/2LL;
    nodes[{n1, n2}] = 1LL;
    ll bits = 0;
    while (k2 > 1LL) {
        map<P, ll> newNodes;
        for (auto p : nodes) {
            ll ma = p.first.first;
            ll mi = p.first.second;
            newNodes[{ma/2LL, (ma-1LL)/2LL}] += p.second;
            newNodes[{mi/2LL, (mi-1LL)/2LL}] += p.second;
        }
        nodes = newNodes;
        k2 /= 2LL;
        bits++;
    }

    for (auto it = nodes.rbegin(); it != nodes.rend(); it++) {
        //cout << (it->first).first << ' ' << (it->first).second << ' ' << it->second << endl;
    }
    k2 = k - (1LL << bits);
    for (auto it = nodes.rbegin(); it != nodes.rend(); it++) {
        k2 -= it->second;
        if (k2 < 0) {
            return it->first;
        }
    }
    return {-1, -1};
}

int main()
{
    /*cout << 5000 << endl;
    for (int i = 1; i < 100; ++i) {
        for (int j = 1; j <= i; ++j) {
            cout << i << ' ' << j << endl;
        }
    }*/

    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        ll n, k;
        cin >> n >> k;
        P result = fast(n, k);
        //P result = slow(n, k);
        cout << "Case #" << cas << ": " << result.first << ' ' << result.second << endl;
    }
}
