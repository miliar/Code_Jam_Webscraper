#include<bits/stdc++.h>
using namespace std;
int main(){

	int t,i,j,k,p,x,arr[20];
	long long n;
	scanf("%d",&t);
	for(p=1 ; p<=t ;p++){
		scanf("%lld",&n);
		x = 0;
        while(n){
			arr[++x] = n%10;
			n/=10;
        }
        for(i=2 ; i<=x ;i++){
			if(arr[i] > arr[i-1]){
				arr[i]--;
				for(j=1 ;j<i ;j++)
					arr[j] = 9;
			}
        }
        reverse(arr+1, arr+x+1);
        i = 1;
        if(arr[1] == 0)
			i = 2;
		printf("Case #%d: ",p);
		for( ;i<=x ;i++)
			printf("%d",arr[i]);
		printf("\n");
	}
	return 0;
}
