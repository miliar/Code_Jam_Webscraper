#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
	int t;ll k,n,r,l,m;
	cin>>t;
	for(int T=1;T<=t;T++){
		cout<<"Case #"<<T<<": ";
		cin>>n>>k;
		l=0LL;r=n-1;
		while(k>1){
			m=(l+r)/2;
			if(k%2==0){
				l=m+1;
			}else{
				r=m-1;
			}
			k=k/2;
		}
		m=(l+r)/2;
		cout<<max(r-m,m-l)<<" "<<min(r-m,m-l)<<endl;
	}
	return 0;
}
