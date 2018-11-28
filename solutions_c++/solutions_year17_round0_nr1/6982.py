#include "bits/stdc++.h"
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pi;
typedef pair <ll, ll> pll;

template<class T> using V = vector<T>;

typedef V <int> vi;
typedef V <ll> vll;
typedef V <pi> vpi;
typedef V <pll> vpll;

const int INF = int(1e9) + 7;
const ll LINF = ll(1e18) + 9;

struct _ {
	_()	{
		ios_base::Init i;
		cin.sync_with_stdio(0);
		cin.tie(NULL);
		cout << fixed << setprecision(25);
		srand(time(NULL));
#define deb(x) cerr << #x << " = " << x << '\n'
#define all(ContainerName) ContainerName.begin(),ContainerName.end()
#ifndef DEBUG
#define cerr if(0)cerr
#endif
#ifdef DEBUG
			freopen("input.txt", "r", stdin);
			freopen("output.txt", "w", stdout);
#endif
	}
} _;






inline void solve (int TEST_CASE) {
	
	string s;
	int k, ans = 0;
	cin >> s >> k;
	
	for (int i = 0; i <= s.size() - k; ++i)
		if (s[i] == '-') {
			++ans;
			for (int l = 0; l < k; ++l)
				s[i + l] = (s[i + l] == '-' ? '+' : '-');
		}
	
	for (int i = s.size() - k + 1; i != s.size(); ++i)
		if (s[i] == '-') {
			cout << "Case #" << TEST_CASE << ": " << "IMPOSSIBLE" << '\n';
			return;
		}
	
	cout << "Case #" << TEST_CASE << ": " << ans << '\n';
}





int main() {
		
	int t;
	cin >> t;
	for (int i = 1; i <= t; solve(i++));
	
	cerr << "\n\n\nTIME  =  " << int(clock()*ld(1000)/CLOCKS_PER_SEC) << "\t\t\t\t\t";
	return 0;
}
