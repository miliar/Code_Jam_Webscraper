#include <bits/stdc++.h>
using namespace std;

int main() {
	char str[1001];
	int sz, count;
	//
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; casenum++) {
		count = 0;
		scanf("%s %d", str, &sz);
		int i;
		for (i = 0; str[i+sz-1] != '\0'; i++) {
			if (str[i] == '-') {
				count++;
				// flip
				for (int j = i; j < i+sz; j++) {
					if (str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
				}
			}
		}
		printf("Case #%d: ", casenum);
		for ( ; str[i] != '\0'; i++)
			if (str[i] == '-')
				break;
		if (str[i] == '-') 
			printf("IMPOSSIBLE \n");
		else 
			printf("%d \n", count);
	}
	return 0;
}
