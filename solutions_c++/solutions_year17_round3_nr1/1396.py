#include <bits/stdc++.h>
 
using namespace std;
 
#define ll long long int
#define pb push_back
#define mp make_pair
#define inff 100000
#define ff first
#define ss second
#define sz(x) ((int) (x).size())
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define rep(i,N) for(int i = 0;i < N;i++)
#define frep(i,a,b) for(int i = a;i <= b;i++)
#define pii pair<int , int>
#define pll pair<ll , ll>
#define vii vector<int>
#define vpii vector< pii >
#define fill(A,v) memset(A,v,sizeof(A))
#define setbits(x) __builtin_popcountll(x)
#define print(A,j,k) for(int ii=j;ii<k;ii++)cout<<A[ii]<<" ";cout<<"\n"
#define all(x) (x).begin(), (x).end()
#define gcd __gcd
#define CASES int t;cin>>t;while(t--)
#define FILE freopen("inp.txt" , "r" , stdin);
#define ld long double

const int MOD = 1e9 + 7;
const int N = 2e6 + 5;
const int K = (1 << 17) + 10;
const ll INF = 2e18 + 500;
const int inf = 2e9 + 500;
const int SQRT = 500;
const int lgN = 20;
const ld PI = 3.1415926535897;

pll A[N];
ll dp[1003][1003];

int main(int argc, char const *argv[])
{
	fast;

	int t;
	cin >> t;
	for (int tt = 1;tt <= t;tt++) {

		cout << "Case #" << tt << ": ";
		int n , k;
		cin >> n >> k;

		frep(i , 1 , n) {
			cin >> A[i].ff >> A[i].ss;
		}


		if (k == 1) {
			ll ans = 0;
			frep(i , 1 , n) {
				ans = max(ans , A[i].ff * A[i].ff + 2 * A[i].ff * A[i].ss);
			}
			ld sol = (ld)ans * PI;
			cout <<  setprecision(10) << fixed << sol << endl;
			continue;
		}


		sort(A + 1 , A + n + 1);
		reverse(A + 1 , A + n + 1);

		//dp[i][j] denote max possible area if we select 
		// j pancakes from first i 

		ll sol = 0;
		for (int i = 1;i <= n;i++) {
			priority_queue<ll> PQ;
			ll ans = A[i].ff * A[i].ff + 2LL * A[i].ff * A[i].ss;
			// cout << "ans " << ans << endl;
			int c = 0;
			for (int j = i + 1;j <= n;j++) {
				c++;
				PQ.push(2LL * A[j].ff * A[j].ss);
			}
			if (c < k - 1) continue;
			c = k - 1;
			while (c--) {
				ans += PQ.top();
				PQ.pop();
			}
			// cout << "net ans " << ans << endl;
			sol = max(sol , ans);
		}
		ld fans = sol;
		fans *= PI;
		cout <<  setprecision(10) << fixed << fans << endl;

	}


	return 0;
}