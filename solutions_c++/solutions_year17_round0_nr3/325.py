#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	freopen ( "C-large.in", "r", stdin );
	freopen ( "C.out", "w", stdout );
	
	int ntc;
	cin >> ntc;
	for ( int test = 1; test <= ntc; ++test ) {
		ll n, k, A, B, step;
		cin >> n >> k;
		
		map<ll,ll> m;
		map<ll,ll>::reverse_iterator it;
		m[n]++;
		do {
			it = m.rbegin();
			n = it->first;
			
			step = min ( k, it->second );
			
			m.erase(n);
			A = n/2;
			B = n-A-1;
			if ( A == B ) m[A] += 2L*step;
			else m[A] += step, m[B] += step;
			
			k -= step;
		} while ( k );
		cout << "Case #" << test << ": " << A << " " << B << endl;
	}
	
	return 0;
}
