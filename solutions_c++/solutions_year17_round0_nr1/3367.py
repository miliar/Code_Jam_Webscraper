#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
	int T, cont = 1, k;
	char str[1005];

	cin >> T;
	while(T--) {
		int turn = 0;

		scanf(" %s ", str);
		cin >> k;

		for(int i = 0; i < strlen(str); i++) {
			if(str[i] == '-') {
				if(strlen(str) - i < k)
					break;
				for(int j = i; j < i + k; j++)
					if(str[j] == '+')
						str[j] = '-';
					else
						str[j] = '+';
				turn++;
			}
		}

		for(int i = 0; i < strlen(str); i++)
			if(str[i] == '-') {
				cout << "Case #" << cont++ << ": IMPOSSIBLE" << endl;
				k = -1;
				break;
			}

		if(k >= 0)
			cout << "Case #" << cont++ << ": " << turn << endl;
	}

	return 0;
}