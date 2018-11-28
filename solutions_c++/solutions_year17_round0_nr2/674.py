#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main(void) {
	int T, digit[64], len, i, j, trimmed_leading_zero;
	
	cin >> T;
	for (int t=1; t<=T; t++) {
		printf("Case #%d: ", t);
		string s;
		cin >> s;
		len = s.size();
		digit[0] = 0;
		for (i=0; i<len; i++) digit[i+1] = s[i] - '0';
		//for (i=0; i<len+1; i++) printf("%d", digit[i]); printf("\n");
		for (i=len; i>0; i--) {
			if (digit[i] < digit[i-1]) {
				for (j=i; j<len+1; j++) digit[j] = 9;
				digit[i-1]--;	//must have been at least 1
			}
		}
		trimmed_leading_zero = 0;
		for (i=0; i<len+1; i++) {
			if (digit[i] != 0) trimmed_leading_zero = 1;
			if (trimmed_leading_zero) printf("%d", digit[i]);
		}
		printf("\n");
	}
	
	return 0;
}