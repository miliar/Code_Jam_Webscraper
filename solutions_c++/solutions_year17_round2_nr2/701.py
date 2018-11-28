#include <bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
//#define tr(it,v) for(auto it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define ALL(G) (G).begin(),(G).end()

#if 1
	#define DEB printf
#else
	#define DEB(...)
#endif

typedef long long ll;
typedef long long LL;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int inft = 1000000009;
const int mod = 1000000007;
const int MAXN = 1000006;

void no(){
	puts("IMPOSSIBLE");
}
void solve() {
	int r,o,y,g,b,v,n;
	scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
	string S="";
	map<char,int> M;
	M['$']=0;
	M['R']=r;
	M['Y']=y;
	M['B']=b;
	char tab[]={'R','Y','B'};
	while(M['R']+M['Y']+M['B']>0){
		char best='$';
		fru(h,3)if(S.back()!=tab[h] && M[tab[h]]>M[best])best=tab[h];
		if(best=='$')return no();
		S+=best;
		M[best]--;
	}
	int k=min(7,n);
	vi perm;
	fru(i,k)perm.pb(i+1);
	do{
		string W=S;
		fru(i,k)W[n-i-1]=S[n-perm[i]];
		bool ok=1;
		fru(i,n)if(W[i]==W[(i+1)%n])ok=0;
		if(ok){S=W;break;}
	}while(next_permutation(ALL(perm)));
	if(S.back()==S[0])return no();
	cout<<S<<endl;
}

int main() {
	int te = 1;
	scanf("%d",&te);
	fru(ti,te) {
		printf("Case #%d: ",ti+1);
		solve();
	}
	return 0;
}
