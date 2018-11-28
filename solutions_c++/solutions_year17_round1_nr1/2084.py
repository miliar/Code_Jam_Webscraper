#include <bits/stdc++.h>

using namespace std;

int r, c;

void asignar(int i, int j, vector<vector<char> > &vc){
	if(vc[i][j]=='?'){
		if(i>0){ // puede arriba
			if(vc[i-1][j]!='?'){
				vc[i][j] = vc[i-1][j];
			}
			else{
				asignar(i-1,j,vc);
				vc[i][j] = vc[i-1][j];
			}
			return;
		}
	}
}

void asignar2(int i, int j, vector<vector<char> > &vc){
	if(vc[i][j]=='?'){
		if(i<r-1){ // puede arriba
			if(vc[i+1][j]!='?'){
				vc[i][j] = vc[i+1][j];
			}
			else{
				asignar2(i+1,j,vc);
				vc[i][j] = vc[i+1][j];
			}
			return;
		}
	}
}

void asignar3(int i, int j, vector<vector<char> > &vc){
	if(vc[i][j]=='?'){
		if(j>0){ // puede izq
			if(vc[i][j-1]!='?'){
				vc[i][j] = vc[i][j-1];
			}
			else{
				asignar3(i,j-1,vc);
				vc[i][j] = vc[i][j-1];
			}
			return;
		}
	}
}

void asignar4(int i, int j, vector<vector<char> > &vc){
	if(vc[i][j]=='?'){
		if(j<c-1){ // puede izq
			if(vc[i][j+1]!='?'){
				vc[i][j] = vc[i][j+1];
			}
			else{
				asignar4(i,j+1,vc);
				vc[i][j] = vc[i][j+1];
			}
			return;
		}
	}
}

int main(){

	int tc;
	scanf("%d",&tc);

	for(int x=0 ; x<tc;x++){
		
		scanf("%d %d",&r,&c);

		vector<vector<char> > vc;
		vc.assign(r,vector<char>(c));

		for(int i=0 ; i<r; i++){
			string aux;
			cin >> aux;
			// cout << aux ;
			for(int j=0 ; j<c; j++){
				vc[i][j] = aux[j];
				// cout << vc[i][j];
			}
			// cout << endl;
		}

		for(int i=r-1 ; i>=0; i--){
			for(int j=c-1 ; j>=0; j--){
				if(vc[i][j] == '?'){

					asignar2(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar2(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar3(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar4(i,j,vc);

				}
			}
		}

		for(int i=0 ; i<r; i++){
			for(int j=0 ; j<c; j++){
				if(vc[i][j] == '?'){

					asignar(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar2(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar3(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar4(i,j,vc);

				}
			}
		}

		for(int i=0 ; i<r; i++){
			for(int j=0 ; j<c; j++){
				if(vc[i][j] == '?'){

					asignar3(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar2(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar3(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar4(i,j,vc);

				}
			}
		}

		for(int i=r-1 ; i>=0; i--){
			for(int j=c-1 ; j>=0; j--){
				if(vc[i][j] == '?'){

					asignar4(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar2(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar3(i,j,vc);

					// if(vc[i][j] == '?')
					// 	asignar4(i,j,vc);

				}
			}
		}

		cout << "Case #" <<x+1<<":"<<endl;
		for(int i=0 ; i<r; i++){
			for(int j=0 ; j<c; j++){
				cout << vc[i][j];
			}
			cout << endl;
		}
		// cout << endl;

	}
}