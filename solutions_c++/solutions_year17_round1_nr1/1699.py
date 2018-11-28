#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int tc;
	cin >> tc;
	for (int q = 1; q <= tc; q++) {
		int r,c;
		char arr[35][35], dummy;
		bool donotuse[35][35];
		for (int i =0; i < 35; i++) {
			for (int j = 0; j < 35; j++) {
				donotuse[i][j] = false;
			}
		}
		cin >> r >> c;
		scanf("%c", &dummy);
		for (int i = 0; i < r; i++) {
			for (int j = 0;j < c; j++) {
				char temp;
				scanf("%c", &temp);
				arr[i][j] = temp;
			}
			scanf("%c", &dummy);
		}
		for (int i = 0; i < r; i++) {
			for (int j = 1; j < c; j++) {
				if (arr[i][j] != '?') continue;
				arr[i][j] = arr[i][j-1];
			}
			for (int j = c-2; j >= 0; j--) {
				if (arr[i][j] != '?') continue;
				arr[i][j] = arr[i][j+1];
			}
		}
		for (int j = 0; j < c; j++) {
			for (int i = 1; i < r; i++) {
				if (arr[i][j] != '?') continue;
				arr[i][j] = arr[i-1][j];
			}
			for (int i = r-2; i >= 0; i--) {
				if (arr[i][j] != '?') continue;
				arr[i][j] = arr[i+1][j];
			}
		}
		printf("Case #%d: \n", q);
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				printf("%c", arr[i][j]);
			}
			cout << endl;
		}
	}
	return 0;
}