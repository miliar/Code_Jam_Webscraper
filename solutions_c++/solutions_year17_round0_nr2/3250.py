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
ll d[30];
ll l;
ll dr[30];
void init(ll x){
	l=0;
	while(x){
		d[l]=x%10LL;
		x/=10LL;
		l++;
	}
}
int main(){SYNC
	int T;
	cin>>T;
	repn(tc,T){
		cout<<"Case #"<<tc<<": ";
		ll n;
		cin>>n;
		init(n);
		ll ans=0;
		int max=-1;
		for(int i=0;i<l-1;i++){
			if(d[i]<d[i+1]){
				max=i;
			}
		}
		if(max==-1){
			cout<<n<<"\n";
			continue;
		}
		while(max<(l-2) && d[max+2]==d[max+1]){
			max++;
		}
		d[max+1]--;
		if(d[l-1]){
			cout<<d[l-1];
		}
		for(int i=l-2;i>max;i--){
			cout<<d[i];
		}
		for(int i=0;i<=max;i++){
			cout<<"9";
		}
		cout<<"\n";
	}
	return 0;
}