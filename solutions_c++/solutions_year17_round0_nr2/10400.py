#include<iostream>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

char* decrementNumber( char* number );

int main() {
	int T; char number[19];
	cin >> T;
	fgets(number, sizeof(number), stdin);

	for(int i = 0; i < T; i++) {
		fgets(number, sizeof(number), stdin);
		for(   ;   ;   ) {
			int numlen = strlen(number);
			if(numlen == 2) {
				printf("Case #%d: %s", i + 1, number);
				goto start;
			}
			for(int j = 0; j < numlen - 2; j++) {
				if(number[j] > number[j+1]) {
					char *result = decrementNumber( number );
					strcpy(number, result);
					break;
				}
				if(j == numlen - 3) {
					printf("Case #%d: ", i + 1);
					bool printall = false;
					for(int a = 0; a < strlen(number); a++) {
						if(printall || number[a] != '0') {
							printf("%c", number[a]);
							printall = true;
						}
					}
					printf("");
					goto start;
				}
			}
		}
		start: printf("");
	}
}

char *decrementNumber( char* number ) {
	int numlen = strlen(number);
	for(int j = numlen - 2; j > -1; j--) {
		number[j]--;
		if(number[j] - '0' < 0) {
			number[j] = '9';
		} else return number;
	}
	return number;
}
