#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int next() {int x; cin >> x; return x;}

int main() {

	int tests = next();

	int len = 720;
	vector<vector<vector<int>>> minch(len + 2, vector<vector<int>>(len + 2, vector<int>(2)));
	for (int test = 1; test <= tests; test++) {
		vector<int> who(2 * len + 3, -1);

		int ac = next();
		int aj = next();

		for (int i = 0; i < ac; i++) {
			int a = next();
			int c = next();
			for (int j = a; j < c; j++) who[j] = 0;
		}
		
		for (int i = 0; i < aj; i++) {
			int a = next();
			int c = next();
			for (int j = a; j < c; j++) who[j] = 1;
		}
		
		int answ = 2 * len + 5;

		for (int start = 0; start < 2; start++) {
			for (int i = 0; i <= len; i++)
				for (int j = 0; j <= len; j++) 
					for (int last = 0; last < 2; last++) minch[i][j][last] = 2 * len + 5;

			minch[0][0][start] = 0;

			for (int i = 0; i <= len; i++)
				for (int j = 0; j <= len; j++) {
					if (who[i + j] != 1) {
						minch[i][j + 1][1] = min(minch[i][j + 1][1], minch[i][j][1]);
						minch[i][j + 1][1] = min(minch[i][j + 1][1], minch[i][j][0] + 1);												
					}
					if (who[i + j] != 0) {
						minch[i + 1][j][0] = min(minch[i + 1][j][0], minch[i][j][0]);
						minch[i + 1][j][0] = min(minch[i + 1][j][0], minch[i][j][1] + 1);
					}
				}

			answ = min(answ, minch[len][len][start]);
			//answ = min(answ, minch[len][len][start ^ 1] + 1);
		}


		printf("Case #%d: %d\n", test, answ);
	}
}