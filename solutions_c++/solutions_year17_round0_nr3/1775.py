#include<bits/stdc++.h>

using namespace std;

#define mp(x,y) make_pair(x, y)
#define For(i, n) for (int i = 0; i < (int) n; i++)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int main () {
    int T;
    cin >> T;
    For(cases, T) {
        ll n, m;
        cin >> n >> m;
        map<ll,ll> counts;
        counts [n] = 1;
        ll lastmin, lastmax;
        while (m > 0) {
            auto it = counts.rbegin();
            lastmin = ((it->first) - 1) / 2;
            lastmax = (it->first)/ 2;
            counts[lastmin] += it->second;
            counts[lastmax] += it->second;
            m -= it->second;
            counts.erase(it->first);
        }
        printf("Case #%d: %lld %lld\n", cases + 1, lastmax, lastmin);
    }
}
