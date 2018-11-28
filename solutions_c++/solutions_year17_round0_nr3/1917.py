#include<bits/stdc++.h>
using namespace std;
long long dfs(long long n,long long k){
	if(k==1)	return n;
	if(n&1)		return dfs(n>>1,k>>1);
	if(k&1)		return dfs((n-1)>>1,k>>1);
	return dfs(n>>1,k>>1);
}
int main(){
	int T;
	cin>>T;
	for(int i=1;i<=T;i++){
		long long n,k;
		cin>>n>>k;
		cout<<"Case #"<<i<<": ";
		long long A=dfs(n,k);
		cout<<A/2<<" "<<(A-1)/2<<endl;
	}
}
