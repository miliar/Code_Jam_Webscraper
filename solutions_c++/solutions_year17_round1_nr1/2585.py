//============================================================================
// Name        : .cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <cstring>
#include <map>

using namespace std;

int main() {

	int casos;
	cin >> casos;

	for(int t=1; t<=casos; t++){
		int r, c;
		cin >> r >> c;

		map <char, bool> mymap;

		char matrix[r+20][c+20];
		memset(matrix, '.', sizeof(matrix));


		for(int i =0; i<r; i++){
			string linea;
			cin >> linea;
			for(int j=0; j<c; j++){
				matrix[i][j] = linea[j];
			}
		}

		for(int i =0; i<r; i++){
			for(int j=0; j<c; j++){
				if(matrix[i][j]!='?' and mymap[matrix[i][j]]==false){

					char caracter = matrix[i][j];
		//			cout << caracter << endl;
					//derecha
					int d, ar, ab, iz;
					for(d=j+1; d<c; d++){
						if(matrix[i][d]!='?' and matrix[i][d]!=caracter){
							d--;
							break;
						}
					}

					if(d==c)
						d--;

		//			cout << "d " << d << endl;

					//arriba
					for(ar=i; ar>=0; ar--){
						bool romperi = false;
						for(int jaux = j; jaux<=d; jaux++ ){
							if(matrix[ar][jaux]!='?'  and matrix[ar][jaux]!=caracter){
								ar++;
								romperi = true;
								break;
							}
						}

						if(romperi)
							break;
					}

					if(ar==-1)
						ar++;

		//			cout << "ar " << ar << endl;

					//izquierda
					for(int auxi = i; auxi>=ar; auxi--){
						bool romperi = false;
						for(iz = j; iz>=0; iz--){
							if(matrix[auxi][iz]!='?' and matrix[auxi][iz]!=caracter){
								iz++;
								romperi=true;
								break;

							}
						}

						if(romperi)
							break;
					}

					if(iz==-1)
						iz++;

		//			cout << "iz " << iz << endl;


					//abajo
					for(ab = i; ab<r; ab++){
						bool romperi=false;
						for(int auxj = iz; auxj<=d; auxj++){
							if(matrix[ab][auxj]!='?' and matrix[ab][auxj]!=caracter ){
								ab--;
								romperi=true;
								break;
							}
						}

		//				cout <<" abss" << ab << endl;

						if(romperi)
							break;
					}

					if(ab==r)
						ab--;

		//			cout << "ab " << ab << endl << endl;


					mymap[caracter] = true;

					for(int k=ar; k<=ab; k++){
						for(int l=iz; l<=d; l++){
							matrix[k][l] = caracter;
						}
					}


				}
			}
		}

		cout << "Case #" << t << ":" << endl;

		for(int i =0; i<r; i++){
			for(int j=0; j<c; j++){
				cout << matrix[i][j];
			}
			cout << endl;
		}

	}

	return 0;
}
