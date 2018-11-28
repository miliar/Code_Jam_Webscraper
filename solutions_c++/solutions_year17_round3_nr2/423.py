#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;

#define fi first
#define se second

#define maxn 2222
const int oo = 1e9;

int x[2222];
int f[888][888][3][3];

int main (){
	freopen("a.inp", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++){
		int n, m;
		cin >> n >> m;
		memset (x, 0, sizeof (x));
		for (int i = 0; i <= 720; i++){
			for (int j = 0; j <= 720; j++){
				for (int _i = 0; _i < 3; _i++){
					for (int _j = 0; _j < 3; _j++)
						f[i][j][_i][_j] = oo;
				}		
			}
		}

		for (int i = 0; i < n; i++){
			int l, r;
			cin >> l >> r;
			for (int j = l; j < r; j++){
				x[j] = 1;
			}
		}

		for (int i = 0; i < m; i++){
			int l, r;
			cin >> l >> r;
			for (int j = l; j < r; j++){
				x[j] = 2;
			}
		}
		int ret = oo;
		for (int i = 0; i <= 720; i++){
			for (int j = 0; j <= 720; j++){
				for (int stat = 1; stat < 3; stat++){
					for (int cur = 1; cur < 3; cur++){
						int time = i + j;

						if (time == 0 && cur != stat) continue;
						if (cur == x[time]) continue;

						int &tmp = f[i][j][cur][stat];
						if (time == 0){
							tmp = 0;
							continue;
						}

						
						
						if (cur == 1){
							if (i > 0){
								tmp = min (tmp, f[i-1][j][1][stat]);
								tmp = min (tmp, f[i-1][j][2][stat] + 1);
							}
						}

						if (cur == 2){
							if (j > 0){
								tmp = min (tmp, f[i][j-1][2][stat]);
								tmp = min (tmp, f[i][j-1][1][stat] + 1);
							}
						}


						if (time == 1440){
							tmp += cur != stat;
							ret = min (ret, tmp);
						}

					}
				}
			}
		}

		printf ("Case #%d: %d\n", t, ret);
	}
	
	return 0;
}