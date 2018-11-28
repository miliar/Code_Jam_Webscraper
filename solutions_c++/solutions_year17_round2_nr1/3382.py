#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen("A.INP","r",stdin);
	freopen("A.OUT","w",stdout);
	int t,N,D,K,S;
	double ans=100000000000000000000000,tmp;
	cin>>t;
	for(int i=0;i<t;i++){
		ans=10000000000000000000000;
		cin>>D>>N;
		for(int j=0;j<N;j++){
			cin>>K>>S;
			tmp=(double)((double)(D/((double)(D-K)/S)));
			ans=min(ans,tmp);
		}
		printf("Case #%d: %lf\n",i+1,ans);
	}
	return 0;
}
