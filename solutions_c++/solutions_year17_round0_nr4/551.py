#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

int n;

struct tri{
	int x, y;
	char c;
	tri(int x = 0, int y = 0, char c = '\0') : x(x), y(y), c(c) { }
};

int linha[110][300];
int coluna[110][300];
int diagonalEsq[210][300];
int diagonalDir[210][300];
int idEsq[110][110];
int idDir[110][110];
char mat[110][110];
char ops[] = {'o', '+', 'x'};

vector < tri > aux, ans;
int tot = 0;

int getX(int x, int y){
	int qt = 0;
	int xx = x;
	while( xx >= 0 ){ qt += (mat[xx][y] == 'o' || mat[xx][y] == 'x'); xx--; }
	xx = x+1;
	while( xx < n  ){ qt += (mat[xx][y] == 'o' || mat[xx][y] == 'x'); xx++; }
	return qt;
}

int getY(int x, int y){
	int qt = 0;
	int yy = y;
	while( yy >= 0  ){ qt += (mat[x][yy] == 'o' || mat[x][yy] == 'x'); yy--; }
	yy = y+1;
	while( yy < n ){ qt += (mat[x][yy] == 'o' || mat[x][yy] == 'x'); yy++; }
	return qt;
}

int getDiagPrinc(int x, int y){
	int qt = 0;
	int a = x, b = y;
	while( a >= 0 && b >= 0 ){  qt += (mat[a][b] == 'o' || mat[a][b] == '+'); a--; b--; }
	a = x+1; b = y+1;
	while( a < n && b < n ){ qt += (mat[a][b] == 'o' || mat[a][b] == '+'); a++; b++; }
	return qt;
}

int getDiagSec(int x, int y){
	int qt = 0;
	int a = x, b = y;
	while( a >= 0 && b < n ){ qt += (mat[a][b] == 'o' || mat[a][b] == '+'); a--; b++; }
	a = x+1; b = y-1;
	while( a < n && b >= 0 ){ qt += (mat[a][b] == 'o' || mat[a][b] == '+'); a++; b--; }
	return qt;
}

bool check( ){
	int ok = 0;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			int a = 0;
			if((getX(i, j) >= 2) || (getY(i, j) >= 2) || 
			 (getDiagPrinc(i, j) >= 2) || (getDiagSec(i, j) >= 2)){
				return false;
			}
		}
	}
	return true; 
}

bool pode( int i, int j, char pos ){
	char bkp = mat[i][j];
	mat[i][j] = pos;
	bool ok = ((getX(i, j) >= 2) || (getY(i, j) >= 2) || 
			 (getDiagPrinc(i, j) >= 2) || (getDiagSec(i, j) >= 2));
	mat[i][j] = bkp;
	return (ok == false);
}

int main(){
	ios::sync_with_stdio(false);
	int t, m, x, y;
	char op;
	
	cin >> t;

	for(int w = 1; w <= t; w++){
		cin >> n >> m;

		tot = 0;
		ans.clear();

		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				mat[i][j] = '.';
			}
			mat[i][n] = '\0';
		}

		//initIds();

		for(int i = 0; i < m; i++){
			cin >> op >> x >> y;
			mat[x-1][y-1] = op;
			//aplica(x-1, y-1, op, 1);
		}

		for(int i = 0; i < n; i++){
			int l = ((mat[0][i] == '.') ? (3) : (1));
			if(mat[0][i] == 'o') continue;
			for(int j = 0; j < l; j++){
				if( mat[0][i] != ops[j] && pode(0, i, ops[j]) ){
					//aplica(0, i, ops[j], 1);
					mat[0][i] = ops[j];
					ans.push_back(tri(1, i+1, ops[j]));
					break;
				}
			}
		}

		for(int i = 1; i < n-1; i++){
			for(int j = 1; j < n; j++){
				if( pode(i, j, 'x') ){
					//aplica(i, j, 'x', 1);
					mat[i][j] = 'x';
					ans.push_back(tri(i+1, j+1, 'x'));
				}
			}
		}		

		for(int i = 0; i < n && n > 1; i++){
			for(int j = 0; j < 3; j++){
				if( mat[n-1][i] != ops[j] && pode(n-1, i, ops[j]) ){
					//aplica(n-1, i, ops[j], 1);
					mat[n-1][i] = ops[j];
					ans.push_back(tri(n, i+1, ops[j]));
					break;
				}
			}
		}
		
		for(int i =0; i < n; i++){
			for(int j = 0; j < n; j++){
				if( mat[i][j] != '.' ) tot++;
				if( mat[i][j] == 'o' ) tot++;
			}
		}

		cout << "Case #" << w << ": " << tot << " " << ans.size() << "\n";
		for(int i= 0; i < ans.size(); i++){
			cout << ans[i].c << " " << ans[i].x << " " << ans[i].y << '\n';
		}
		
	}

	return 0;
}