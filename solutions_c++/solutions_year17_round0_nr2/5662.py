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
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("input.in","r",stdin);
	freopen("answer.out","w",stdout); 
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		cin>>s;
		for(int i=SZ(s)-1;i>0;i--){
			if(s[i]<s[i-1]){
				for(int j=i;j<SZ(s);j++)
					s[j]='9';
				s[i-1]--;
			}
		}
		cout<<"Case #"<<t<<": ";
		bool noo=0;
		for(int i=0;i<SZ(s);i++){
			if(s[i]>'0'||noo){
				cout<<s[i];
				noo=1;
			}
		}
		cout<< '\n';
	}
	return 0;
}

