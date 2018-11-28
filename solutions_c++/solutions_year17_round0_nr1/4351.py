#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main() {
	char str[1010];
	int T, K;
	scanf("%d", &T);
	for(int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		scanf("%s %d", str, &K);
		// cout << str << endl << endl;
		int i, num = 0;
		int len = strlen(str);
		for(i = 0; str[i] != '\0'; ) {
			if(str[i] == '+')
				i++;
			else {
				
				for(int j = i; j < i + K && i + K <= len ; j++) {
					str[j] = str[j] == '+' ? '-': '+';
				}
				// for(int q = 0; str[q] != '\0'; q++)
					// cout << str[q];
				// cout << endl;
				num++;
				i++;
			}
		}
		int imp = 0;
		for(int i = 0; str[i] != '\0'; i++) {
			if(str[i] == '-') {
				imp = 1;
			}

		}
		if(imp)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << num << endl;
		for(int i = 0; i < len; i++) str[i] = '\0';

	}

}