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






inline ll solve () {
	
	ll n;
	cin >> n;
	
	vi d;
	
	for (; n; d.push_back(n % 10), n/= 10);
	
	for (int i = 1; i < d.size(); ++i)
		if (d[i] > d[i - 1]) {
			--d[i];
			for (int j = 0; j < i; d[j++] = 9);
		}
	
	ll ans = 0;
	for (auto i = d.rbegin(); i != d.rend(); ++i)
		ans = 10*ans + *i;
	
	return ans;
}





int main() {
		
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		cout << "Case #" << i << ": " << solve() << '\n';
	
	cerr << "\n\n\nTIME  =  " << int(clock()*ld(1000)/CLOCKS_PER_SEC) << "\t\t\t\t\t";
	return 0;
}
