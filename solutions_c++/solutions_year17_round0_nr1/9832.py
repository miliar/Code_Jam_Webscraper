#include<stdio.h>
#include<string.h>
#define MAX 10
char string[MAX] = { '\0' };

int change(int n, int k);
void reset();

int main(void){
	int T,k;
	int i, j;
	int ct=0,stat;
	
	scanf("%d", &T);

	for(i = 0; i < T; i++){
		scanf("%s", string);
		scanf("%d", &k);

		for (j = 0; j < strlen(string); j++){
			if (string[j] == '-'){
				stat = change(j, k);
				ct++;
			}
			if (stat){
				printf("Case #%d: IMPOSSIBLE\n", i+1);
				break;
			}
		}
		if (stat == 0){
			printf("Case #%d: %d\n", i+1,ct);
		}
		ct = 0;
		reset();
		stat = 0;
	}

	scanf("%d", i);
	return 0;
}

int change(int n, int k){
	int i = 0;
	for (i = n; i < n + k; i++){
		if (i>=strlen(string)){
			return 1;
		}
		if (string[i] == '-'){
			string[i] = '+';
		}
		else{
			string[i] = '-';
		}
	}
	return 0;
}

void reset(){
	int i;
	for (i = 0; i < MAX; i++){
		string[i] = '\0';
	}
}