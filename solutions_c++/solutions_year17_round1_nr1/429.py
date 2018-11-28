#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

main() {

	FILE *fin = freopen("A-large.in", "r", stdin);
	FILE *fout = freopen("A-large.out", "w", stdout);


	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int r, c;
		cin >> r >> c;
		string str[r];
		for(int i = 0; i < r; i++){
			cin >> str[i];
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(str[i][j] != '?'){
					int k = j;
					while(1){
						k--;
						if(k < 0 || k >= c) break;
						if(str[i][k] != '?') break;
						str[i][k] = str[i][k+1];
					}
				}
			}
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(str[i][j] != '?'){
					int k = j;
					while(1){
						k++;
						if(k < 0 || k >= c) break;
						if(str[i][k] != '?') break;
						str[i][k] = str[i][k-1];
					}
				}
			}
		}

		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(str[i][j] != '?'){
					int k = i;
					while(1){
						k--;
						if(k < 0 || k >= r) break;
						if(str[k][j] != '?') break;
						str[k][j] = str[k+1][j];
					}
				}
			}
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(str[i][j] != '?'){
					int k = i;
					while(1){
						k++;
						if(k < 0 || k >= r) break;
						if(str[k][j] != '?') break;
						str[k][j] = str[k-1][j];
					}
				}
			}
		}
		cout << endl;
		for(int i = 0; i < r; i++){
			cout << str[i] << endl;
		}
	}
	exit(0);
}