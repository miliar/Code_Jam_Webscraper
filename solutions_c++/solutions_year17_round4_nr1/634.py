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
#define MAXN 100000


int main(int argc, char *argv[]){
	READ(T);
	FOR(t, T){
		READ(n);
		READ(p);
		READV(v,n);
		vector<int> mods(p, 0);
		FOR(i, sz(v)){mods[v[i]%p]++;}
		int res =0;
		res += mods[0];
		if(p==2){
			res += (mods[1]+1)/2;
		}else if(p==3){
			res += min(mods[1], mods[2]);
			res += (max(mods[1], mods[2]) - min(mods[1], mods[2]) + 2) / 3;
		}else if(p==4){
			while(true){
				if(mods[1] && mods[3]){mods[1]--; mods[3]--; res++; continue;}
				if(mods[2] > 1){mods[2]--; mods[2]--; res++; continue;}
				if(mods[2] && mods[3] > 1){mods[2]--; mods[3]-=2; res++; continue;}
				if(mods[1] > 1 && mods[2]){mods[1]-=2; mods[2]--; res++; continue;}
				if(mods[1] > 1 && mods[2]){mods[1]-=2; mods[2]--; res++; continue;}
				if(mods[1] > 2 && mods[2] && mods[3]){mods[1]-=2; mods[2]--; mods[3]--; res++; continue;}
				if(mods[1] > 3){mods[1]-=4; res++; continue;}
				if(mods[3] > 3){mods[3]-=4; res++; continue;}
				break;
			}
			if(mods[1] || mods[2] || mods[3]) res++;
		}

		cout<<"Case #"<<(t+1)<<": "<<res<<endl;
	}
	return 0;
}