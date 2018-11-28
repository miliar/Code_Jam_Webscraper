#include<bits/stdc++.h>

#define fname "B-large"
#define pb push_back
#define mp make_pair
#define ss second
#define fff first

using namespace std;

typedef long double ld;
typedef long long ll;
const int maxn = (1e5) + 10;
const int INF = (1e9);
const ll inf = (1e18);
const double eps = (1e-9);
const ld PI = acos(-1);
ll n;
int t,f,ff;
vector< ll > v;
int main() {    

	ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen(fname".in", "r", stdin);
	freopen(fname".out", "w", stdout);
	cin>>t;
	for(int tt=1;tt<=t;++tt){
		cin>>n;
		v.clear();
		f=0;
		ff=0;
		cout<<"Case #"<<tt<<": ";
		while(n>0){
			v.pb(n%10);
			n/=10;
		}
		reverse(v.begin(),v.end());
		while(true){
			ff=0;
			for(int i=0;i<v.size()-1;++i){
				if(v[i]>v[i+1]){
					if(v[i]==1){
						f=1;
						break;
					}else{
						v[i]--;
						for(int j=i+1;j<v.size();++j)
						v[j]=9;	
					}
				}
			}
			if(f){
				for(int i=0;i<v.size()-1;++i)
				cout<<"9";
				break;
			}else{
				for(int i=0;i<v.size()-1;++i)
				if(v[i]>v[i+1]){
					ff=1;
					break;
				}
				if(!ff){
					for(int i=0;i<v.size();++i)
					cout<<v[i];
					break;
				}
			}
		}
		cout<<"\n";
	}
	return 0;
}


