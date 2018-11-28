//              +-- -- --++-- +-In the name of ALLAH-+ --++-- -- --+              \\

#include <bits/stdc++.h>

using namespace std ;

#define int long long

int const N = 1000 + 20 ;
int T , n , c , m , cnt[N] , d[N] ;

int32_t main(){
	ios::sync_with_stdio(false) , cin.tie(0) , cout.tie(0) ;

	cin >> T ;

	for (int tt = 0 ; tt < T ; tt ++) {
		memset(cnt , 0 , sizeof cnt) ;
		memset(d , 0 , sizeof d) ;

		cin >> n >> c >> m ;

		for (int i = 0 ; i < m ; i ++) {
			int p , b ;
			cin >> p >> b ;
			b -- ;

			d[b] ++ ;
			cnt[p] ++ ;
		}
	
		int ans = 0 ;
		for (int i = 0 ; i < c ; i ++) {
			ans = max(ans , d[i]) ;
		}

		int sum = 0 ;
		for (int i = 1 ; i <= n ; i ++) {
			sum += cnt[i] ;
			ans = max(ans , (sum + i - 1) / i) ;
		}

		sum = 0 ;
	
		for (int i = 1 ; i <= n ; i ++) {
			sum += max(0ll , cnt[i] - ans) ;
		}

		cout << "Case #" << tt + 1 << ": " << ans << ' ' << sum << '\n' ;
	}
}
