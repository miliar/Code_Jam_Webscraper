#include<bits/stdc++.h>

#define fname "C-small-1-attempt0"
#define pb push_back
#define mp make_pair
#define ss second
#define ff first

using namespace std;

typedef long double ld;
typedef long long ll;
const int maxn = (2e6) + 10;
const int INF = (1e9);
const ll inf = (1e18);
const double eps = (1e-9);
const ld PI = acos(-1);
int n,k,t,u[maxn],l,r,al,ar;
int main() {    

	ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen(fname".in", "r", stdin);
	freopen(fname".out", "w", stdout);
	cin>>t;
	for(int tt=1;tt<=t;++tt){
		cin>>n>>k;
		for(int i=1;i<=n;++i)
		u[i]=0;
		cout<<"Case #"<<tt<<": ";
		for(int j=1;j<=k;++j){
		ar=0;
		al=1;
		l=1;
		r=0;
		for(int i=1;i<=n;++i){
			if(u[i]){
				if(r-l+1>ar-al+1){
					ar=r;
					al=l;
				}
				l=i+1;
				r=i+1;
			}else
			r=i;
		}
		if(l<=n&&r<=n&&r-l+1>ar-al+1){
			ar=r;
			al=l;
		}
	//	cout<<al<<" "<<ar<<"\n";
		if((ar-al+1)%2==0){
		 //   if(u[al+(ar-al+1)/2-1])
		   // cout<<j<<"\n";
			u[al+(ar-al+1)/2-1]=1;
		}
		else{
			u[al+(ar-al+1)/2]=1;
		}
		}
		if((ar-al+1)%2==0){
			cout<<(ar-al+1)/2<<" "<<(ar-al+1)/2 - 1;
			u[al+(ar-al+1)/2-1]=1;
		}
		else{
			cout<<(ar-al+1)/2<<" "<<(ar-al+1)/2;
			u[al+(ar-al+1)/2]=1;
		}
		cout<<"\n";
	}
	return 0;
}





