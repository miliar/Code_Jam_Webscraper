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
#define F first
#define S second
#define mkp make_pair
#define pb push_back
const ll INF=4e18;
const ll MAX=1e6+5;
const ll MOD=1e9+7;
//}}}
string s;
int k;
int che(){
	int si=SZ(s);
	int ans=0;
	for(int i=0;i<=si-k;i++){
		if(s[i]=='-'){
			ans++;
			for(int j=i;j<i+k;j++){
				s[j]= s[j]=='+' ? '-' : '+';
			}
		}
	}
	for(int i=si-k+1;i<si;i++)
		if(s[i]=='-')	return -1;
	return ans;
}
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("input.in","r",stdin);
	freopen("answer.out","w",stdout); 
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		cin>>s;
		cin>>k;
		int ans=che();
		cout<<"Case #"<<t<<": ";
		if(ans<0)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<ans<< '\n';
	}
	return 0;
}

