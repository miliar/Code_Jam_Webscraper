#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

void solvre(){
	int r, c;
	char mapa[30][30];
	cin>>r>>c;
	char linha[30];

	for(int i = 0; i<r; i++){
		for(int j = 0; j<c; j++){
			cin>>mapa[i][j];
		}
	}

	for(int i = 0; i<r; i++){
		linha[i] = 0;
		for(int j = 0; j<c; j++){
			if(mapa[i][j]!='?'){
				linha[i] = mapa[i][j];
				break;
			}
		}
	}

	for(int i = 0; i<r; i++){
		if(linha[i]==0) continue;
		for(int j = 0; j<c; j++){
			if(mapa[i][j]=='?'){
				mapa[i][j] = linha[i];
			}else linha[i] = mapa[i][j];
		}
	}

	for(int i = 1; i<r; i++){
		if(linha[i]==0){
			
			if(mapa[i-1][0]!='?') linha[i] = mapa[i-1][0];
			else continue;

			for(int j = 0; j<c; j++){
				mapa[i][j] = mapa[i-1][j];
			}
		}
	}

	for(int i = r-2; i>=0; i--){
		if(linha[i]==0){
			for(int j = 0; j<c; j++){
				mapa[i][j] = mapa[i+1][j];
			}
		}
	}

	cout<<endl;
	for(int i = 0; i<r; i++){
		for(int j = 0; j<c; j++){
			cout<<mapa[i][j];
		}
		cout<<endl;
	}
}

int main(){
	int t;
	cin>>t;
	for(int i = 1; i<=t; i++){
		printf("Case #%d:", i);
		solvre();
	}
}