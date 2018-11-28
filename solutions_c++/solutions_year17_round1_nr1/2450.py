#include <bits/stdc++.h>

using namespace std;

#define N 25

string mat[N + 1];
string aux[N + 1];
bool seen[N + 1][N + 1];
int n, m;

void print(){
	int i;

	for (i = 0; i < n; i++){
		cout << mat[i] << endl;
	}
}

bool inside(int x, int y){
	return x >= 0 and x < n and y >= 0 and y < m;
}

char check(int xi, int yi, int xf, int yf){
	char c = 0;
	int i, j;

	for (i = xi; i <= xf; i++){
		for (j = yi; j <= yf; j++){
			if (seen[i][j]){
				return 0;
			}

			if (mat[i][j] != '?'){
				if (c){
					return 0;
				}

				c = mat[i][j];
			}
		}
	}

	return c;
}

void fill(int xi, int yi, int xf, int yf, char c){
	int i, j;

	for (i = xi; i <= xf; i++){
		for (j = yi; j <= yf; j++){
			seen[i][j] = true;
			mat[i][j] = c;
		}
	}
}

void restore(int xi, int yi, int xf, int yf){
	int i, j;

	for (i = xi; i <= xf; i++){
		for (j = yi; j <= yf; j++){
			seen[i][j] = false;
			mat[i][j] = aux[i][j];
		}
	}
}

bool solve(int pos){
	int x, y, i, j;
	char c;

	x = pos / m;
	y = pos % m;

	if (pos >= n * m){
		return true;
	}

	if (seen[x][y]){
		return solve(pos + 1);
	}

	for (i = n - 1; i >= x; i--){
		for (j = m - 1; j >= y; j--){
			c = check(x, y, i, j);

			if (c){
				fill(x, y, i, j, c);

				if (solve(pos + 1)){
					return true;
				}

				restore(x, y, i, j);
			}
		}
	}

	return false;
}

int main(){
	int t, i, j;

	ios::sync_with_stdio(false);
	
	cin >> t;
	
	for (i = 1; i <= t; i++){
		cin >> n >> m;

		for (j = 0; j < n; j++){
			cin >> mat[j];
			aux[j] = mat[j];
		}

		memset(seen, false, sizeof(seen));
		solve(0);

		cout << "Case #" << i << ":" << endl;

		print();
	}

	return 0;
}