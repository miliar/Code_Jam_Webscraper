#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double ld;

char mat[100][100];

void run() {
	ll T;
	cin >> T;

	vector< pair<ll, ll> > sps;

	for(int t = 0; t < T; t++) {
		ll R, C;
		cin >> R >> C;
		for(int j = 0; j < R; j++)  {
			for(int i = 0; i < C; i++) {
				cin >> mat[j][i];
				if(mat[j][i] != '?') sps.push_back(make_pair(j, i));
			}
		}
	

		for(int j = 0; j < R; j++) {
			ll lp = -1;
			for(int i = 0; i < C; i++) {
				if(mat[j][i] != '?') {
					lp = i;
					break;
				}
			}		

			if(lp == -1) continue;

			for(int k = 0; k < lp; k++) mat[j][k] = mat[j][lp];

			for(int i = lp+1; i < C; i++) {
				if(mat[j][i] != '?') lp = i;
				else mat[j][i] = mat[j][lp];
			}
		}

		int lp = -1;
		for(int j = 0; j < R; j++) {
			if(mat[j][0] != '?') {
				lp = j;
				break;
			}
		}

		
		for(int j = 0; j < lp; j++) {
			for(int i = 0; i < C; i++) {
				mat[j][i] = mat[lp][i];
			}
		}

		for(int j = lp+1; j < R; j++) {
			if(mat[j][0] != '?') continue;
			
			for(int i = 0; i < C; i++) {
				mat[j][i] = mat[j-1][i];
			}
		}

		printf("Case #%d:\n", t+1);
		for(int j = 0; j < R; j++) {
			for(int i = 0; i < C; i++) {
				printf("%c", mat[j][i]);
			}
			printf("\n");
		}
	}
}

int main() {
	run();
}
