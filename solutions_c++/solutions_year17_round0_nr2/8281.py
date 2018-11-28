#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;
typedef unsigned int uint;

int T;
char N[19];

void solve(int c){
	scanf("%s", N);
	for(int i = strlen(N) - 2; i >= 0; i--){
		if(N[i] > N[i + 1]){
			--N[i];
			for(int j = i + 1; j < strlen(N); j++)
				N[j] = '9';
		}
	}

	printf("Case #%d: ", c);
	for(int i = 0; i < strlen(N); i++)
		if(i > 0 || N[i] != '0')
			printf("%c", N[i]);
	printf("\n");
}

int main(){
	scanf("%d", &T);
	for(int i = 0; i < T; i++)
		solve(i + 1);
}
