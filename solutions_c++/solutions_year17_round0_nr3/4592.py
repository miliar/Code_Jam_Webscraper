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
	int n,k;
	scanf("%d%d",&n,&k);
	priority_queue<pii>Q;
	Q.push(pii(n,0));
	pii ans;
	fru(i,k){
		pii u=Q.top();Q.pop();
		int a=-u.y,b=u.x+a;
		int c=a+(b-a-1)/2;
		Q.push(pii(ans.x=c-a,a));
		Q.push(pii(ans.y=b-c-1,c+1));
	}
	if(ans.x<ans.y)swap(ans.x,ans.y);
	printf("%d %d\n",ans.x,ans.y);
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
