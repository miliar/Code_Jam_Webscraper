#include <bits/stdc++.h>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it)
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define ROF(i,n) for (ll i = ((ll)n-1); i >= 0; i--)
#define FOR1(i,n) for (ll i = 1; i < ll(n); i++)
#define READ(a) int a; 0 == scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(_i,n){ 0 == scanf("%d", &v[_i]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
const double PI = std::atan(1.0)*4;
#define cpx complex<double>
#define MOD 1000000007ll
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#define MAXN 1000

int myh, mya, hish, hisa, b, d;


int ttl(int ttk, int debuffs){
	int h=myh;
	int a=hisa;
	int t = 0;
	while(true){
		t++;
		if(debuffs){
			if(h<=a-d) {h=myh; goto pass;}
			a-=d;
			debuffs--;
			goto pass;
		}
		if(h<=a && ttk!=1){h=myh; goto pass;}
		if(ttk){
			ttk--;
			if(!ttk) return t;
			goto pass;
		}
		break;
		pass: h-=a;
		if(t>MAXN) return t;
	}
	return t;
}

int solve(int buffs, int debuffs){
	ll mya2 = mya + buffs*b;
	ll ttk=buffs + (hish + mya2 -1)/mya2;
	// cout<<ttk<<endl;
	int t = ttl(ttk, debuffs);
	if(t>MAXN) return -1;
	return t;
}


int main(int argc, char *argv[]){
	READ(T);
	FOR(t, T){
		cin>>myh>>mya>>hish>>hisa>>b>>d;

		ll m = -1;
		// if(myh-2*hisa+3*d<=0 && (mya){
		// 	cout<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl;
		// 	goto next;
		// }

		FOR(i,101) FOR(j, 101){
			ll r = solve(i,j);
			// cout<<i<<" "<<j<<" "<<r<<endl;
			if(r!=-1 && (m==-1 || r<m)){m=r;}
		}
		if(m==-1){
			cout<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<"Case #"<<(t+1)<<": "<<m<<endl;
		}
		next: continue;
	}
	return 0;
}