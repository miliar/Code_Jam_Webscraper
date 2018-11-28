#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;

map<LL, LL> mp;

int main() {
    int T, kase = 0; scanf("%d",&T);
    while (T--) {
        mp.clear();
        LL n, k; scanf("%lld%lld",&n,&k);
        mp[n] = 1;
        map<LL, LL>::iterator it;
        LL temp = k - 1;
        while (temp) {
            it = --mp.end();
            LL cnt = min(temp, it->second), size = it->first;
            (it->second) -= cnt;
            if (it->second == 0) {
                mp.erase(it);
            }
            if (size % 2) mp[size>>1] += cnt * 2;
            else {
                mp[size>>1] += cnt;
                if (size > 2) mp[(size>>1) - 1] += cnt;
            }
            temp -= cnt;
        }
        it = --mp.end();
        LL size = it->first;
        printf("Case #%d: ",++kase);
        if (size % 2) {
            printf("%lld %lld\n",size>>1,size>>1);
        }
        else {
            printf("%lld %lld\n",size>>1,(size>>1)-1);
        }
    }
    return 0;
}
