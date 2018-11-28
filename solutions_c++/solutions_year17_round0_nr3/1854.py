#include <bits/stdc++.h>

#define ll long long int

using namespace std;

bool v[1024];
map<ll, ll> M;
map<ll, ll>::iterator Mi;
ll T, C=1, n, k;

int main() {

    for (scanf("%lld",&T);T--;) {
        printf("Case #%lld: ",C++);
        scanf("%lld %lld",&n,&k);
        M.clear();
        M[n] = 1;
        while (1) {
            Mi = M.end(); Mi--;
            if (k <= Mi->second) break;
            k -= Mi->second;
            ll qnts = Mi->second;
            ll tbloco = Mi->first;
            M.erase(Mi);
            if (tbloco%2==0) {
                M[tbloco/2] = M[tbloco/2] + qnts;
                M[tbloco/2-1] = M[tbloco/2-1] + qnts;
            } else
                M[tbloco/2] = M[tbloco/2] + 2*qnts;
        }
        ll we = Mi->first, a, b;
        if (we%2==0) {
            a = we/2; b = we/2 - 1;
        } else {
            a = b = we/2;
        }
        printf("%lld %lld\n",a,b);
    }

    return 0;

}
