#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;

int main(){

	int T;
	int N,M;
	bool hay;
	vector<string> mapa;

	optimizar_io(0);

	cin >> T ; 

	for(int caso = 1 ; caso <= T; caso++){
		cin >> N >> M; 	
		cout << "Case #" << caso << ":\n";

		mapa = vector<string>(N);		
		for(int i = 0 ; i < N ; i ++){
			cin >> mapa[i] ;	
			hay = false;	
			for(int j = 0 ; j < M ; j ++){
				if( mapa[i][j] != '?' ){
					hay = true;
					break;
				}
			}
			if(!hay && i){
				for(int j = 0 ; j <  M ; j ++)
					mapa[i][j] = mapa[i-1][j];				
			} else if(hay){
				int j  = 0 ;
				while(mapa[i][j] == '?' && j < M) 
					j++;
				for(int k = j ; k >= 0 ; k--)
					mapa[i][k] = mapa[i][j];
				char ant ;
				while(j < M){
					if(mapa[i][j] != '?') ant = mapa[i][j];
					mapa[i][j] = ant;
					j++;
				}
			}
		}		
		int i = 0 ;
		while(mapa[i][0] == '?') i++;
		i--;
		while(i >= 0){
			for(int j = 0 ; j < M ; j ++)
				mapa[i][j] = mapa[i+1][j];
			i--;
		}		

		for(int i = 0 ; i < N ; i ++)	
			cout << mapa[i] << '\n';
	}

	return 0;
}