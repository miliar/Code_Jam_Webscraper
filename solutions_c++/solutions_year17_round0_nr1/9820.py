#include <iostream>
#include <vector>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include <string>


using namespace std;

	string te_la_volteo(string s, int K, int j){
		int q;
		for(q=j; q<j+K; q++){
			if(s[q] == '-'){
				s[q] = '+';
			}
			else {
				s[q] = '-';
			}
		}
		return s;
	}


int main(){
	int T,K[100],x[100],long_cadena[100],cont[100],valido[100];
	string S[100];
	cin >> T;

	for(int i=0;i<T;i++){
		cont[i] = 0;
		cin >> S[i] >> K[i];
		int m=0;
		long_cadena[i] = 0;
		while (S[i][m] != '\0'){
			long_cadena[i]++;
			m++;
		}
		if ((long_cadena[i] >= 2) && (long_cadena[i] <= 1000)){
			long_cadena[i]= long_cadena[i] - K[i] + 1;
			for(int j=0; j<long_cadena[i];j++){
				if (S[i][j] == '-'){
					S[i] = te_la_volteo(S[i],K[i],j);
					cont[i]++;
				}
			}
			long_cadena[i] = long_cadena[i] + K[i] - 1;
			x[i] = i+1;
			valido[i] = 0;
			for(int j=0; j<long_cadena[i];j++){
				if(S[i][j] == '+'){
					valido[i]=2*valido[i];
				}
				else{
					valido[i] =-1;
				}
			}
		}
	}
	for (int i=0; i<T; i++){
		if (long_cadena[i] >= 2 & long_cadena[i] <= 1000){
			if (valido[i] == 0){
				cout << "Case #" << x[i] << ": " << cont[i] << endl;
			}
			else{
				cout << "Case #" << x[i] << ": " << "IMPOSSIBLE" << endl;
			}
		}
	}

	return 0;
}
