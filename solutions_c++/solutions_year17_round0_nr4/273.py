//              +-- -- --++-- +-In the name of ALLAH-+ --++-- -- --+              \\

#include <bits/stdc++.h>

using namespace std ;

int const N = 200 + 10 ;

int T ;

int n , m , match[2][N] ;
bool mark[2][N][N] , chg[N][N] , dead[2][N] , vis[N] ;
vector <int> g[N] ;

void out (int c) ;

bool dfs (int v) {
	if (v == -1) {
		return 1 ;	
	}
	
	if (vis[v]) {
		return 0 ;
	}

	vis[v] = 1 ;

	for (int u : g[v]) {
		if (!dead[1][u] && match[1][u] != v && dfs(match[1][u])) {
			match[0][v] = u ;
			match[1][u] = v ;
			return 1 ;
		}
	}
}

int main(){
	ios::sync_with_stdio(false) , cin.tie(0) , cout.tie(0) ;

	cin >> T ;

	for (int c = 0 ; c < T ; c ++) {
		cin >> n >> m ;
	
		memset(mark , 0 , sizeof mark) ;
		memset(chg , 0 , sizeof chg) ;

		for (int i = 0 ; i < m ; i ++) {
			char c ;
			int x , y ;

			cin >> c >> x >> y ;
			x -- , y --;

			if (c == 'x') {
				mark[0][x][y] = 1 ;
			}
			else if (c == '+') {
				mark[1][x][y] = 1 ;
			}
			else {
				mark[0][x][y] = 1 ;
				mark[1][x][y] = 1 ;
			}
		}

		// ****

		memset(match , -1 , sizeof match) ;
		memset(vis , 0 , sizeof vis) ;
		memset(dead , 0 , sizeof dead) ;

		for (int i = 0 ; i < N ; i ++) {
			g[i].clear() ;
		}

		for (int i = 0 ; i < n ; i ++) {
			for (int j = 0 ; j < n ; j ++) {
				if (mark[0][i][j]) {
					dead[0][i] = 1 ;
					dead[1][j] = 1 ;
				}
			}
		}

		for (int i = 0 ; i < n ; i ++) {
			for (int j = 0 ; j < n ; j ++) {
				if (!dead[0][i] && !dead[1][j]) {
					g[i].push_back(j) ;
				}
			}
		}

		bool fin = 0 ;
		while (!fin) {
			memset(vis , 0 , sizeof vis) ;

			fin = 1 ;
			for (int i = 0 ; i < n ; i ++) {
				if (!vis[i] && !dead[0][i] && match[0][i] == -1) {
					fin &= !dfs(i) ;
				}
			}
		}

		for (int i = 0 ; i < n ; i ++) {
			int j = match[0][i] ;

			if (j == -1 || mark[0][i][j]) {
				continue ;
			}

			chg[i][j] = 1 ;
			mark[0][i][j] = 1 ;
		}

		// ****

		// ****

		memset(match , -1 , sizeof match) ;
		memset(vis , 0 , sizeof vis) ;
		memset(dead , 0 , sizeof dead) ;

		for (int i = 0 ; i < N ; i ++) {
			g[i].clear() ;
		}

		for (int ii = 0 ; ii < n ; ii ++) {
			for (int jj = 0 ; jj < n ; jj ++) {
				int i = ii + jj , j = ii + n - jj ;

				if (mark[1][ii][jj]) {
					dead[0][i] = 1 ;
					dead[1][j] = 1 ;
				}
			}
		}

		for (int ii = 0 ; ii < n ; ii ++) {
			for (int jj = 0 ; jj < n ; jj ++) {
				int i = ii + jj , j = ii + n - jj ;

				if (!dead[0][i] && !dead[1][j]) {
					g[i].push_back(j) ;
				}
			}
		}

		fin = 0 ;
		while (!fin) {
			memset(vis , 0 , sizeof vis) ;

			fin = 1 ;
			for (int i = 0 ; i < 2 * n ; i ++) {
				if (!vis[i] && !dead[0][i] && match[0][i] == -1) {
					fin &= !dfs(i) ;
				}
			}
		}

		for (int i = 0 ; i < 2 * n ; i ++) {
			int j = match[0][i] ;
	
			// i = ii + jj , j = ii + n - jj  ==>  i + j = 2ii + n , ii = (i + j - n) / 2
			int ii = (i + j - n) / 2 , jj = i - ii ;
		
			if (j == -1 || mark[1][ii][jj]) {
				continue ;
			}

			chg[ii][jj] = 1 ;
			mark[1][ii][jj] = 1 ;
		}

		// ****

		out(c) ;	
	}
}

void out (int c) {
	cout << "Case #" << c + 1 << ": " ;

	int cnt = 0 , ans = 0 ;
		
	for (int i = 0 ; i < n ; i ++) {
		for (int j = 0 ; j < n ; j ++) {
			if (chg[i][j]) {
				cnt ++ ;
			}
		}
	}

	for (int i = 0 ; i < n ; i ++) {
		for (int j = 0 ; j < n ; j ++) {
			ans += mark[0][i][j] ;
			ans += mark[1][i][j] ;
		}
	}
		
	cout << ans << ' ' << cnt << '\n' ;

	for (int i = 0 ; i < n ; i ++) {
		for (int j = 0 ; j < n ; j ++) {
			if (chg[i][j]) {
				if (mark[0][i][j] && mark[1][i][j]) {
					cout << "o " ;
				}
				else if (mark[0][i][j]) {
					cout << "x " ;
				}
				else {
					cout << "+ " ;
				}
				cout << i + 1 << ' ' << j + 1 << '\n' ;
			}
		}
	}
}
