#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define FOR(i,l,r) for(int i=(l);i<(r);++i)
#define REP(i,a) FOR(i,0,a)
#define all(c) begin(c), end(c)
#define uniquenize(v) (v).erase(unique(all(v)), end(v))
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
const int maxn=1e5+1;
template<class T> inline void maxi(T &a,T b) { if (a<b) a=b; }

LL n,k;
LL solmax(LL d) {
	return d/2;
}
LL solmin(LL d) {
	return (d-1)/2;
}
int main() {
	int T; scanf("%d",&T);
	for (int tt=1;tt<=T;++tt) {
		printf("Case #%d: ",tt);

		scanf("%lld%lld",&n,&k);
		LL a=n,gs[2]={1,0},tgs[2];
		while (1) {
			if (k<=gs[0]+gs[1]) {
				if (k<=gs[1]) {
					printf("%lld %lld\n",solmax(a+1),solmin(a+1));
				}
				else {
					printf("%lld %lld\n",solmax(a),solmin(a));
				}
				break;
			}
			k-=gs[0]+gs[1];
			if (a&1) {
				tgs[0]=gs[0]*2+gs[1];
				tgs[1]=gs[1];
			}
			else {
				tgs[0]=gs[0];
				tgs[1]=gs[0]+gs[1]*2;
			}
			gs[0]=tgs[0]; gs[1]=tgs[1];
			a=(a-1)/2;
		}
	}
	return 0;
}

