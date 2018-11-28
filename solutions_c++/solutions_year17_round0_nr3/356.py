#include <cstdio>
using namespace std;

int main(){
	int cases;
	scanf("%d", &cases);
	
	long long n, k;
	for(int z=1; z<=cases; z++){
		scanf("%lld %lld", &n, &k);
		
		while(k > 1){
			k--;
			if(n%2 == 0){
				if(k%2 == 0){
					n = n/2 - 1;
				}else{
					n = n/2;
				}
			}else{
				n /= 2;
			}
			k = (k+1)/2;
		}
		printf("Case #%d: %lld %lld\n", z, n/2, (n-1)/2);
	}

	return 0;
}