#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<math.h>

using namespace std;
int main(){
	int T, logk;
	long long n, k, p;

  	freopen ("C-large.in","r",stdin);
  	freopen("C-large-output", "w", stdout);

//Getting number of times
	scanf("%d", &T);

//For each input
	for(int t=1;t<=T;t++){
		cin >> n >> k;

		printf("Case #%d: ", t);	

		p = 1;
		logk=1;
		while(p*2 <= k){
			p*=2;
			logk++;
		}
		k-=p;
		
		for(int i=0; i<logk-1; i++){
			if(k%2 == 0)
				n = n/2;
			else
				n = (n-1)/2;
			k/=2;
		}
		
		printf("%lld %lld", n/2, (n-1)/2);
		
		printf("\n");		
	}
	
	return 0;
}