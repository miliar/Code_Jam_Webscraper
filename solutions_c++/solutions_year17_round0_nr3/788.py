#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
#define LL long long

LL n,k;
priority_queue<LL> pq;
map<LL,LL> mp;

int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
        scanf("%lld%lld",&n,&k);
        mp.clear();
        while (!pq.empty()) pq.pop();

        mp[n] = 1;
        pq.push(n);
        LL now,cnt;
        while (!pq.empty()) {
            now = pq.top();
            cnt = mp[now];
            pq.pop();
            k -= cnt;
            if (k <= 0) break;

            LL a = now/2;
            if (mp.find(a) != mp.end()) {
                mp[a] += cnt;
            }
            else {
                mp[a] = cnt;
                pq.push(a);
            }

            a = (now-1)/2;
            if (mp.find(a) != mp.end()) {
                mp[a] += cnt;
            }
            else {
                mp[a] = cnt;
                pq.push(a);
            }
        }
        printf("Case #%d: %lld %lld\n",t,now/2,(now-1)/2);
    }
	return 0;
}
