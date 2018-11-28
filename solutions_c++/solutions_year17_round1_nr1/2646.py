#include <iostream>
using namespace std;
int main(){
	int zes;
	cin>>zes;
	for(int i = 1; i <= zes; i++){
		int R,C;
		cin>>R>>C;
		char T[R][C];
		for(int i = 0; i < R; i++){
			for(int j = 0; j < C; j++){
				cin>>T[i][j];
			}
		}
		for(int i = 0; i < R; i++){
			for(int j = 0; j < C; j++){
				if(T[i][j] != '?'){
					int y = j - 1;
					while(y > -1 && T[i][y] == '?'){
						T[i][y] = T[i][j];
						y--;
					}
					y = j + 1;
					while(y < C && T[i][y] == '?'){
						T[i][y] = T[i][j];
						y++;
					}
				}
				
			}
		}
		for(int l = 0; l < 25; l++){
			for(int i = 1; i < R; i++){
				for(int j = 0; j < C; j++){
					if(T[i][j] == '?')
						T[i][j] = T[i - 1][j];
				}
			}
			
			for(int i = 0; i < R - 1; i++){
				for(int j = 0; j < C; j++){
					if(T[i][j] == '?')
						T[i][j] = T[i + 1][j];
				}
			}
		}
		
		cout<<"CASE #"<<i<<":"<<endl;
		for(int i = 0; i < R; i++){
			for(int j = 0; j < C; j++){
				cout<<T[i][j];
			}
			cout<<endl;
		}
	}
}

