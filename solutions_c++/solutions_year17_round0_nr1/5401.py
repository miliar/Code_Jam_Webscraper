
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

char s[1001];

int allhappy(int k, int length) {
	for (int i = 0; i<length; i++) {
		if (s[i] == '-') {
			//printf("%d is -\n", i);
			return 0;
		}
	}
	return 1;
}


int howmanytimes(int k, int length) {
	int count = 0;

	for (int i = 0; i <= length - k; i++) {
		if (s[i] == '-') {
			for (int j = i; j<k + i; j++) {
				if (s[j] == '-') {
					s[j] = '+';
				}
				else {
					s[j] = '-';
				}

			}
			count++;
			//printf("count up\n");
		}
		//printf("%s\n", s);
	}

	if (allhappy(k, length) == 1) {
		return count;
	}
	else {
		return 999999;
	}
}



int main() {

	FILE *fp = fopen("1out.txt", "w");
	freopen("1in.txt", "r", stdin);
	int t;
	int k;

	cin >> t;
	for (int i = 1; i <= t; i++) {
		scanf("%s", s);
		scanf("%d", &k);

		string temp = s;
		int length = (int)temp.length();

		int answer = howmanytimes(k, length);
		if (answer == 999999) {
			printf("Case #%d: IMPOSSIBLE\n",i);
			fprintf(fp, "Case #%d: IMPOSSIBLE\n",i);
		}
		else {
			printf("Case #%d: %d\n", i,answer);
			fprintf(fp, "Case #%d: %d\n",i, answer);
		}

	}
}

