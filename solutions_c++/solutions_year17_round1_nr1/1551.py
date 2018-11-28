#include <bits/stdc++.h>

using namespace std;

string T[50];
int NC = 1;

int main(){

	int TC;
	cin>>TC;	
	while(TC--){
		int R, C;
		
		cin>>R>>C;
		
		for(int i = 0 ; i<R ;i++){
				cin>>T[i];	
		}	

		for(int i = 0; i<R ;i++){
			for(int j = 0 ; j<C ;j++){
				if(T[i][j] != '?'){
					for(int jj = j-1 ;jj>=0 && T[i][jj]=='?' ; jj--){
						T[i][jj] = 	T[i][j];
					}	
					for(int jj = j+1 ; jj<C && T[i][jj] == '?'; jj++){
						T[i][jj] = T[i][j];	
					}
				}	
			}	
		}
		for(int count = 0; count<50 ;count++){
		for(int i = 1 ; i<R ;i++){
			if(T[i][0] == '?' && i-1>=0){
				for(int j = 0 ; j<C ;j++){
					T[i][j] = T[i-1][j];	
				}	
			}	
		}
		
			}
	for(int count = 0 ; count<50 ;count++){
			for(int i = R-1 ; i>= 0; i--){
			if(T[i][0] == '?' && i+1<C){
				for(int j = 0 ; j<C ;j++){
					T[i][j] = T[i+1][j];	
				}	
			}	
		}
	
	}	
		
		cout<<"Case #"<<NC++<<":"<<endl;

		for(int i = 0 ; i<R ;i++){
			cout<<T[i]<<endl;
		}
		
	}


	return 0;	
}
