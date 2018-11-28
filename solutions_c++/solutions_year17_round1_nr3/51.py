#include<stdio.h>
#include<algorithm>
#include<cmath>
#define ce(a,b) (((a)/(b)) + ((a)%(b)?1:0))
using namespace std;

typedef long long lld;
lld Hd, Ad, Hk, Ak, B, D;

lld noDebuf(lld hp, lld K){
	lld x=0, turn, a, b;
	for(x=0;; x++){
		if(ce(Hk, Ad+x*B) == ce(Hk, Ad+(x+1)*B))break;
	}
	turn = x + ce(Hk, Ad+x*B);
	if(K == 0)return turn;

	a = (hp-1)/K, b = (Hd-1)/K-1;
	if(b <= 0) return -1;
	if(turn <= a+1) return turn;
	turn -= a;
	if((turn-1) % b == 0) return a+1 + turn+((turn-1)/b)-1;
	else if(turn % b == 0) return a+1 + turn+(turn/b)-1;
	return a+1 + turn+(turn/b);
}

void test(int tn){
	scanf("%lld%lld%lld%lld%lld%lld", &Hd, &Ad, &Hk, &Ak, &B, &D);
	if(Ad >= Hk){ printf("Case #%d: 1\n", tn); return; }
	if(Ak < Hd && (Ad*2 >= Hk || Ad+B >= Hk)){ printf("Case #%d: 2\n", tn); return; }
	if(2*Ak - 3*D >= Hd){ printf("Case #%d: IMPOSSIBLE\n", tn); return; }

	lld mi = noDebuf(Hd, Ak);
	if(D){
		lld turn=0, hp=Hd;
		while(Ak > 0){
			turn++; Ak -= D;
			if(Ak < 0)Ak = 0;
			hp -= Ak;
			lld gap = noDebuf(hp, Ak);
			if(gap != -1){
				if(mi == -1 || mi > gap+turn)mi = gap+turn;
			}
			if(hp <= Ak - D) turn++, hp = Hd - Ak;
		}
	}
	if(mi == -1) printf("Case #%d: IMPOSSIBLE\n", tn);
	else printf("Case #%d: %lld\n", tn, mi);
}

int main(){
	int i, tn;
	freopen("C-small-attempt0.in","r",stdin); freopen("output.txt","w",stdout);
	scanf("%d", &tn);
	for(int i=1; i<=tn; i++)test(i);
	return 0;
}
