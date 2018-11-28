#include<iostream>
#include<cstdio>
using namespace std;
typedef long long ll;

int main(){
	int t;
	ll k, n;
	scanf("%d", &t);
	for(int tcase=1;tcase<=t;tcase++){
		printf("Case #%d: ", tcase);
		scanf("%I64d %I64d", &n, &k);
		n++;
		int log=0;
		while(k>>log!=1){
			log++;
		}
		ll rmd, quo;
		quo=n>>log;
		rmd=n-((n>>log)<<log);
		printf("%I64d %I64d\n", (quo+(k-(1<<log)+1<=rmd))/2+(quo+(k-(1<<log)+1<=rmd))%2-1, (quo+(k-(1<<log)+1<=rmd))/2-1);	
	}
	return 0;
}
