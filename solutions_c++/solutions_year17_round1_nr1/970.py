#include<iostream>

using namespace std;

int t,r,c;
char tab[29][29];
char res[29][29];

int main(){
	ios_base::sync_with_stdio(0);
	cin >> t;
	for(int test = 0; test < t; test++){
		cin >> r >> c;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				cin >> tab[i][j];
				res[i][j] = '?';
			}
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(tab[i][j] != '?'){
					char akt = tab[i][j];
					int koniec = (c-1);
					for(int k = (j+1); k < c; k++){
						if(tab[i][k] != '?'){
							koniec = (k - 1);
							break;
						}
					}
					
					for(int w = i; w >= 0; w--){
						for(int k = koniec; k >= 0; k--){
							if(res[w][k] == '?')
								res[w][k] = akt;
						}
					}
					
				}
			}
		}
		for(int i = 1; i < r; i++){
			for(int j = 0; j < c; j++){
				if(res[i][j] == '?')
					res[i][j] = res[i-1][j];
			}
		}
			
		cout << "Case #"<<test+1<<": \n";
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				cout << res[i][j];
			}
			cout <<endl;
		}
	}


return 0;
}