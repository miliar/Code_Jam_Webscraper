#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

struct Node{
	long long r,h;
}P[1010],P2[1010],tmpN;

bool cmp(Node a, Node b){
	if(a.r == b.r) return a.h > b.h;
	return a.r > b.r;
}

bool cmp2(Node a, Node b){
	return a.r*a.h > b.r*b.h;
}

int main(){
	int T;
	int N,K;
	int cs;
	long long Maxr;
	long long ans,tt;
	long long a[1010],b[1010];
	scanf("%d",&T);
	for(int i=1;i<=T;++i){
		ans = 0;
		scanf("%d %d",&N,&K);
		for(int j=0;j<N;++j){
			scanf("%lld %lld",&P[j].r,&P[j].h);
		}

		for(int j=0;j<N;++j){
			Maxr = 0;
			for(int k=0;k<N;++k){
				P2[k].r = P[k].r;
				P2[k].h = P[k].h;
			}
			tmpN.r = P2[0].r;
			tmpN.h = P2[0].h;
			P2[0].r = P2[j].r;
			P2[0].h = P2[j].h;
			P2[j].r = tmpN.r;
			P2[j].h = tmpN.h;

			sort(P2+1,P2+N,cmp2);

			Maxr += P2[0].r * P2[0].r;

			for(int k=0;k<K;++k)
				Maxr += P2[k].r * P2[k].h * 2;
			
			if(Maxr > ans) ans = Maxr;
		}
		
/*
		a[0] = Maxr = 0;

		sort(P,P+N,cmp2);

		for(int j=0;j<K;++j){
			a[0] += P[j].r * P[j].h * 2;
			if(P[j].r > Maxr) Maxr = P[j].r;
		}
		b[0] = Maxr;
		for(int j=1;j<=N-K;++j){
			a[j] = a[j-1] - P[j-1].r * P[j-1].h * 2 + P[j-1+K].r * P[j-1+K].h * 2;
			Maxr = 0;
			for(int h=0;h<K;++h){
				if(P[j+h].r > Maxr) Maxr = P[j+h].r;
			}
			b[j] = Maxr;
		}

		Maxr = 0;
		for(int j=0;j<=N-K;++j){
			a[j] += b[j]*b[j];
			if(a[j] > Maxr) Maxr = a[j];
		}

		ans = Maxr;
*/
/*
		sort(P,P+N,cmp);

		ans += P[0].r * P[0].r;
		ans += P[0].r * P[0].h * 2;

		sort(P+1,P+N,cmp2);

		for(int j=1;j<K;++j)
			ans += P[j].r * P[j].h * 2;

		cs = 1;

		while(true){
			if(cs == N) break;
			tt = 0;
			sort(P+cs,P+N,cmp);
			
			tt += P[cs].r * P[cs].r;
			tt += P[cs].r * P[cs].h * 2;
			
			++cs;

			sort(P+cs,P+N,cmp2);

			for(int j=cs;j<K+cs-1;++j)
				tt += P[j].r * P[j].h * 2;

			if(tt > ans)
				ans = tt;
			else
				break;
		}
*/

		printf("Case #%d: %.9lf\n",i,(double)ans*acos(-1));
	}
	return 0;
}
