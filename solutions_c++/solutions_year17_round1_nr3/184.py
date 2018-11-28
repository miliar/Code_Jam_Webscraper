#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;

const int mod=1000000000+7;

int addm(int& a,int b) {return (a+=b)<mod?a:a-=mod;}

template<class T,class U> bool smin(T& a,U b) {return a>b?(a=b,1):0;}
template<class T,class U> bool smax(T& a,U b) {return a<b?(a=b,1):0;}

const int maxn=100;
ll T,Hd,Ad,Hk,Ak,B,D;

ll ssmall(ll Hd,ll Hdc,ll Ad,ll Hk,ll Ak,ll B,ll D,ll nd,ll nb) {
	ll r=0;
	while (r<1000) {
		if (nd>0) {
			ll nAk=max(0ll,Ak-D);
			if (nAk>=Hdc) Hdc=Hd;
			else Ak=nAk,nd--;
		}
		else if (nb>0) {
			if (Ak>=Hdc) Hdc=Hd;
			else Ad+=B,nb--;
		}
		else {
			if (Ad>=Hk) return r+1;
			if (Ak>=Hdc) Hdc=Hd;
			else Hk-=Ad;
		}
		Hdc-=Ak;
		if (Hdc<=0) return LLONG_MAX;
		r++;
	}

	return LLONG_MAX;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		ll r=LLONG_MAX;
		for (int nd=0;nd<=100;nd++) for (int nb=0;nb<=100;nb++) 
			r=min(r,ssmall(Hd,Hd,Ad,Hk,Ak,B,D,nd,nb));
		cout << "Case #" << cas << ": ";
		if (r==LLONG_MAX) cout << "IMPOSSIBLE\n";
		else cout << r << '\n';
	}
}
