//              +-- -- --++-- +-In the name of ALLAH-+ --++-- -- --+              \\

#include <bits/stdc++.h>

using namespace std ;

int const N = 25 + 3 ;
int T ;

int n , m ;
bool mark[N] ;
string s[N] ;

string solve (string s) {
	int sz = s.size() ;
	int p = -1 ;

	for (int i = 0 ; i < sz ; i ++) {
		if (s[i] != '?') {
			p = i ;
			break ;
		}
	}

	for (int i = 0 ; i < sz ; i ++) {
		if (s[i] != '?') {
			continue ;
		}

		if (i < p) {
			s[i] = s[p] ;
		}
		else {
			s[i] = s[i - 1] ;
		}
	}

	return s ;
}

int main(){
	ios::sync_with_stdio(false) , cin.tie(0) , cout.tie(0) ;

	cin >> T ;

	for (int c = 0 ; c < T ; c ++) {
		cout << "Case #" << c + 1 << ":\n" ;
		
		memset(mark , 0 , sizeof mark) ;

		cin >> n >> m ;
		for (int i = 0 ; i < n ; i ++) {
			cin >> s[i] ;
			for (int j = 0 ; j < m ; j ++) {
				mark[i] |= (s[i][j] != '?') ;	
			}
		}

		for (int i = 0 ; i < n ; i ++) {
			if (mark[i]) {
				s[i] = solve(s[i]) ;
			}
		}

		int p = -1 ;
		for (int i = 0 ; i < n ; i ++) {
			if (mark[i]) {
				p = i ;
				break ;
			}
		}

		for (int i = 0 ; i < n ; i ++) {
			if (mark[i]) {
				continue ;
			}

			if (i < p) {
				s[i] = s[p] ;	
			}
			else {
				s[i] = s[i - 1] ;
			}
		}

		for (int i = 0 ; i < n ; i ++) {
			cout << s[i] << '\n' ;
		}
	}
}
