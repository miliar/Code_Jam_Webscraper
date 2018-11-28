#include <iostream> 
using namespace std;

void solve_case(int T){
  int R, C;
  cin >> R >> C;
  char cake[R][C];
  char inp;

  for (int i = 0; i < R; i++){
  	for (int j = 0; j < C; j++){
  		cin >> inp;
  		cake[i][j] = inp;
  	}
  }

  for (int i = 0; i < R; i++){
  	for (int j = 0; j < C; j++){
  		if (cake[i][j] == '?'){
  			for (int k = j; k < C; k++){
  				if (cake[i][j] == '?' && cake[i][k] != '?'){
  					cake[i][j] = cake[i][k];
  				}
  			}
  			for (int k = j; k >= 0; k--){
  				if (cake[i][j] == '?' && cake[i][k] != '?'){
  					cake[i][j] = cake[i][k];
  				}
  			}
  		}
  	}
  }

  cout << "Case #" << T << ": " << endl;

  int col = -1;
  for (int i = 0; i < R; i++){
  	col = -1;
  	if (cake[i][0] == '?'){
  		for (int j = i; j < R; j++){
  			if (cake[j][0] != '?' && col < 0){
  				col = j;
  			}
  		}
  		for (int j = i; j >= 0; j--){
  			if (cake[j][0] != '?' && col < 0){
  				col = j;
  			}
  		}
  	} else {
  		col = i;
  	}
  	for (int j = 0; j < C; j++){
  		cout << cake[col][j];
  	}
  	cout << endl;
  }
}

int main() {
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  	solve_case(i);
  	}
  	return 0;
}