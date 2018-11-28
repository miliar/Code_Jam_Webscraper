#include <bits/stdc++.h>

const long long MAX = 1000000000000000000LL;

int main(){
	
	int test,t,j,len,i;
	char n[30];
	long long ans;
	scanf("%d",&test);
	
	for( t=0 ; t<test ; printf("Case #%d: %lld\n",++t,ans) ){
		scanf("%s",n);
		do{
			j=0;
			for( i=1 ; n[i] ; i++ ){
				if( n[i] < n[i-1] ){
					n[i-1]--;
					n[i] = '9';
					for( j=i+1 ; n[j] ; j++ ) n[j]='9';	
					j = 1;
				}
			}
		}while(j);
		ans = atoll(n);
	}
	return 0;
}

