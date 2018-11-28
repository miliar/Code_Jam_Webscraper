#include <bits/stdc++.h>
#define LL long long
#define INF 0x3f3f3f3f
#define VI vector<int>
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
using namespace std;
int main(){
	int t;
	LL n, k;
	scanf("%d", &t);
	for(int c = 1; c <= t; c++){
		scanf("%lld %lld", &n, &k);
		printf("Case #%d: ", c);
		LL f = n;
		LL s = 1, p = n;
		while(true){
			LL L = s, R = min(n, 2LL*s - 1LL);
			//printf("%lld %lld\n", L, R);
			if(k >= L && k <= R){
				if(R == n) printf("0 0\n");
				else{
					LL x = f + s - p*s;
					//printf("%lld\n", x);
					k -= (L-1LL);
					if(k > x) p--;
					printf("%lld %lld\n", ((p-1)/2LL) + (bool)((p-1)%2LL), (p-1)/2LL);
				}
				break;
			}
			p = (p-1)/2LL + (bool)((p-1)%2LL);
			f -= s;
			s <<= 1LL;
		}
	} 
	return 0;

}