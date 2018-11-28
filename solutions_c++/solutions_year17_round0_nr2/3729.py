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

bool f(int x) {
	string s = "";
	while (x) {
		s.pb(x % 10 + '0');
		x /= 10;
	}
	reverse(all(s));
	for (int i = 1;i < s.size();i++) if (s[i] < s[i - 1]) return false;
	return true;
}

string convert(ll x) {
	string s = "";
	while (x) {
		s.pb(x % 10 + '0');
		x /= 10;
	}
	reverse(all(s));
	return s;
}

string s;
ll dp[50][20][5];

ll join(ll a , ll b) {
	string s = convert(b);
	for (int i = 0;i < s.size();i++) a *= 10LL;
	return a + b;
}

ll solve(int index , int prev ,  bool tight) {
	
	if (index + 1 == s.size()) {
		//adding the last digit now
		if (tight == false) return dp[index][prev][tight] = 9;
		int last_digit = s[(int)s.size() - 1] - '0';
		//no way to form this number now as number formed upto now is equal
		//last digit is lesser than the previous digit
		if (prev > last_digit) return dp[index][prev][tight] = -1;
		//max value possible is last_digit
		return dp[index][prev][tight] = last_digit;
	}

	if (dp[index][prev][tight] != -1) return dp[index][prev][tight];

	ll ans = 0;
	int curr_digit = s[index] - '0';
	for (int i = prev;i <= 9;i++) {
		if (tight == true) {
			if (i > curr_digit) break;
		}
		bool ntight = tight && (i == curr_digit);
		// cout << "index + 1 " << index + 1 << endl;
		// cout << "curr_digit " << curr_digit << endl;
		// cout << "adding " << i << endl;
		ll ret = solve(index + 1 , i , ntight);
		// cout << "ret " << ret << endl;
		if (ret != -1) {
			ans = max(ans , join(i , ret) );
		}
	}
	// cout << "ans " << ans << endl;
	return dp[index][prev][tight] = ans;

}

int main(int argc, char const *argv[])
{

	int tt;
	cin >> tt;
	for (int t = 1;t <= tt;t++) {

		fill(dp , -1);

		cout << "Case #" << t << ": ";
		
		ll n;
		cin >> n;
		
		s = convert(n);
		// cout << "s " << s << endl;
		if (s.size() == 1) {
			cout << n << '\n';
			continue;
		}
		//all 9 of length (len - 1)
		ll ans = 0;
		for (int i = 0;i < (int)s.size() - 1;i++) {
			ans = ans * 10LL + 9;
		}
		for (int fdigit = 1;fdigit <= 9;fdigit++) {
			// cout << "fdigit " << fdigit << endl;
			// cout << "S " << s << endl;
			if (fdigit > (s[0] - '0')) {
				// cout << "breaking at " << fdigit << endl;
				break;
			}
			// cout << "fdigit " << fdigit << endl;
			bool tight = (fdigit == (s[0] - '0'));
			// cout << "tight " << tight << endl;
			ll ret = solve(1 , fdigit , tight);
			// cout << "ret " << ret << endl;
			if (ret > 0) {
				ans = max(ans , join(fdigit , ret));
			}
		}
		cout << ans << endl;

	}

	return 0;
}