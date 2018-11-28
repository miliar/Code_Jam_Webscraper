#include <stdio.h>
#include <iostream>

using namespace std;

#define MAXN 30

int main () {
	int T;

	cin>>T;

	for(int i = 0 ; i < T ; i++){
		string numero;

		cin>>numero;

		
		int j;

		for(j = 0 ; j < numero.length() ; j++)
			numero[j] = numero[j]-'0';

		int verif = 0, indice=-1;

		for(j=0; j < numero.length()-1 ; j++){
			//printf("comp %d==%d\n",indice,j);
			if(numero[j]>numero[j+1]){
				//printf("antes %i depois %i\n",numero[j],numero[j]-1);
				numero[j] = numero[j]-1;
				//printf("antes %i depois 9\n",numero[j+1]);
				numero[j+1] = 9;
				if(!verif){
					indice = j;
					verif = 1;
				}
				j=-1;
				
			}
			else if(indice==j){
				//printf("asdfas\n");
				break;
			}
			
		}
		//printf("indices = %d = %c\n",indice+1,numero[indice+1]);
		if(indice!=-1)
			for(j = indice+1 ; j<numero.length() ; j++){
				numero[j] = 9;
			}

		if(numero.length()>0)
			for(j = 0 ; numero[j]==0 ; j++);

		printf("Case #%d: ", i+1);

		for(; j<numero.length(); j++){
			printf("%i",numero[j]);
		}
		printf("\n");

	}

	return 0;
}
