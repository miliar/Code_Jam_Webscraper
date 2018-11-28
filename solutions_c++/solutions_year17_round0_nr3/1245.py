#include <bits/stdc++.h>
using namespace std;
#define k first
#define v second

int main(){
	
	int test,t;
	long long ansmax,ansmin,n,k;
	map<long long, long long> ctr;
	scanf("%d",&test);
	
	for( t=0 ; t<test ; printf("Case #%d: %lld %lld\n",++t,ansmax,ansmin) ){
		scanf("%lld%lld",&n,&k);
		
		ctr.clear();
		ctr[n]++;
		
		for( auto i=ctr.rbegin() ; i!=ctr.rend() ; i++ ){
//			printf("%lld %lld left: %lld\n",i->k,i->v,k);
			ansmax = (i->k)/2;
			ansmin = ansmax - ((i->k&1) == 0);
			
			ctr[ansmax] += i->v;
			ctr[ansmin] += i->v;
			if( k <= i->v ) break;
			else k-=i->v;
		}	
	}
	return 0;
}

