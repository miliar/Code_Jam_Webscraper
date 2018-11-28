#include <stdio.h>

bool is_tidy(long long a){
	if(a%10 == 0) return false;
	int arr[20] = {0,};
	for(int i=0; a>0; i++){
		if(a%10==0) return false;
		arr[i]=a%10;
		a /= 10;
	}
	for(int j=0; arr[j]!=0; j++) if(arr[j]<arr[j+1]) return false;
	return true;
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=1; i<=n; i++){
		long long x;
		scanf("%lld", &x);
		for(long long j=x; j>0; j--){
			if(is_tidy(j)){
				printf("Case #%d: %lld\n",i,j);
				break;
			}
		}
	}	
	return 0;
}
