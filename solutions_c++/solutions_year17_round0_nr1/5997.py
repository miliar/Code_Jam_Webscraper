#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

int main() {
freopen("input.txt", "r", stdin);
freopen("output.txt", "w+", stdout);
	
	int testCase;
	scanf("%d", &testCase);

	for (int t = 1; t <= testCase; t++) {

		int fliper;
		char panCakes[1010];
		scanf("%s %d", panCakes, &fliper);

		int panCakesSize = strlen(panCakes);
		int number = 0;

		for (int i = 0; i < panCakesSize - fliper + 1; i++) {
			if (panCakes[i] == '-') {
				for (int j = 0; j < fliper; j++) {
					panCakes[i + j] = panCakes[i + j] == '-' ? '+' : '-';
				}
				number++;
			}
		}

		for (int i = 0; i < panCakesSize; i++) {
			if (panCakes[i] == '-') {
				number = -1;
			}
		}
		printf("Case #%d: ", t);
		number == -1 ? printf("IMPOSSIBLE") : printf("%d", number);
		printf("\n");
	}	

}