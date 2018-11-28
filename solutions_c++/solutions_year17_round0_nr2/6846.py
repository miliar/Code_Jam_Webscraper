#include <bits/stdc++.h>
using namespace std;

int main () {
	char num[20];
	//
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; casenum++) {
		scanf("%s", num);
		int start, curr;
		for (start = curr = 0; num[curr] != '\0'; curr++) {
			if (num[curr] > num[start])
				start = curr;
			else if (num[curr] < num[start]) {
				num[start]--;
				for (int i = start+1; num[i] != '\0'; i++)
					num[i] = '9';
				break;
			}
		}
		printf("Case #%d: ", casenum);
		if (num[0] == '0') 
			printf("%s \n", num+1);
		else 
			printf("%s \n", num);
	}
	return 0;
}
