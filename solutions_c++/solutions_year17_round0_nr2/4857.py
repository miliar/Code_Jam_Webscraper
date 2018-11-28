#include <iostream>
#include <cstdio>
using namespace std;
int array[20];
int main() {
	int tc,cant;
	unsigned long num; 
	cin>>tc;
	for(int i=1;i<=tc;i++){
		scanf("%lu\n",&num);
		int dig=0;
		while(num>0){
			array[dig++]=int (num%10);
			num/=10;
		}
		//for(int j=dig-1;j>=0;j--) printf("%d",array[j]);
		//printf("\n");
		int ind,top=0;
		for(ind=dig-1;ind>top;ind--){
			//printf("ind: %d\n",ind);
			if(array[ind]>array[ind-1]){
				if(array[ind]==0) array[ind]=9;
				else array[ind]--;
				top=ind-1;
				for(int j=ind-1;j>=0;j--) array[j]=9;
				ind+=2;
			}
			if(ind>dig) break;
		}
		printf("Case #%d: ",i);
		if (array[dig-1]!=0) printf("%d",array[dig-1]);
		for(int j=dig-2;j>=0;j--) printf("%d",array[j]);
		printf("\n");
	}
	return 0;
}