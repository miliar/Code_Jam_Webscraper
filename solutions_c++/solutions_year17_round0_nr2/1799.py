#include <bits/stdc++.h>

#define ll long long int

using namespace std;

ll T, C=1;

ll mtidy(ll num) {
        ll v[32];
        ll onum = num;
        ll n=0;
        while (onum > 0) {
            v[n++] = onum%10ll;
            onum /= 10ll;
        }
        reverse(v,v+n);
        ll q=-1ll;
        for (ll i=0;i+1<n;i++)
            if (v[i] > v[i+1]) {
                q = i;
                break;
            }
        if (q==-1ll)
            return num;
        num=0;
        for (ll i=0;i<=q;i++)
            num = 10ll*num + v[i];
        num--;
        num = mtidy(num);
        for (ll i=q+1;i<n;i++) {
            num = 10ll*num + 9ll;
        }
        return num;
}

int main() {

    for(scanf("%lld",&T);T--;) {
        printf("Case #%lld: ",C++);
        ll num;
        scanf("%lld",&num);
        printf("%lld\n",mtidy(num));
    }

    return 0;
}
