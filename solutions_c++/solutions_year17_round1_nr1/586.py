#include <iostream>
#include <utility>
#include <string>
#include <vector>

using namespace std;


char cake[26][26];
char Top;
int j_0;
char Left[26];
int main(int argc, char *argv[]){
	int T = 0;
	cin >> T;
	for(int I = 1; I <= T; I++){
		int R = 0, C = 0;
		cin >> R >> C;
		for(int j = 1; j <= R; j++){
			for(int i = 1; i <= C; i++){
				cin >> cake[j][i];
			}
		}
		for(int j = 1; j <= R; j++){
			Left[j] = '_';
			for(int i = 1; i<= C; i++){
				if(cake[j][i] != '?'){
					Left[j] = cake[j][i];
					break;
				}
			}
		}
		j_0 = 0;
		for(int j = 1; j<= R; j++){
			if(Left[j] != '_'){
				j_0 = j;
				break;
			}
		}


		char cur = '_';
		for(int i = 1; i <= C; i++){
			// filling cake[j_0][i]
			if(cake[j_0][i] == '?'){
				if(cur == '_'){
					cake[j_0][i] = Left[j_0];
				}
				else{
					cake[j_0][i] = cur;
				}
			}
			else{
				cur = cake[j_0][i];
			}
		}
		for(int j = j_0 - 1; j >= 1; j--){
			for(int i = 1; i <= C; i++){
				cake[j][i] = cake[j_0][i];
			}
		}
		for(int j = j_0 + 1; j <= R; j++){
			if(Left[j] == '_'){
				for(int i = 1; i <= C; i++){
					cake[j][i] = cake[j-1][i];
				}
			}
			else{
				cur = '_';
				for(int i = 1; i <= C; i++){
			// filling cake[j_0][i]
					if(cake[j][i] == '?'){
						if(cur == '_'){
							cake[j][i] = Left[j];
						}
						else{
							cake[j][i] = cur;
						}
					}
					else{
						cur = cake[j][i];
					}
				}
			}
		}


		cout << "Case #" << I << ":" << endl;
		for(int j = 1; j <= R; j++){
			for(int i = 1; i <= C; i++){
				cout << cake[j][i];
			}
			cout << endl;
		}
	
	}
	return 0;
}