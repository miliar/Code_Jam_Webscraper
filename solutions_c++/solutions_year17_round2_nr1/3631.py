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

int const NN = 1003;
int K[NN];
int S[NN];
double tim[NN];
int D, N;

bool ok(double vel){
	double tm = D*1.0 / vel;
	for (int i = 1; i <= N; ++i){
		if (tim[i] > tm)return false;
	}
	return true;
}

void solve(){
	double lo = 1, hi = 1e15, mid; int tot = 1e2;
	while (hi - lo >= (1e-7) && tot--){
		mid = (lo + hi) / 2.0;
		if (ok(mid)){
			lo = mid + (1e-7);
		}
		else{
			hi = mid - (1e-7);
		}
	}
	printf("%.12lf\n", mid);
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t; in(t);
	for (int cs = 1; cs <= t; ++cs){		
		cin >> D >> N;
		for (int i = 1; i <= N; ++i){
			cin >> K[i] >> S[i];
		}
		tim[N] = (D*1.0 - 1.0*K[N]) / S[N] * 1.0;
		double mx = tim[N];
		for (int i = N - 1; i >= 1; --i){
			double tm = (D*1.0 - 1.0*K[i]) / S[i] * 1.0;
			tm = max(tm, mx);
			tim[i] = tm;
			mx = max(mx, tim[i]);
		}
		printf("Case #%d: ", cs); //el;
		/*cout << D << " " << N; el;
		for (int i = 1; i <= N; ++i){
			cout << K[i] << " " << S[i]; el;
		}*/
		solve();
	}
	return 0;
}