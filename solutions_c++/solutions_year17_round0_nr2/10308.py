#include <bits/stdc++.h>

using namespace std;

bool tidy(int a, int b){
	if(b==0) return true;
	else if(a>=b%10)return tidy(b%10,b/10);
	else return false;	
}

int main(){
	int t, n;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&n);
		while(tidy(n%10,n/10)!=true) n--;
		printf("Case #%d: %d\n",i,n);
	}
	return 0;
}
