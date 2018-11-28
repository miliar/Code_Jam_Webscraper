#include <bits/stdc++.h>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mkp make_pair
#define bgn begin()
#define end end()
#define all(x) x.bgn,x.end
#define itr(x) x::iterator
#define fst first
#define scd second
#define dlt pop()

using namespace std;

typedef long long int ll;
typedef vector<int> vint;
typedef vector<ll> vlong;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef map<int,int> mii;
typedef map<ll,ll> mll;
typedef queue<int> qint;
typedef queue<ll> qlong;
typedef stack<int> sint;
typedef stack<ll> slong;
typedef queue<pii> qpii;
typedef stack<pii> spii;
typedef vector<pii> vpii;

int mod = 1e9+7;
int NN = 1e6+7;

ll gcd(ll a, ll b){
	return b==0 ? a : gcd(b,a%b);
}

// (1/b)%a where gcd(a,b)=1
ll invmod(ll a, ll b){
	ll x=0, y=1, r, q, m=a;
	while(b){
		r=a%b;
		q=a/b;
		a=b;
		b=r;
		r=x;
		x=y;
		y=r-q*y;
	}
	return (x+m)%m;
}

int small(vector<vector<pair<int,int> > > rng){
	if(rng[0].empty()) return 0;
	if(rng[1].empty()) return 0;
	int lc=max(rng[0][0].fst,rng[1][0].fst);
	int rc=min(rng[0][0].scd,rng[1][0].scd);
	if(rc-lc>=0 && rc>0){
		rng[0].erase(rng[0].begin());
		rng[1].erase(rng[1].begin());
		return small(rng)+1;
	}
	vector<vector<pair<int,int> > > trng;
	for(int i=0; i<2; i++){
		trng.push_back(rng[i]);
	}

	trng[0].erase(trng[0].begin());
	rng[1].erase(rng[1].begin());
	return max(small(trng),small(rng));
}

int main(){
	int t;
	cin>>t;
	for(int z=1; z<=t; z++){
		int n, p;
		cin>>n>>p;
		vint rg(n), pg[n];
		for(int i=0; i<n; i++) cin>>rg[i];
		for(int i=0; i<n; i++){
			pg[i]=vint(p);
			for(int j=0; j<p; j++){
				cin>>pg[i][j];
			}
			sort(pg[i].begin(),pg[i].end);
		}

		vector<vector<pair<int,int> > > rng(n);
		for(int i=0; i<n; i++){
			for(int j=0; j<p; j++){
				int r1=110*rg[i], r2=90*rg[i];
				int q1=(pg[i][j]*100)/r1, rm1=(pg[i][j]*100)%r1;
				int q2=(pg[i][j]*100)/r2, rm2=(pg[i][j]*100)%r2;
				int l=q1+(rm1>0), r=q2;
				if(l<=r) rng[i].push_back(make_pair(l,r));
			}
		}

		int ans=0;
		if(n==1){
			for(int i=0; i<rng[0].size(); i++){
				if(rng[0][i].scd>0) ans++;
			}
		}
		else if(n==2){
			ans=small(rng);
		}
		else ans=-1;

		cout<<"Case #"<<z<<": "<<ans<<endl;
	}
}

		/*int ans=0;
		for(int i=0; i<p; i++){
			bool f=false;
			for(int j=0; j<n; j++){
				if(rng[j].empty()){
					f=true;
					break;
				}
			}
			if(f){
				break;
			}
			
			int lc=0, rc=10000000;
			for(int b=0; b<n; b++){
				lc=max(lc,rng[b][i].fst);
				rc=min(rc,rng[b][i].scd);
			}

			if(rc-lc>=0){
				for(int j=0; j<n; j++){
					rng[j].erase(rng[j].begin());
				}
			}
			else{
				int i=-1;
				int nf=10000000;

			}
		}*/