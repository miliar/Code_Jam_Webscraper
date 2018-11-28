#include<bits/stdc++.h>

using namespace std;

long long int slove(long long int n,long long int k){
	long long int m=0,l;
	long long int x=0,y=1;
	while(x<k){
		y*=2;
		x=x+y;
	};
	x=x-y;
	m=(n-(y-1))%y;
	l=(n-(y-1))/y;
	if(!m){
		return l;
	}
	if(x+m<k){
		return l;
	} else return l+1;
}

main(){
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int i,T;
	long long int N,K,ans;
	cin>>T;
	for(i=0;i<T;i++){
		cin>>N>>K;
	ans=slove(N,K-1);
		cout<<"Case #"<<i+1<<": "<<ans/2<<" ";
		if (ans%2){
			cout<<ans/2<<endl;
		} else cout<<max((long long int)0,ans/2-1)<<endl;
		
	}
}
