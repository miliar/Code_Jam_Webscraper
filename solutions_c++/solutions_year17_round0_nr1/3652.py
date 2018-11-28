//Name     : Hemant Mangla
//Username : hkmangla
//College  : DCRUST Murthal
//Country  : India

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define IN(s) freopen(s,"r",stdin)
#define OUT(s) freopen(s,"w",stdout)
#define pll pair<ll,ll>
#define pii pair<int,int>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define MEM(a,x) memset(a,x,sizeof(a))
#define foreach( gg,itit )  for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;

ll power(ll x,ll y){
  ll t=1;
  while(y>0){
    if(y%2) y-=1,t=t*x%mod;
    else y/=2,x=x*x%mod;
  }
  return t;
}
char flip(char a){
	if(a=='-') return '+';
	else return '-';
}
int main(){
	IN("input.txt");
	OUT("output.txt");
	int t; cin>>t; 
	REPP(tt,1,t+1){
		cout<<"Case #"<<tt<<": ";
		int k,n; string s;
		cin>>s>>k;
		n = s.length();
		int ans=0;
		REP(i,n-k+1){
			if(s[i] == '-'){
				ans ++;
				REPP(j,i,i+k) s[j] = flip(s[j]);
			}
		}
		bool flag = false;
		REPP(i,n-k+1,n) if(s[i] == '-') flag = true;
		if(flag) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
  return 0;
}
