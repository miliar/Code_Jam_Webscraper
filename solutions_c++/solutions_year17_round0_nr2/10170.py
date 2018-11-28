#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string> 


using namespace std;

int main(int argc, char *argv[]) {
	
	
	int cantCasos;
	string entrada;
	freopen("B-small.in","r",stdin);
	freopen("B-salidaSmall.out","w",stdout);
	cin >> cantCasos;
	int caso = 1;
	while(cantCasos--){
		
		cin >> entrada;
		
		int tamanio = entrada.size();
		
		int i = 0;
		
		if(tamanio == 1) cout << "Case #"<<caso<<": "<< atoi(entrada.c_str()) << endl;
		else{
			while(i <  tamanio - 1){
				if(entrada[i] <= entrada[i+1])
					i++;
				else if(entrada[i] == 49){
					entrada[0] = 48;
					for(int j = 1; j < tamanio; j++)
						entrada[j] = 57;
					entrada.substr(1,tamanio);
				}
				else{
					entrada[i]--;
					for(int j = i+1; j < tamanio; j++)
						entrada[j] = 57;
					i--;
				}
			}
			cout << "Case #"<<caso<<": "<< atoi(entrada.c_str()) << endl;
		}
		
		caso++;
	}

	
	return 0;
}

