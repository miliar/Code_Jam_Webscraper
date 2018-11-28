#include<cstdio>
#include<map>
using namespace std;

int main() {
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++) {
        printf("Case #%d: ", casen);
        long long n, k, ansx = -1, ansy = -1;
        scanf("%lld %lld", &n, &k);
        map<long long, long long> mp;
        mp[n] = 1;
        while(k > 0) {
            long long len = mp.rbegin() -> first;
            long long cnt = mp.rbegin() -> second;
            mp.erase(len);
            k -= cnt;
            ansx = len / 2, ansy = (len - 1) / 2;
            mp[ansx] += cnt;
            mp[ansy] += cnt;
        }
        printf("%lld %lld\n", ansx, ansy);
    }
    return 0;
}
