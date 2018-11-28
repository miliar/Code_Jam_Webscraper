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
int N,C,M;
int a[1001];
int n[1001];
void solve(){
	cin>>N>>C>>M;
	rep(i,1001) a[i]=0,n[i]=0;
	rep(i,M){
		int p,b;
		cin>>p>>b;
		p--,b--;
		a[p]++;
		n[b]++;
	}
	int mx = 0;
	rep(i,C) chmax(mx,n[i]);
	int sm = 0;
	rep(i,N){
		sm+=a[i];
		int tmp = (sm+i)/(i+1);
		chmax(mx,tmp);
	}
	int sum = 0;
	rep(i,N){
		sum += max(0,a[i]-mx);
	}
	cout<<mx<<" "<<sum<<endl;
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: ",t);
		solve();
	}
}
