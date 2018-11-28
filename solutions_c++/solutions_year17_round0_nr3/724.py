#include<stdio.h>
#include<map>
using namespace std;
int main() {
    int ca;
    scanf("%d", &ca);
    for (int cas = 1; cas <= ca; cas++) {
        long long n, k;
        scanf("%lld%lld", &n, &k);
        map<long long, long long> mp;
        mp[n] = 1;
        while (true) {
            long long s = mp.rbegin()->first - 1;
            long long ct = mp.rbegin()->second;
            mp.erase(--mp.end());
            if (ct >= k) {
                printf("Case #%d: %lld %lld\n", cas, (s + 1) / 2, s / 2);
                break;
            } else {
                k -= ct;
                mp[(s + 1) / 2] += ct;
                mp[s / 2] += ct;
            }
        }
    }
}
