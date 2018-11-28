#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;
char A[19];

void zeros(int ind){
	for (; ind > 0 && A[ind - 1] > A[ind]; ind--){
		A[ind] = '9';
		A[ind - 1] --;
	}
}
int main(){
	/*freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);*/
	int T, len;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%s", &A);
		len = strlen(A);
		for (int j = 0; j < len - 1; j++){
			if (A[j] <= A[j + 1])continue;
				A[j]--;
			for (int k = j + 1; k < len; k++) A[k] = '9';
			A[j + 1] = '9';
			zeros(j);
		}
		printf("Case #%d: ", i);
		for (int i = 0; i < len; i++){
			if (A[i] != '0')
				printf("%c", A[i]);
		}
		printf("\n");
	}
	return 0;
}