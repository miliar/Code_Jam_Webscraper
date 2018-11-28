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

void solve() {
	string R;
	int k;
	cin>>R>>k;
	int n=R.size();
	int ret=0;
	set<int>S;
	bool poss=1;
	fru(i,n){
		while(!S.empty() &&*S.begin()+k<=i)S.erase(S.begin());
		if((S.size()+(R[i]=='-'))%2){
		//	printf("mam %d\n",i);
			if(i<=n-k){S.insert(i);ret++;}
			else poss=0;
		}
	}
	if(!poss)puts("IMPOSSIBLE");
	else printf("%d\n",ret);
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
