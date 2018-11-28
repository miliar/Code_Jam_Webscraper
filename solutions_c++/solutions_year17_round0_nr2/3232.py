#include <cstdio>
#include <cstring>

typedef long long int Long;

int t, len, i, dig[30];
Long ans;

int isTidy() {
	for(int i = 1; i < len; ++i)
		if(dig[i-1] < dig[i])
			return 0;
	return 1; 
}

int main() {
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		scanf("%lld", &ans);
		len = 0;
		while(ans) {
			dig[len++] = ans % 10;
			ans /= 10;
		}
		
		while( !isTidy() ) {
			i = 0;
			while(i < len && dig[i] == 9) ++i;
			while(i < len) {
				dig[i] = 9;
				if(dig[i + 1]) {
					--dig[i + 1];
					break;
				} else {
					++i;
				}
			}
		}
		
		while(len--) {
			ans = ans * 10 + dig[len];
		}
		printf("Case #%d: %lld\n", tc, ans);
	}
	
	return 0;
}
