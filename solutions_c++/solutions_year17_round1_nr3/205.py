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
ll H,A,h,a,B,D;
ll AN;
ll inf = 1e10;
ll prod(ll x,ll y){
	if(inf/x<y) return inf;
	return x*y;
}
ll f(ll x,ll t){return prod(A+x*B,t-x);}
bool canA(ll t){
	if(B==0) return A*t>=h;
	rep(i,3){
		ll x;
		if(i==0) x=0;
		if(i==1) x=(B*t-A)/(2*B);
		if(i==2) x=(B*t-A)/(2*B)+1;
		if(!(0<=x&&x<=t)) continue;
		if(f(x,t)>=h) return 1;
	}
	return 0;
}
void calcAN(){
	ll ub = 1LL<<30, lb = 0;
	while(ub-lb>1){
		ll m = (ub+lb)/2;
		if(canA(m)) ub=m;
		else lb=m;
	}
	AN = ub;
}
bool can(ll t){
	if(t<AN) return 0;
	//endure t-1 times
	rep(d,101){
		ll nowH=H,nowa=a;
		ll an=0;
		ll dn=0;
		rep(i,t){
			if(an+1==AN) return 1;
			if(dn!=d && nowH>(nowa-D)){
				dn++;
				nowa-=D;
				if(nowa<0) nowa=0;
			}else if(nowH<=nowa){
				nowH=H;
			}else{
				an++;
				if(an==AN){
					return 1;
				}
			}
			nowH-=nowa;
		}
	}
	return 0;
}
void solve(){
	cin>>H>>A>>h>>a>>B>>D;
	calcAN();
//	show(AN);
	ll ub = 300, lb = 0;
//	show(can(5));
	while(ub-lb>1){
		ll m = (ub+lb)/2;
		if(can(m)) ub=m;
		else lb=m;
	}
	if(ub == (300)){
		puts("IMPOSSIBLE");
		return;
	}
	cout<<ub<<endl;
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: ",t);
		solve();
	}
}
