//              +-- -- --++-- +-In the name of ALLAH-+ --++-- -- --+              \\

#include <bits/stdc++.h>

#define int long long

using namespace std ;

int T ;
map <int , int> mp ;

int get (int n , int s) {
	if (mp.count(n)) {
		return mp[n] ;
	}
	if (n <= s) {
		return mp[n] = 0 ;
	}

	return mp[n] = 1 + get(n >> 1 , s) + get((n - 1) >> 1 , s) ;
}

int32_t main(){
	ios::sync_with_stdio(false) , cin.tie(0) , cout.tie(0) ;

	cin >> T ;

	for (int c = 0 ; c < T ; c ++) {
		
		int n , k ;
		cin >> n >> k ;
	
		int L = 0 , R = n ;
		while (L < R - 1) {
			int md = (L + R) >> 1 ;

			if (get(n , md) <= k - 1) {
				R = md ;
			}
			else {
				L = md ;
			}

			mp.clear() ;
		}

		cout << "Case #" << c + 1 << ": " << R / 2 << ' ' << (R - 1) / 2 << endl ;
	}
}
