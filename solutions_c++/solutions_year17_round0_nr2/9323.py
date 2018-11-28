#include <cstdio>

int main(){
	int t,n;
	int ans[101];
	scanf("%d", &t);
	for(int z=1;z<=t;z++){
		scanf("%d", &n);
		while(1){
			int tmp=n;
			bool flag=true;
			while(tmp){
				if((tmp/10)%10>tmp%10){
					n--;
					tmp=n;
					flag=false;
					break;
				}
				else tmp/=10;
			}
			if(flag){
				ans[z]=n;
				break;
			}
		}
	}
	for(int z=1;z<=t;z++){
		printf("Case #%d: %d\n", z,ans[z]);
	}
	return 0;
}
