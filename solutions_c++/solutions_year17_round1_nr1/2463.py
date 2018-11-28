#include <bits/stdc++.h>
using namespace std;

#define pb         push_back

typedef long long ll;
const ll INF = 1000000000000000000ll;
const ll MOD = 1000000007ll;
const double EPS = 1e-8;

int main(void) {
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	int t;
	cin >> t;

	for(int l=1; l<=t; l++){
		int r, c;
		cin >> r >> c;

		vector<string> cake;
		for(int i=0; i<r; i++){
			string tmp;
			cin >> tmp;
			cake.pb(tmp);
		}

		vector<pair<int, int>> q;
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				if(cake[i][j] == '?'){
					q.pb(make_pair(i, j));
				}
			}
		}
		
		int cnt = 0;
		//横チェック
		for(int i=0; i<q.size(); i++){
			auto tmp = q[i];
			int yo = tmp.first;
			int xo = tmp.second;
			int y = tmp.first;
			int x = tmp.second;

			char l = '?';
			char r = '?';
			while(x >= 0){if(cake[y][x] != '?'){l = cake[y][x];}; x--;}
			y = yo;
			x = xo;
			while(x < c){if(cake[y][x] != '?'){ r = cake[y][x];}; x++;}
			if(l == r){
				cake[yo][xo] = l;
				if(l == '?') cnt++;
			}
		}

		//縦check
		cnt = 0;
		for(int i=0; i<q.size(); i++){
			auto tmp = q[i];
			int yo = tmp.first;
			int xo = tmp.second;
			int y = tmp.first;
			int x = tmp.second;
			if(cake[yo][xo] != '?') continue;

			char u = '?';
			char d = '?';
			while(y >= 0){if(cake[y][x] != '?'){u = cake[y][x];}; y--;}
			y = yo;
			x = xo;
			while(y < r){if(cake[y][x] != '?'){d = cake[y][x];}; y++;}
			if(u == d){
				cake[yo][xo] = u;
				if(u == '?') cnt++;
			}
		}

		//左斜check
		cnt = 0;
		for(int i=0; i<q.size(); i++){
			auto tmp = q[i];
			int yo = tmp.first;
			int xo = tmp.second;
			int y = tmp.first;
			int x = tmp.second;
			if(cake[yo][xo] != '?') continue;

			char u = '?';
			char d = '?';
			int uy, ux, dy, dx;
			while(y >= 0 && x >= 0 && y < r && x < c){if(cake[y][x] != '?'){u = cake[y][x]; uy=y; ux=x;}; y--; x++;}
			y = yo;
			x = xo;
			while(y >= 0 && x >= 0 && y < r && x < c){if(cake[y][x] != '?'){d = cake[y][x]; dy=y; dx=x;}; y++; x--;}
			if(u == d){
				if(u != '?'){
					for(int j=uy; j<=dy; j++){
						for(int k=dx; k<=ux; k++){
							cake[j][k] = u;
						}
					}
				}else if(u == '?') cnt++;
			}
		}

		//右斜めcheck
		cnt = 0;
		for(int i=0; i<q.size(); i++){
			auto tmp = q[i];
			int yo = tmp.first;
			int xo = tmp.second;
			int y = tmp.first;
			int x = tmp.second;
			if(cake[yo][xo] != '?') continue;

			char u = '?';
			char d = '?';
			int uy, ux, dy, dx;
			while(y >= 0 && x >= 0){if(cake[y][x] != '?'){u = cake[y][x]; uy = y; ux = x;}; y--; x--;}
			y = yo;
			x = xo;
			while(y < r && x < c){if(cake[y][x] != '?'){d = cake[y][x]; dy = y; dx = x;}; y++; x++;}
			if(u == d){
				if(u != '?'){
					for(int j=uy; j<=dy; j++){
						for(int k=ux; k<=dx; k++){
							cake[j][k] = u;
						}
					}
				}else if(u == '?') cnt++;
			}
		}

		//extend
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				char c = cake[i][j];
				if(c == '?') continue;

				int ylim;
				for(ylim=i; ylim<r; ylim++){
					if(cake[ylim][j] != c){
						break;
					}
				}
				//cout << ylim << endl;

				for(int n=j; n<c; n++){
					int cnt = 0;
					for(int k=i; k<ylim; k++){
						if(cake[k][n] == '?' || cake[k][n] == c){
							cnt++;
						}
					}
					//cout << ylim - i+1 << endl;
					if(cnt == (ylim-i)){
						for(int k=i; k<ylim; k++){
							cake[k][n] = c;
						}
					}else{
						break;
					}
				}
			}
		}


		//final yoko
		for(int i=0; i<r; i++){
			for(int j=c-1; j>=0; j--){
				char now = cake[i][j];

				int j2 = j;
				j2--;
				while(j2 >= 0 && cake[i][j2] == '?') {cake[i][j2] = now; j2--;}
			}
		}

		//final tate
		for(int i=0; i<c; i++){
			for(int j=r-1; j>=0; j--){
				char now = cake[j][i];

				int j2 = j;
				j2--;
				while(j2 >= 0 && cake[j2][i] == '?') {cake[j2][i] = now; j2--;}
			}
		}

		for(int i=0; i<c; i++){
			for(int j=0; j<r; j++){
				char now = cake[j][i];

				int j2 = j;
				j2++;
				while(j2 < r && cake[j2][i] == '?') {cake[j2][i] = now; j2++;}
			}
		}

		printf("Case #%d:\n", l);
		for(int i=0; i<r; i++){
			cout << cake[i] << endl;
		}

	}
	
	return 0;
}
