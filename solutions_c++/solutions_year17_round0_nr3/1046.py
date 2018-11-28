#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;

#define MAX_N 1005

int T;
ll N,K;
ll p[63];

inline void precal(){
	p[0]=1LL;
	for(int i=1;i<63;++i){
		p[i]=p[i-1]<<1;
		//printf("%lld\n",p[i]);
	}
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("ansC3.txt","w",stdout);

	scanf("%d",&T);
	precal();

	for(int ts=1;ts<=T;++ts){
		scanf("%lld%lld",&N,&K);

		ll accul=0LL;
		int k=-1;
		for(int i=0;i<63;++i){
			accul+=p[i];
			k=i;
			if(accul>=K){
				accul-=p[i];
				k=i-1; // last
				break;
			}
		}
		//printf("k=%d, accul=%lld\n",k,accul);

		ll xk=N-accul; // stalls left
		ll k2=p[k+1]; // 2^(k+1) intervals

		//printf("k2=%lld, accul=%lld\n",p[k+1],accul);

		ll every_interval_length=xk/k2;
		ll remain_length=xk%k2;

		if(K-accul<=remain_length){
			every_interval_length++;
		}

		every_interval_length--; // insert new people
		//printf("%lld\n",every_interval_length);
		ll MX,MN;
		if(every_interval_length%2LL==1LL){// ODD
			//puts("jizz");
			MN=every_interval_length>>1;
			MX=MN+1LL;
		}
		else { // EVEN
			MX=MN=every_interval_length>>1;
			//MN=MX-1LL;
		}
		printf("Case #%d: %lld %lld\n",ts,MX,MN);
	}


	fclose(stdin);
	fclose(stdout);

	return 0;
}
