#include <iostream>
#define ll long long
using namespace std;

int main () {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        ll n, k; cin >> n >> k;
        ll ht = 1, pow = 1;
        while (pow < k) {
            ht++;
            pow = 2*pow+1;
        }
        ll sum = n-(pow/2);
        ll num = 1<<(ht-1);
        ll low = sum/num;
        ll num_high = sum-low*num;
        ll sz;
        if (k-(pow/2) <= num_high) sz = low;
        else sz = low-1;
        ll a, b;
        if (sz == 0) {
            a = b = 0;
        }
        else {
            a = (sz-1)/2+1; b = sz/2;
        }
        cout << "Case #" << t << ": " << a << " " << b << '\n';
    }
    return 0;
}