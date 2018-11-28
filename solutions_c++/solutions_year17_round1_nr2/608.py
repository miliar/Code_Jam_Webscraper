//              +-- -- --++-- +-In the name of ALLAH-+ --++-- -- --+              \\

#include <bits/stdc++.h>

using namespace std ;
using pii = pair <int , int> ;

int T ;

int const N = 50 + 10 ;
int n , m , a[N][N] , b[N] , p[N] , ans ;
vector <pii> vec[N] ;
set <pii> L , R ;

inline void clr () {
	n , m = 0 ;
	ans = 0 ;

	memset(a , 0 , sizeof a) ;
	memset(b , 0 , sizeof b) ;
	memset(p , 0 , sizeof p) ;
	
	for (int i = 0 ; i < N ; i ++) {
		vec[i].clear() ;
	}
	
	L.clear() ;
	R.clear() ;
}

int main () {
	ios::sync_with_stdio(false) , cin.tie(0) , cout.tie(0) ;

	cin >> T ;

	for (int c = 0 ; c < T ; c ++) {
		clr() ;

		cin >> n >> m ;

		for (int i = 0 ; i < n ; i ++) {
			cin >> b[i] ;
		}

		for (int i = 0 ; i < n ; i ++) {
			for (int j = 0 ; j < m ; j ++) {
				cin >> a[i][j] ;

				int x = a[i][j] ;

				int l = (x * 10 + 10) / 11 ;
				l = (l + b[i] - 1) / b[i] ;
			
				int r = (x * 10) / 9 ;
				r = r / b[i] ;

				vec[i].push_back({l , r}) ;
			}
	
			sort(vec[i].begin() , vec[i].end()) ;
		}

		for  (int i = 0 ; i < n ; i ++) {
			L.insert({vec[i][0].first , i}) ;
			R.insert({vec[i][0].second , i}) ;
		}

		bool fin = 0 ;
		while (!fin) {
			if (L.rbegin() -> first > R.begin() -> first) {
				int id = R.begin() -> second ;
			
				L.erase({vec[id][p[id]].first , id}) ;
				R.erase({vec[id][p[id]].second , id}) ;
				
				p[id] ++ ;
				if (p[id] == m) {
					fin = 1 ;
					break ;
				}

				L.insert({vec[id][p[id]].first , id}) ;
				R.insert({vec[id][p[id]].second , id}) ;
			}
			else {
				ans ++ ;

				L.clear() , R.clear() ;

				for (int i = 0 ; i < n ; i ++) {
					p[i] ++ ;

					if (p[i] == m) {
						fin = 1 ;
						break ;
					}

					L.insert({vec[i][p[i]].first , i}) ;
					R.insert({vec[i][p[i]].second , i}) ;
				}
			}
		}

		cout << "Case #" << c + 1 << ": " << ans << '\n' ;
	}
}
