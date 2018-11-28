										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL
#define EPS 1e-9

int n, q;
double mat[110][110];
double d[110], s[110];

bool gr(double a, double b){
	return a - EPS > b;
}

void Floyd(){
	for(int k = 0; k < n; k++){
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(mat[i][k] < 0 || mat[k][j] < 0)
					continue;
				if(mat[i][j] < 0 || mat[i][j] > mat[i][k] + mat[k][j])
					mat[i][j] = mat[i][k] + mat[k][j];
			}
		}
	}
}

void print(){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			cout << mat[i][j] << ' ';
		}
		cout << endl;
	}
}

int main(){
	std::ios::sync_with_stdio(false);
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> q;
		for(int i = 0; i < n; i++)
			cin >> d[i] >> s[i];
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++)
				cin >> mat[i][j];
			mat[i][i] = 0;
		}

		Floyd();
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(mat[i][j] < 0 || gr(mat[i][j], d[i]))
					mat[i][j] == -1;
				else mat[i][j] /= s[i];
			}
		}
		Floyd();

		cout << "Case #" << ++test << ":";
		for(int i = 0; i < q; i++){
			int u, v;
			cin >> u >> v;
			cout << ' ' << setprecision(7) << fixed << mat[u - 1][v - 1];
		}
		cout << endl;
	}
	return 0;
}
