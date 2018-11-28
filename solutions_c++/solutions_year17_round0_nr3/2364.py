#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
int main(){
	ll n,k,aa,bb;
	int t;
	cin>>t;
	int cse=1;
	while(t--){
		cout<<"Case #"<<cse++<<": ";
		cin>>n>>k;
		ll a=1LL;
		ll b=0LL;
		ll s=1LL;
		ll ant=1LL;
		ll antn=n;
		ll av=n;
		ll bv=0;
		for(ll p=2LL;;p*=2LL){
			
		    if(k<p)break;
			if(n&1LL){
				aa=(a*2LL)+b;
				bb=b;
			}else{
				aa=a;
				bb=a+(b*2LL);
			}
			a=aa;
			b=bb;
			av=n/2LL;
			bv=av-1LL;
			n/=2LL;
			ant=p;
		}
		k-=ant;
		//cout<<k<<endl;
		//cout<<av<<" "<<bv<<endl;
		if(k<a){
			cout<<av/2LL<<" "<<(av-1LL)/2LL<<"\n";
		}else{
			cout<<bv/2LL<<" "<<(bv-1LL)/2LL<<"\n";
		}
	}
	return 0;
}
