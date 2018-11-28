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
ll N,K;
typedef pair<ll,ll> P;
map<ll,ll> cnt;
priority_queue<ll> que;
void solve(){
	cnt.clear();
	while(!que.empty()) que.pop();
	cin>>N>>K;
	cnt[N]=1;
	que.push(N);
	while(K){
		ll L = que.top(), n = cnt[L];
		que.pop();
		if(K<=n){
			cout<<L/2<<" "<<(L-1)/2<<endl;
			return;
		}
		K-=n;
		rep(t,2){
			ll nL=(L-t)/2;
			if(cnt.count(nL)){
				cnt[nL]+=n;
			}else{
				cnt[nL]+=n;
				que.push(nL);
			}
		}
	}
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: ",t);
		solve();
	}
}
