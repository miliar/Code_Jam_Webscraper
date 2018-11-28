#include <stdio.h>
#include <map>
using namespace std;
map<long long, int> mp;
int main() {
    int t, cas = 0;
    long long a, b;
    scanf("%d", &t);
    while (t--) {
        cas++;
        scanf("%lld %lld", &a, &b);
        mp.clear();
        mp[a] = 1;
        while(true) {
            map<long long, int>::iterator it = mp.end();
            it--;
            long long t1 = it->first;
            long long t2 = it->second;
            mp.erase(it);
            if (t2 >= b) {
                printf("Case #%d: %lld %lld\n", cas, t1 / 2, (t1 - 1) / 2);
                break;
            }
            b -= t2;
            mp[(t1 - 1) / 2] += t2;
            mp[t1 / 2] += t2;
        }
    }
}
