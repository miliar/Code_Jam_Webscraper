#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
typedef pair<int, int>          pii;
#define V			 vector
#define SYNC		 ios_base::sync_with_stdio(0);cin.tie(0); 
#define rep(i,b)     for(int i=0;i<b;i++)
#define repn(i,n) 	 for(int i=1;i<=n;i++)
#define ALL(x)  	 (x).begin(), (x).end()
#define fi           first
#define se           second
#define pb 		     push_back
#define dzx 		 cerr<<"here";
const ll MOD=1e9+7,INF=1e18;
const int inf=1e8;
/* cent π */
map<ll,ll> fre;
int main(){SYNC
	int T;
	cin>>T;
	repn(tc,T){
		cout<<"Case #"<<tc<<": ";
		int n,k;
		ll mx=-inf,mn=inf;
		cin>>n>>k;
		fre.clear();
		fre[n]=1;
		while(k){
			auto it=fre.rbegin();
			if((*it).se >=k ){
				mx=((*it).fi)/2;
				mn=((*it).fi-1)/2;
				break;
			}
			k-=(*it).se;
			ll f=0;
			fre[(*it).fi/2]+=(*it).se;
			fre[((*it).fi-1)/2]+=(*it).se;
			fre.erase((*it).fi);
		}
		cout<<mx<<" "<<mn;
		cout<<"\n";
	}
	return 0;
}