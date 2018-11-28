#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

map<ll,map<pair<ll,ll>,ll> > z; // (-min(ls,rs),-max(ls,rs))
ll n,k;

void doit(ll n){
	if(z.count(n))return;
	ll k0=(n-1)/2,k1=k0;
	if((n-1)%2)k1++;
	doit(k0);doit(k1);
	map<pair<ll,ll>,ll>& w0=z[k0];
	map<pair<ll,ll>,ll>& w1=z[k1];
	map<pair<ll,ll>,ll> r;
	for(auto p:w0)r[p.fst]+=p.snd;
	for(auto p:w1)r[p.fst]+=p.snd;
	r[mp(-k0,-k1)]++;
	z[n]=r;
}

int main(){
	int tn;z[0];z[1][mp(0,0)]=1;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		scanf("%lld%lld",&n,&k);k--;
		doit(n);
		map<pair<ll,ll>,ll>& w=z[n];
		ll r0=-1,r1=-1;
		for(auto p:w){
			k-=p.snd;
			if(k<0){
				r1=-p.fst.fst;
				r0=-p.fst.snd;
				break;
			}
		}
		assert(r0>=0&&r1>=0);
		printf("%lld %lld\n",r0,r1);
	}
	return 0;
}

