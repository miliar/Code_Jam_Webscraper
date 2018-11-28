#include<cstdio>
using namespace std;
typedef long long ll;
ll t,n,k;
int main() {
    scanf("%lld", &t);
    for(int i=1;i<=t;i++) {
        scanf("%lld%lld", &n, &k);
        ll mx, mn;
        if(k == 1) mx = n / 2, mn = (n - 1) / 2;
        else {
            ll p = k, lev_k = 0;
            while(p) p /= 2, lev_k++;
            ll a = n / 2, b = (n - 1) / 2;
            ll s = 1, pow = 2;
            ll na = 1, nb = 1, ta, tb;
            for(ll j=3;j<=lev_k;j++) {
                if(a % 2 == 0 && b % 2 == 0) {
                    ta = na + nb;
                    tb = na + nb;
                } else if(a % 2 == 1 && b % 2 == 0) {
                    ta = 2 * na + nb;
                    tb = nb;
                } else if(a % 2 == 0 && b % 2 == 1) {
                    ta = na;
                    tb = na + 2 * nb;
                } else {
                    ta = 2 * na;
                    tb = 2 * nb;
                }
                na = ta, nb = tb;
                a /= 2, b = b ? (b - 1) / 2 : 0;
                s += pow, pow *= 2;
            }
            if(a == b) mx = a / 2, mn = a ? (a - 1) / 2 : 0;
            else {
                ll rem = k - s;
                if(rem <= na) mx = a / 2, mn = a ? (a - 1) / 2 : 0;
                else mx = b / 2, mn = b ? (b - 1) / 2 : 0;
            }
        }
        printf("Case #%d: %lld %lld\n", i, mx, mn);
    }
    return 0;
}
