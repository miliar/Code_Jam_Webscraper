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
int N,M;
int a[4];
int solve(){
	rep(i,4) a[i]=0;
	cin>>N>>M;
	rep(i,N){
		int x;
		cin>>x;
		x%=M;
		a[x]++;
	}
	if(M==2){
		return a[0] + (a[1]+1)/2;
	}
	if(M==3){
		int sum = a[1] + 2*a[2];
		int res = a[0];
		int mn = min(a[1],a[2]);
		res += mn;
		a[1] -= mn;
		a[2] -= mn;
		res += a[1]/3;
		res += a[2]/3;
		if(sum%3!=0) res++;
		return res; 
	}
	if(M==4){
		int sum = a[1] + 2*a[2] + 3*a[3];
		int res = a[0];
		res += a[2]/2;
		a[2]%=2;
		int mn = min(a[1],a[3]);
		res += mn;
		a[1] -= mn;
		a[3] -= mn;
		res += a[1]/4;
		a[1]%=4;
		res += a[3]/4;
		a[3]%=4;
		if(a[1]+a[3]>=2 && a[2]==1) res++;
		if(sum%4!=0) res++;
		return res;
	}
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: %d\n",t,solve());
	}
}
