#include <bits/stdc++.h>
using namespace std;
pair<long long int,long long int> solve(long long int n,long long int k){
	if(k==1) return {n/2,(n-1)/2};
	if(n%2) return solve(n/2,k/2);
	else if(k%2) return solve((n-1)/2,k/2);
	else return solve(n/2,k/2);
}
int main(){
	long long int t,k,tc=1,i,j,f,n;
	for(cin>>t;tc<=t;++tc){
		cin>>n>>k;
		pair<long long int, long long int> ans=solve(n,k);
		cout<<"Case #"<<tc<<": "<<ans.first<<" "<<ans.second<<'\n';
	}
}