#include <bits/stdc++.h>
using namespace std;
const int N = 20 + 5;
int T, Case;
map<long long,long long> cnt;
long long n, k;

int main() {
    freopen("out3.txt","w",stdout);
    freopen("C-large.in","r",stdin);
    scanf("%d", &T);
    while(T--) {
        scanf("%lld%lld", &n, &k); k--;
        cnt.clear();
        cnt[n] = 1;
        while(k > 0) {
            auto p = *cnt.rbegin();
            long long x = min(k, p.second);
            k -= x;
            if((cnt[p.first] -= x) == 0) cnt.erase(p.first);
            if(p.first&1) {
                cnt[p.first/2] += x*2;
            }else {
                cnt[p.first/2] += x;
                cnt[p.first/2-1] += x;
            }
        }
        auto p = cnt.rbegin();
        long long mi, mx;
        if(p->first&1) mi = mx = p->first/2;
        else mi = p->first/2-1, mx = p->first/2;
        printf("Case #%d: %lld %lld\n", ++Case, mx, mi);
    }
    return 0;
}
