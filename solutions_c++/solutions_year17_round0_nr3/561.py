#include <iostream>
#include <map>

using namespace std;

typedef long long ll;

ll n, k;

void solve(int x) {
    cin >> n >> k;
    map<ll,ll> s;
    s[n] = 1;
    ll a, b;
    while (k > 0) {
        pair<ll,ll> p = *s.rbegin();
        ll u = p.first; ll c = p.second;
        s.erase(u);
        if (u%2 == 0) {
            a = u/2;
            b = u/2-1;
            s[u/2-1] += c;
            s[u/2] += c;
        } else {
            a = u/2;
            b = u/2;
            s[u/2] += c;
            s[u/2] += c;
        }
        k -= c;
    }
    cout << "Case #" << x << ": " << a << " " << b << "\n";
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
