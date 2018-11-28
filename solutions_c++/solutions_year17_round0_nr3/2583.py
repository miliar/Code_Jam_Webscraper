#include <cstdio>
#include <queue>
#include <map>
using namespace std;

typedef long long ll;

ll n, k;
int T, Case = 1;
map<ll, ll> s;

int main()
{
    scanf("%d", &T);
    while(T--) {
        s.clear();
        printf("Case #%d: ", Case++);
        scanf("%lld%lld", &n, &k);
        s[n] = 1;
        ll i = n;
        while(1) {
            ll m = s[i], l = (i-1) / 2, r = i - l - 1;
            s.erase(i);
            k -= m;
            //55printf("k=%d\n", k);
            if(k <= 0) {
                printf("%lld %lld\n", r, l);
                break;
            }
            if(l == r && l != 0)
                s[l] += m + m;
            else{
                if(l != 0)
                    s[l] += m;
                if(r != 0)
                    s[r] += m;
            } 
            i = s.rbegin()->first;
        }
    }
    return 0;
}