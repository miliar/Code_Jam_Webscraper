#include<bits/stdc++.h>
bool isTidy(long long x){
	int tmp = x % 10;
	while(x/10 > 0){
		if (tmp < (x/10)%10){
			return false;
		}
		x/=10;
		tmp = x%10;
	}
	return true;
}
int main() {
	long long in,ans = 1 << 18,cmp = 1 << 17;
	int T;
	scanf("%d", &T);
	for (int tT = 1 ; tT <= T ; tT++) {
		scanf("%lld", &in);
		while(!isTidy(in--)){
			
		}

		printf("Case #%d: %lld\n",tT,in+1);
	}

}