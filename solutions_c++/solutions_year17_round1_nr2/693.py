#include <bits/stdc++.h>
using namespace std;
typedef long long				ll;
typedef pair<int,int >			pii;
#define V						vector
#define SYNC					ios_base::sync_with_stdio(0);cin.tie(0);
#define rep(i,b)				for(int i=0;i<b;i++)
#define repn(i,n)				for(int i=1;i<=n;i++)
#define ALL(x)					(x).begin(),(x).end()
#define fi						first
#define se						second
#define pb						push_back
#define dzx						cerr<<"here";
const ll MOD=1e9+7,INF=9e18;
const int inf=2e8;
/* cent π */
int r[100];
long double lr[100];
long double rr[100];
multiset<long double> a[50];
int main(){SYNC
	int T;
	cin>>T;
	repn(tc,T){
		cout<<"Case #"<<tc<<": ";
		int n,p;
		cin>>n>>p;
		rep(i,50){
			a[i].clear();
		}
		rep(i,n){
			cin>>r[i];
			lr[i]=(long double)r[i]*(long double)9/(long double)10;
			rr[i]=(long double)r[i]*((long double)11/(long double)10);
		}
		rep(i,n){
			rep(j,p){
				int temp;
				cin>>temp;
				a[i].insert((long double)temp/(long double)r[i]);
			}
		}
		int ans=0;
		int max=inf;
		for(int i=0;i<n;i++){
			max=min(max,(int)ceil((long double)1e6/lr[i]));
		}
		/*for(int k=1;k<=max;k++){
			int to=inf;
			for(int i=0;i<n;i++){
				int c=0;
				auto itl=a[i].lower_bound((long double)k*((long double)9/(long double)10));
				auto itr=a[i].upper_bound((long double)k*((long double)11/(long double)10));
				while(itl!=itr){
					itl++;
					c++;
				}
				to=min(c,to);
				if(to==0){
					break;
				}
			}
			ans+=to;
			if(to){
				for(int i=0;i<n;i++){
					int c=0;
					auto itl=a[i].lower_bound((long double)k*((long double)9/(long double)10));
					auto cur=itl;
					while(c!=to){
						itl++;
						a[i].erase(cur);
						cur=itl;
						c++;
					}
				}
			}
		}*/
		while(a[0].size()!=0){
			auto it=a[0].begin();
			auto temp=it;
			int l=ceil((*it)*((long double)10/(long double)11));
			int r=floor((*it)*((long double)10/(long double)9));	
			for(int k=l;k<=r;k++){
				int to=inf;
				for(int i=0;i<n;i++){
					int c=0;
					auto itl=a[i].lower_bound((long double)k*((long double)9/(long double)10));
					auto itr=a[i].upper_bound((long double)k*((long double)11/(long double)10));
					while(itl!=itr){
						itl++;
						c++;
					}
					to=min(c,to);
					if(to==0){
						break;
					}
				}
				ans+=to;
				if(to){
					for(int i=0;i<n;i++){
						int c=0;
						auto itl=a[i].lower_bound((long double)k*((long double)9/(long double)10));
						auto cur=itl;
						while(c!=to){
							itl++;
							a[i].erase(cur);
							cur=itl;
							c++;
						}
					}
				}
			}
			if(a[0].begin()==temp){
				a[0].erase(temp);
			}
		}
		cout<<ans<<"\n";
	}
	return 0;
}