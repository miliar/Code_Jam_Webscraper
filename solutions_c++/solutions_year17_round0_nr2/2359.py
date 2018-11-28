#include <bits/stdc++.h>
using namespace std;
typedef long long lli;

vector <lli> V;

int A[20];

int red(int i){
	int res=9;
	for(int j=i-1;j>=0;j--){
		if(A[j]>A[i]) return(0);
		if(A[j]<A[i]) return(1);
	}
	return(0);
}

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		lli x;
		scanf("%lld",&x);
		for(int i=0;i<20;i++){
			A[i]=x%10;
			x/=10;
		}
		for(int i=19;i>=0;i--){
			if(red(i) ){
				A[i]--;
				for(int j=i-1;j>=0;j--){
					A[j]=9;
				}
				break;
			}
		}
		lli res=0,m=1;
		for(int i=0;i<20;i++){
			res+=m*A[i];
			m*=10;
		}
		printf("Case #%d: %lld\n",t,res);
	}
}