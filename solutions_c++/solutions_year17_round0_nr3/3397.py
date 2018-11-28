#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) (int)a.size()
#define rep(i, a, n) for(int i = a; i < n; i++)
#define dec(i, a, n) for(int i = a; i >= n; i--)
#define clr(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define MAXN 100010 // 1e5
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector <int> vi;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	scanf("%d", &tt);
	rep(caso,1,tt+1) {
		int n, k;
		scanf("%d %d", &n, &k);
		set <pair <int, pii > > simu;
		simu.insert(mp(-n,mp( 0,n+1)));
		rep(i,1,k) {
			int l= (*simu.begin()).y.x, r=(*simu.begin()).y.y;
			simu.erase(simu.begin());
			int meio = (l + r) /2;
			simu.insert(mp(-(meio-l-1),mp(l,meio)));
			simu.insert(mp(-(r-meio-1), mp(meio, r)));
		}
		int l = (*simu.begin()).y.x, r= (*simu.begin()).y.y;
		int meio=(l+r)>>1;
		printf("Case #%d: %d %d\n", caso, max(r-meio-1,meio-l-1),min(r-meio-1,meio-l-1));
	}
}
