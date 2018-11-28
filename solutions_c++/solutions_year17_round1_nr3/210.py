#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int INFTY=1000000000;
typedef long long ll;
enum {DEBUFF, BUFF, ATTACK, CURE};

ll hd, ad, hk, ak, b, d;

ll result(int nd, int nb) {
	ll chd=hd, cad=ad, chk=hk, cak=ak, turn;
	int la=DEBUFF;
	for(turn=1; ; turn++) {
		if(cad>=chk) {
			//printf(">%d%d%lld\n", nd, nb, turn);
			return turn;
		}
		if((nd==0 && chd<=cak) || (chd<=cak-d)) {
			if(la==CURE) return INFTY;
			la=CURE;
			chd=hd;
			chd-=cak;
			if(chd<=0) return INFTY;
			continue;
		}
		if(nd>0) {
			cak=max(cak-d, 0LL);
			nd--;
			chd-=cak;
			if(chd<=0) return INFTY;
			la=DEBUFF;
			continue;
		}
		if(nb>0) {
			cad+=b;
			nb--;
			chd-=cak;
			if(chd<=0) return INFTY;
			la=BUFF;
			continue;
		}
		if(nd==0 && nb==0) {
			chk-=cad;
			if(chk<=0) {
				//printf(">%d%d%lld\n", nd, nb, turn);
				return turn;
			}
			chd-=cak;
			if(chd<=0) return INFTY;
			la=ATTACK;
			continue;
		}
	}
	return 0;
}

ll solve() {
	int nd, nb, maxd, maxb;
	scanf("%lld%lld%lld%lld%lld%lld", &hd, &ad, &hk, &ak, &b, &d);
	if(ad>=hk) return 1;
	if(d==0) maxd=0; else maxd=(ak+d-1)/d;
	if(b==0) maxb=0; else maxb=(hk-ad)/b+1;
	ll ans=INFTY;
	for(nd=0; nd<=maxd; nd++) for(nb=0; nb<=maxb; nb++)
		ans=min(ans, result(nd, nb));
	return ans;
}


int main() {
	int icase, ncase;
	ll ans;
	scanf("%d", &ncase);
	for(icase=1; icase<=ncase; icase++) {
		ans=solve();
		if(ans==INFTY) printf("Case #%d: IMPOSSIBLE\n", icase);
		else printf("Case #%d: %lld\n", icase, ans);
	}
	return 0;
}

//48 1 35 26 4 2