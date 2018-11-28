#include <cstdio>
using namespace std;

int main(){
	int cases;
	scanf("%d", &cases);

	long long n;
	for(int z=1; z<=cases; z++){
		scanf("%lld", &n);
		
		int num[18];
		for(int i=0; i<18; i++){
			num[i] = n%10;
			n /= 10;
		}
		
		for(int i=0; i<17; i++){
			if(num[i] < num[i+1]){
				num[i+1]--;
				for(int j=i; j>=0; j--){
					num[j] = 9;
				}
			}
		}
		
		printf("Case #%d: ", z);
		bool zero = true;
		for(int i=17; i>=0; i--){
			if(num[i] != 0){
				zero = false;
				printf("%d", num[i]);
			}else{
				if(!zero){
					printf("%d", num[i]);
				}
			}
		}
		printf("\n");
	}
	
	return 0;
}