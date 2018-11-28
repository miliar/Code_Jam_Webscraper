#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
template<class S,class T> ostream& operator<<(ostream& o,const pair<S,T> &p){return o<<"("<<p.fs<<","<<p.sc<<")";}
template<class T> ostream& operator<<(ostream& o,const vector<T> &vc){o<<"sz = "<<vc.size()<<endl<<"[";for(const T& v:vc) o<<v<<",";o<<"]";return o;}

typedef long long ll;
int N,P;
ll a[50];
ll b[50][50];
int it[50];

bool toosmall(ll x,ll tar){
	return x*10<tar*9;
}
bool toolarge(ll x,ll tar){
	return x*10>tar*11;
}
int solve(){
	cin>>N>>P;
	rep(i,N) cin>>a[i];
	rep(i,N){
		rep(j,P) cin>>b[i][j];
		sort(b[i],b[i]+P);
	}
	int ans=0;

	rep(i,N) it[i]=0;
	rep1(n,1000000){
		bool ok=1;
		rep(i,N){
			ll tar=a[i]*n;
			while(it[i]<P && toosmall(b[i][it[i]],tar)) it[i]++;
			if(it[i]==P) return ans;
			if(toolarge(b[i][it[i]],tar)){
				ok=0;
				continue;
			}
		}
		if(ok){
			ans++;
			rep(i,N){
				it[i]++;
				if(it[i]==P) return ans;
			}
			n--;
		}
	}
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: %d\n",t,solve());
	}
}
