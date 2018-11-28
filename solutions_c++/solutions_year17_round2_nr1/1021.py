#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll T, D, N, K[1010], S[1010];

int main(){
	scanf("%lld", &T);
	for(int cas=1; cas<=T; cas++){
		scanf("%lld %lld", &D, &N);			
		for(int i=0; i<N; i++){
			scanf("%lld %lld", &K[i], &S[i]);
		}
		ll max_ = 0, idx = N-1;
		for(int i=N-2; i>=0; i--){
			if( (D-K[i])*(S[idx]) > (D-K[idx])*(S[i]) ){
				idx = i;
			}
		}
		printf("Case #%d: %.15lf\n", cas, (1.0*D)/((1.0*D-K[idx])/S[idx]) );
	}
	return 0;
}
