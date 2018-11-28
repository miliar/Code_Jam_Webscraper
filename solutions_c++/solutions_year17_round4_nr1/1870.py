#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;
const double EPS = 1e-9;
const int INF = 1 << 29;
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define all(a) a.begin(),a.end()
#ifndef ONLINE_JUDGE
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#else
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);

int const NN = 1e5+5;
int g[NN];

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int tt; in(tt);
	for (int cs = 1; cs <= tt; ++cs){		
		int n; cin >> n; int p; cin >> p;
		for (int i = 1; i <= n; ++i){
			cin >> g[i]; g[i] %= p;
		}
		int z = 0, o = 0, t = 0, th = 0;
		for (int i = 1; i <= n; ++i){
			z += (g[i] == 0); o += (g[i] == 1); t += (g[i] == 2); th += (g[i] == 3);
		}
		int ans = 0;
		if (p == 2){
			ans += o / 2;
		}
		else if (p == 3){
			ans += min(o, t);
			int d = max(o, t) - min(o, t);
			ans += 2 * (d / 3);
			d %= 3;
			if (d > 1)++ans;
		}
		else{

		}
		printf("Case #%d: %d\n", cs, n - ans);
	}
	return 0;
}