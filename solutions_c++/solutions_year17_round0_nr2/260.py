//              +-- -- --++-- +-In the name of ALLAH-+ --++-- -- --+              \\

#include <bits/stdc++.h>

#define int long long

using namespace std ;

int const MX = 20 ;
int T , s[MX] , pw[MX] ;

inline int get_len (int x) {
	int cnt = 0 , tmp = x ;

	while (tmp) {
		cnt ++ ;
		tmp /= 10 ;
	}

	return cnt ;
}

int32_t main(){
	ios::sync_with_stdio(false) , cin.tie(0) , cout.tie(0) ;

	s[0] = 0 , pw[0] = 1 ;
	for (int i = 1 ; i < MX ; i ++) {
		s[i] = s[i - 1] * 10 + 1 ;
		pw[i] = pw[i - 1] * 10 ;
	}

	cin >> T ;

	for (int c = 0 ; c < T ; c ++) {
		
		int n ;
		cin >> n ;

		int len = get_len(n) ;

		int nw = 0 , prv = 0 ;
		for (int i = 0 ; i < len ; i ++) {
			int mx = 9 ;
			if (!i && len == 19) {
				mx = 1 ;
			}

			for (int j = mx ; j >= prv ; j --) {
				if (nw + s[len - i] * j <= n) {
					nw += pw[len - i - 1] * j ;
					prv = j ;
					break ;
				}
			}

		}
		cout << "Case #" << c + 1 << ": " << nw << '\n' ;
	}
}
