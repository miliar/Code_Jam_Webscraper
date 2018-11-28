#include <bits/stdc++.h>
using namespace std;
const int MAX = 30;
int N, M;
char A[30][30];
int main(){
	int t; cin >> t;
	int cs = 0;
	while(t--){
		++cs;
		cout << "Case #" << cs << ":\n";

		cin >> N >> M;
		int x = 0, y = 0;
		for(int i=1; i<=N; ++i){
			for(int j=1; j<=M; ++j){
				cin >> A[i][j];
				if(A[i][j] != '?'){
					if(x == 0){
						x = i, y = j;
					}
				}
			}
		} 

		for(int i=1; i<=y; ++i) A[x][i] = A[x][y];
		for(int i=y+1; i<=M; ++i){
			if(A[x][i] != '?');
			else A[x][i] = A[x][i - 1];
		}

		for(int i=x-1; i>0; --i){
			int c = 0;
			for(int j=1; j<=M; ++j){
				if(A[i][j] != '?'){
					c = j;
					break;
				}
			}
			if(c){
				for(int j=1; j<c; ++j) A[i][j] = A[i][c];
				for(int j=c+1; j<=M; ++j){
					if(A[i][j] != '?');
					else A[i][j] = A[i][j - 1];
				}
			}
			else{
				for(int j=1; j<=M; ++j) A[i][j] = A[i + 1][j];
			}
		}

		for(int i=x+1; i<=N; ++i){
			int c = 0;
			for(int j=1; j<=M; ++j){
				if(A[i][j] != '?'){
					c = j;
					break;
				}
			}
			if(c){
				for(int j=1; j<c; ++j) A[i][j] = A[i][c];
				for(int j=c+1; j<=M; ++j){
					if(A[i][j] != '?');
					else A[i][j] = A[i][j - 1];
				}
			}
			else{
				for(int j=1; j<=M; ++j) A[i][j] = A[i - 1][j];
			}	
		}

		for(int i=1; i<=N; ++i){
			for(int j=1; j<=M; ++j){
				cout << A[i][j];
			} cout << endl;
		}
	}
}