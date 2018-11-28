#include <bits/stdc++.h>
using namespace std;
//debug
#ifdef grief
#define debug(...) do{\
	fprintf(stderr , "%s - %d : (%s) = " , __PRETTY_FUNCTION__ , __LINE__ , #__VA_ARGS__ );\
	_DO(__VA_ARGS__);\
}while(0)
template<typename I> void _DO(I&&x){
	cerr<<x<<endl;
}
template<typename I,typename...T> void _DO(I&&x,T&&...tail){
	cerr<<x<<" , ";
	_DO(tail...);
}
#else
#define debug(...)
#endif
//type
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef priority_queue<pll,vector<pll>,greater<pll> > heap;
//macro
#define SZ(x) ((ll)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define F first
#define S second
#define mkp make_pair
#define pb push_back
#define IOS do{ios_base::sync_with_stdio(0); cin.tie(0);}while(0)
const ll INF=4e18;
const ll MAX=1e5+5;
const ll MOD=1e9+7;
//}}}
int n,p;
int cc[10];
int main(){
	//IOS;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		cin>>n>>p;
		for(int i=0;i<p;i++)	cc[i]=0;
		for(int i=0;i<n;i++){
			int x; cin>>x;	x%=p;
			cc[x]++;
		}
		int ans=cc[0];
//		debug(ans);
		for(int i=1;i<p;i++){
			int x;
			if(i!=p-i)	x=min(cc[i],cc[p-i]);
			else		x=cc[i]/2;
			ans+=x;
			cc[i]-=x; cc[p-i]-=x;
		}
//		debug(ans);
		if(p==4){
			int all=0;
			for(int j=0;j<cc[1];j++){
				if(cc[2]&&(all+2)%p==0){
					cc[2]--; all+=2;
				}
				if(all%p==0)	ans++;
					all+=1;
			}
			for(int j=0;j<cc[3];j++){
				if(cc[2]&&(all+2)%p==0){
					cc[2]--; all+=2;
				}
				if(all%p==0)	ans++;
					all+=3;
			}
			for(int j=0;j<cc[2];j++){
				if(all%p==0)	ans++;
					all+=2;
			}
		}
		else{
			int all=0;
			for(int i=1;i<p;i++){
				for(int j=0;j<cc[i];j++){
					if(all%p==0)	ans++;
					all+=i;
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}

