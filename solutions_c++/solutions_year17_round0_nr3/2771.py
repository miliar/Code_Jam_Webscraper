#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <utility>
#include <iomanip> 
#include <queue>

using namespace std;

#define pb push_back

#define N 100100

typedef long long ll;

ll solve(ll n, ll k)	{
	if (k == 1ll)
		return n;
		
	if (n%2ll || k%2ll == 0ll)
		return solve(n/2ll,k/2ll);
	else
		return solve(n/2ll-1ll,k/2ll);
}

int main() {
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	
	int t;
	ll n, k;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin >> n >> k;
		ll len = solve(n,k);
		cout << "Case #" << tt << ": " << len/2ll << ' ' << (len-1ll)/2ll << endl;
	}

	return 0;
}