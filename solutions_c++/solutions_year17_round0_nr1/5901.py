/*
 * A.cc
 *
 *  Created on: Apr 7, 2017
 *      Author: ra162554
 */

#include <iostream>
#include <cstdio>
#include <cstring>
#define MAX 1002

using namespace std;

void flip(char cadena[] , int indice , int longitud){
	for (int i = 0; i < longitud; ++i, indice++) {
		if (cadena[indice] == '-')
			cadena[indice] = '+';
		else
			cadena[indice] = '-';
	}
}

int main(){

	int test_cases;
	scanf("%d",&test_cases);
	for (int test_number = 0; test_number < test_cases; ++test_number) {
		int resp = 0, K;
		char cadena[MAX];
		scanf("\n%s %d",cadena, &K);
		for (int i = 0; i < (int)strlen(cadena) - K + 1; ++i) {
			if (cadena[i] == '-'){
				flip( cadena , i , K);
				resp++;
			}
		}
		for (int i = 0; i < (int)strlen(cadena); ++i)
			if (cadena[i] == '-')
				resp = -1;

		printf("Case #%d: ",test_number+1);

		if (resp == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", resp);
	}

	return 0;
}

