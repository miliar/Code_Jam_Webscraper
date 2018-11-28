#include <iostream>
using namespace std;

typedef long long ll;

bool is_ordered(ll n) {
    ll nd = n%10;
    n /= 10;
    while (n) {
        ll d = n % 10;
        if (d > nd) return false;
        nd = d;
        n /= 10;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    unsigned t; cin >> t;
    for (unsigned i = 1; i <= t; ++i) {
        ll n; cin >> n;
        while (!is_ordered(n)) {--n;}
        cout << "Case #" << i << ": " << n << '\n';
    }
    return 0;
}
