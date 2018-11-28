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
vector<int> digit;
int numDigit(ll n){
	int ans = 0;
	while(n!=0){
		ans ++;
		digit.pb(n%10);
		n = n/10;
	}
	reverse(all(digit));
	return ans;
}
ll makeNo(ll lastNo, int a,int n){
	while(n--){
		lastNo = lastNo*10 + a;
	}
	return lastNo;
}
int main(){
	 IN("input.txt");
	 OUT("output.txt");
	int t; cin>>t; 
	REPP(tt,1,t+1){
		int n,k; cin>>n>>k;
		priority_queue<int> Q;
		Q.push(n);
		int ls = 0,rs = 0;
		while(k--){
			int a = Q.top();
			Q.pop();
			if(a%2){
				ls = rs = a/2;
			}
			else{
				ls = a/2 - 1;
				rs = a/2;
			}
			Q.push(ls);
			Q.push(rs);
		}
		cout<<"Case #"<<tt<<": ";
		cout<<rs<<" "<<ls<<endl;
	}
  return 0;
}
