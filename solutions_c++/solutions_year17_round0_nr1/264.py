//              +-- -- --++-- +-In the name of ALLAH-+ --++-- -- --+              \\

#include <bits/stdc++.h>

using namespace std ;

int T ;

int main(){
	ios::sync_with_stdio(false) , cin.tie(0) , cout.tie(0) ;

	cin >> T ;

	for (int c = 0 ; c < T ; c ++) {
		string s ;
		int k , n ;

		cin >> s ;
		cin >> k ;

		n = s.size() ;

		int ans = 0 ;
		for (int i = 0 ; i < n ; i ++) {
			if (s[i] == '-') {
				if (i + k > n) {
					ans = -1 ;
					break ;
				}

				ans ++ ;
				for (int j = i ; j < i + k ; j ++) {
					s[j] = '+' + '-' - s[j] ;
				}	
			}
		}

		cout << "Case #" << c + 1 << ": " ;
		if (ans == -1) {
			cout << "IMPOSSIBLE\n" ;
		}
		else {
			cout << ans << '\n' ;
		}
	}
}
