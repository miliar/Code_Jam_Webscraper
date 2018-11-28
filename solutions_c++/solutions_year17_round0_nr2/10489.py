#include<cstdio>

using namespace std;

int main(){
	freopen ("B-small-attempt0.in", "r", stdin);
    freopen ("B-small-attempt0.out", "w", stdout);
	int t,n,x1,x,flag=0;
	scanf("%d",&t);
	for(int i=0 ; i<t ; i++){
		scanf("%d",&n);
		x1=n;
		while(1){
			x=x1;
			flag=0;
			while(x>9){
				if(x%10<(x/10)%10){
					flag=1;
					break;
				}
				x/=10;
			}
			if(flag==0){
				printf("Case #%d: %d\n",i+1,x1);
				break;
			}
			x1--;
		}
	}
}
