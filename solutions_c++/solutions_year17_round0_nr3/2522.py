#include <bits/stdc++.h>

#define ll long long
#define M 1000000007
#define INF 9223372036854775807
#define mp(x, y) make_pair(x,y)
#define pb(x) push_back(x)
#define pmp(x, y) pb(mp(x,y))
#define ld double
#define PI 3.14159265
#define len(a) (ll)a.size()    //
#define F first
#define S second
#define endl "\n"
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;
ll one = 1;

int main() {

    ll t;
    cin >> t;
    for (ll i = 0; i < t; i++) {
        ll k, n, l, r;
        cin >> n >> k;
        ll cnt = (one << 62);
        while (cnt != 0) {
            if (k & cnt)
                break;
            cnt /= 2;
        }
        ll leftover = k - (cnt - 1);
        ll rg = n - (cnt - 1);
        ll div = rg / (cnt);
        ll rem = rg % (cnt);
        if (rem < leftover)
            div--;
        r = div / 2;
        l = div - r;
        cout << "Case #" << i + 1 << ": " << l << " " << r << endl;
    }
    return 0;
}