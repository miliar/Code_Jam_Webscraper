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
typedef priority_queue<pll> heap;
//macro
#define SZ(x) ((ll)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define F first
#define S second
#define mkp make_pair
#define pb push_back
const ll INF=4e18;
const ll MAX=1e6+5;
const ll MOD=1e9+7;
//}}}
string s;
heap pq;
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("input.in","r",stdin);
	freopen("answer.out","w",stdout); 
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		ll n,k;
		cin>>n>>k;
		pq.push({n,-1});
		for(int i=0;i<k-1;i++){
			pii now=pq.top();
			now.S=-now.S;
			pq.pop();
			int s=( (now.F-1)>>1 )+now.S;
			if(now.F>>1)
				pq.push({now.F>>1,-(s+1) });
			if((now.F-1)>>1)
				pq.push({(now.F-1)>>1,-now.S });
		}
		cout<<"Case #"<<t<<": ";
		pii now=pq.top();
		cout<< (now.F>>1) << ' '<<((now.F-1)>>1)<< '\n';
		while(SZ(pq))
			pq.pop();
	}
	return 0;
}

