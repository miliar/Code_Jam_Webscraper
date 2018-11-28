#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int T;
ll n, k;

int main(){
	scanf("%d\n", &T);
	for(int c=1; c<=T; c++){
		scanf("%lld %lld", &n, &k);
		ll pot = 1;		
		while(pot-1 < k){
			pot*=2LL;
		}	
		ll num = pot/2;
		n -= (num-1);
		k -= (num-1);
		ll mirow = n/num;
		ll marow = mirow+1;
		ll qntma = n%num;
		printf("Case #%d: ", c);
		if(k<=qntma){
			if(marow%2) printf("%lld %lld\n", marow/2, marow/2);
			else printf("%lld %lld\n", marow/2, (marow-2)/2);
		}
		else{
			if(mirow%2) printf("%lld %lld\n", mirow/2, mirow/2);
			else printf("%lld %lld\n", mirow/2, (mirow-2)/2);
		}
	}
	return 0;
}
