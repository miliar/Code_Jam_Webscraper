#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

char cake[26][26];

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		printf("Case #%d:\n", t);
		int R, C;
		cin >> R >> C;
		for(int i = 1; i <= R; i++)
			for(int j = 1; j <= C; j++)
				cin >> cake[i][j];


		for(int repeat = 1; repeat <= C; repeat++){			
			for(int i = 1; i <= R; i++){
				for(int j = 1; j < C; j++){
					if(cake[i][j] == '?')
						if(cake[i][j+1] != '?')
							cake[i][j] = cake[i][j+1];
					
					if(cake[i][j] != '?')
						if(cake[i][j+1] == '?')
							cake[i][j+1] = cake[i][j];
						
				}
			}
		}

		for(int repeat = 1; repeat <= R; repeat++){			
			for(int i = 1; i < R; i++){
				for(int j = 1; j <= C; j++){
					if(cake[i][j] == '?')
						if(cake[i+1][j] != '?')
							cake[i][j] = cake[i+1][j];
					
					if(cake[i][j] != '?')
						if(cake[i+1][j] == '?')
							cake[i+1][j] = cake[i][j];
						
				}
			}
		}

		for(int i = 1; i <= R; i++){
			for(int j = 1; j <= C; j++){
				cout << cake[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}

