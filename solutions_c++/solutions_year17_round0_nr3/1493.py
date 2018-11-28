#include<bits/stdc++.h>
using namespace std;

int TCs, TC;
long long int N, K;
long long int i, x, y, L, baseN, added, slots;


int main(){
	scanf("%d", &TCs);
	for (TC=1; TC<=TCs; TC++){
		printf("Case #%d: ", TC);
		scanf("%lld%lld", &N, &K);
		
		baseN = N;
		added = 0;
		slots = 1;
		while(K>slots){
//printf("tmp: %7lld %7lld %7lld\n", baseN, added, slots);
			K -= slots;
			if (!(baseN&1)) added += slots;
			slots *= 2;
			baseN = (baseN-1)/2;
		}
//printf("tmp: %7lld %7lld %7lld\n", baseN, added, slots);
		
		if (K<=added) baseN++;
		printf("%lld %lld\n", baseN/2, (baseN-1)/2);
		
	}
	
	return 0;
}


