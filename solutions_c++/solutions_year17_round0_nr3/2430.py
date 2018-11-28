#include <iostream>
#include <map>
using namespace std;

typedef long long ll;

int main() {
    int T;
    cin >> T;  
    for (int t = 1; t <= T; t++) {
        ll n, k;
        cin >> n >> k;
        map<ll, ll> mp;
        mp[n] = 1;
        ll rc = 0;
        while (true) {
            ll x = mp.rbegin()->first;
            ll c = mp.rbegin()->second;
            mp.erase(x);
            x--;
            ll a = (x % 2 == 0 ? x / 2 : x / 2 + 1);
            ll b = (x / 2);
            mp[a] += c;
            mp[b] += c;
            rc += c;
            if (rc >= k) {
                cout << "Case #" << t << ": " << a << " " << b << endl;
                break;
            }
        }    
    }
    return 0;
}