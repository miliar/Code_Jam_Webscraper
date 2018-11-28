#include <iostream>
#include <algorithm>
#include <vector>
#define UP 0
#define DOWN 1
#define LEFT 2
#define RIGHT 3
using namespace std;
char cake[26][26];
int R;
int C;
void initCake(){
	for(int r = 0 ; r < 26 ; r++){
			for(int c = 0 ; c < 26; c++){
				cake[r][c] = ' ';
		}
	}
}

int main(){
	int T = 0;
	cin >> T;
	for(int idx = 0 ; idx < T ; idx++){
		R = 0;
		C = 0;
		cin >> R >> C ;
		
		for(int r = 0 ; r < R ; r++){
			for(int c = 0 ; c < C; c++){
				char initial;
				cin >> cake[r][c];
			}
		}

		for(int r = 0 ; r < R ; r++){
			for(int cc= 0 ; cc < C; cc++){
			for(int c = 0 ; c < C; c++){
				if(cake[r][c] != '?'){
					if(c - 1 >= 0){
						if(cake[r][c-1] == '?'){
							cake[r][c-1] = cake[r][c];
						}
					}

					if(c + 1 < C){
						if(cake[r][c+1] == '?'){
							cake[r][c+1] = cake[r][c];
						}
					}
				}

			}
			}
		}

		for(int c = 0 ; c < C ; c++){
			for(int rr = 0 ; rr < R; rr++){
			for(int r = 0 ; r < R; r++){
				if(cake[r][c] != '?'){
					if(r - 1 >= 0){
						if(cake[r-1][c] == '?'){
							cake[r-1][c] = cake[r][c];
						}
					}

					if(r + 1 < R){
						if(cake[r+1][c] == '?'){
							cake[r+1][c] = cake[r][c];
						}
					}
				}
			}
			}
		}
		cout << "Case #" << idx+1 << ":" << endl;
		for(int r = 0 ; r < R ; r++){
			for(int c = 0 ; c < C; c++){
				cout << cake[r][c] ;
			}cout << endl;
		}

		initCake();
	}

	return 0;
} 