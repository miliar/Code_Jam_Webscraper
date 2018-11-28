#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long 
bool tidy(int n){
	int prev=n%10;
	n=n/10;
	int next;
	while(n>0){
		next=n%10;
		if(next>prev) return false;
		n=n/10;
		prev=next;
	}	
	return true;
} 
int main(){
	int t,n;
	
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		
		scanf("%d",&n);
		
		for(int j=n;j>0;j--){
		if(tidy(j)){
			printf("Case #%d: %d\n",i,j);
			break;
		}
	}

		
		
	}
	return 0;
}