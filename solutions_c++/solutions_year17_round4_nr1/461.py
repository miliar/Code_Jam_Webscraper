//              +-- -- --++-- +-In the name of ALLAH-+ --++-- -- --+              \\

#include <bits/stdc++.h>

using namespace std ;

int const N = 4 + 2 ;
int T , n , p , cnt[N] ;

int main(){
	ios::sync_with_stdio(false) , cin.tie(0) , cout.tie(0) ;

	cin >> T ;

	for (int tt = 0 ; tt < T ; tt ++) {
		memset(cnt , 0 , sizeof cnt) ;

		cin >> n >> p ;

		for (int i = 0 ; i < n ; i ++) {
			int x ;
			cin >> x ;
			cnt[x % p] ++ ;
		}
	
		cout << "Case #" << tt + 1 << ": " ;

		if (p == 1) {
			cout << cnt[0] << '\n' ;
		}
		else if (p == 2) {
			cout << cnt[0] + (cnt[1] + 1) / 2 << '\n' ;
		}
		else if (p == 3) {
			int ans = cnt[0] ;

			while (cnt[1] && cnt[2]) {
				ans ++ ;
				cnt[1] -- , cnt[2] -- ;
			}

			ans += (cnt[1] + 2) / 3 ;
			ans += (cnt[2] + 2) / 3 ;

			cout << ans << '\n' ;
		}
		else {
			int ans = cnt[0] ;
			
			while (cnt[2] >= 2) {
				ans ++ ;
				cnt[2] -= 2 ;
			}
			while (cnt[1] && cnt[3]) {
				ans ++ ;
				cnt[1] -- , cnt[3] -- ;
			}

			if (cnt[2] && cnt[1] >= 2) {
				ans ++ ;
				cnt[2] -- ;
				cnt[1] -= 2 ;
			}
			if (cnt[2] && cnt[3] >= 2) {
				ans ++ ;
				cnt[2] -- ;
				cnt[3] -= 2 ;
			}

			while (cnt[1] >= 4) {
				ans ++ ;
				cnt[1] -= 4 ;
			}
			while (cnt[3] >= 4) {
				ans ++ ;
				cnt[3] -= 4 ;
			}

			if (cnt[1] || cnt[2] || cnt[3]) {
				ans ++ ;
			}

			cout << ans << '\n' ;
		}
	}
}
