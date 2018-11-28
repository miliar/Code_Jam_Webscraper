#include <stdio.h>
#include <string.h>

int main() {

	int k, s, t, cont, flag;
	char vet[1001];
	scanf("%d", &t);
	
	for (int caso = 1; caso <= t; caso++){
		scanf("%s", vet);
		s = strlen(vet);
		scanf("%d", &k);
		
		cont = 0;
		for (int i = 0; i <= s - k; i++){
			if (vet[i] == '-'){
				cont++;
				for (int j = 0; j < k; j++){
					if (vet[i + j] == '-') vet[i + j] = '+';
					else vet[i + j] = '-';
				}
			}
		}
		flag = 1;
		for (int i = 0; i < s; i++){
			if (vet[i] == '-'){
				flag = 0;
				break;
			}
		}
		printf("Case #%d: ", caso);
		if (flag){
			printf("%d\n", cont);
		}
		else{
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}