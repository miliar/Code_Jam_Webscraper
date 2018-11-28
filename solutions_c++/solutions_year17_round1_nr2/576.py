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
typedef long long ll;
typedef pair<ll,ll> pll;
typedef priority_queue<pll,vector<pll>,greater<pll> > heap;
//macro
#define SZ(x) ((ll)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define L first
#define R second
#define mkp make_pair
#define pb push_back
const ll INF=4e18;
const ll MAX=1e6+5;
const ll MOD=1e9+7;
//}}}
int n,p;
int box[60];
pii q[60][60];
int s[60];
int dfs(int now,int l,int r){
	if(now==n)	return 1;
	for(int i=s[now];i<p;i++){
		if(q[now][i].L<=q[now][i].R)
			if(l<=q[now][i].L&&q[now][i].L<=r||q[now][i].L<=l&&l<=q[now][i].R){
				if( dfs(  now+1  ,  max(l,q[now][i].L)  ,  min(r,q[now][i].R)  ) ){
					s[now]=i+1;
					return 1;
				}
			}
	}
	return 0;
	
}
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("input.in","r",stdin);
	freopen("answer.out","w",stdout);
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		cin>>n>>p;
		for(int i=0;i<n;i++)
			cin>>box[i];
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				int x;
				cin>>x; x*=10;
				int l=x/11/box[i];
				int r=x/9 /box[i];
				if(l*box[i]*11>=x)	l--;
				l++;
				q[i][j]={l,r};
//				debug(l,r);
			}
			sort(q[i],q[i]+p);
		}
		for(int i=0;i<n;i++)
			s[i]=0;
		int cnt=0;
		for(int i=0;i<p;i++){
			if(q[0][i].L<=q[0][i].R)
				cnt+=dfs(1,q[0][i].L,q[0][i].R);
		}
		cout<<"Case #"<<t<<": ";
		cout<<cnt<< '\n';
	}
	return 0;
}

