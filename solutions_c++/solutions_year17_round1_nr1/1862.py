#include <bits/stdc++.h>
using namespace std;

void solve(char M[30][30], int R, int C){
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			if(M[i][j]!='?'){
				char c =  M[i][j];
				for(int k = i+1; k < R; k++){
					if(M[k][j]!='?') break;
					M[k][j]=c;
				}
				for(int k = i-1; k >= 0; k--){
					if(M[k][j]!='?') break;
					M[k][j]=c;
				}
			}
		}
	}

	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			if(M[i][j]!='?'){
				char c =  M[i][j];
				for(int k = j+1; k < C; k++){
					if(M[i][k]!='?') break;
					M[i][k]=c;
				}
				for(int k = j-1; k >= 0; k--){
					if(M[i][k]!='?') break;
					M[i][k]=c;
				}
			}
		}
	}

	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			cout << M[i][j];
		}
		cout << endl;
	}
}

int main(){
	int T;
	cin >> T;
	for(int c=1; c<=T; c++){
		int R, C;
		cin >> R >> C;
		char M[30][30];
		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				cin >> M[i][j];
			}
		}
		printf("Case #%d:\n", c);
		solve(M,R,C);
	}
	return 0;
}