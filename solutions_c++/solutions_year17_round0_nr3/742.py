#include<bits/stdc++.h>
using namespace std;

long long n, m;

long long target;
long long gae[2];

int main(){
	int turn;
	scanf("%d",&turn);
	for(int t = 1; t <= turn;t++){
		scanf("%lld %lld",&n,&m);
		long long ans = 0;
		target = n; gae[0]= 1; gae[1] = 0;
		while(1){
			if(m <= gae[0]){
				ans = target;
				break;
			}else if(m <= gae[0] + gae[1]){
				ans = target-1;
				break;
			}
			m -= (gae[0] + gae[1]);
			if(target%2){
				gae[0] = gae[0] * 2 + gae[1];
			}else{
				gae[1] = gae[1] * 2 + gae[0];
			}
			target = target / 2;
		}
		printf("Case #%d: %lld %lld\n", t, ans/2, (ans-1)/2);
	}
}
