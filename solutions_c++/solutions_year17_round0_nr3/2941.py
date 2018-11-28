#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	int i,j,t,T;ll n,k,p,ans1,ans2;
	cin>>T;
	for (t=0;t<T;t++){
	    cin>>n>>k;
		map<ll,ll> M;
		M[n]=1;M[-1]=0;
		p=0;
		while(1){
			if (p+((--M.end())->second)>=k) break;
			ll u=(--M.end())->first, v=(--M.end())->second;
			M.erase(--M.end());
			p+=v;
		    if (u&1){
				M[u/2]+=v;
				M[u/2]+=v;
			}
			else {
				M[u/2]+=v;
				M[u/2-1]+=v;
			}
		}
		ll u=(--M.end())->first; 
		if (u&1) ans1=u/2,ans2=u/2;
		else ans1=u/2,ans2=u/2-1;
		cout<<"Case #"<<t+1<<": "<<ans1<<" "<<ans2<<"\n";
	}
	return 0;
}
