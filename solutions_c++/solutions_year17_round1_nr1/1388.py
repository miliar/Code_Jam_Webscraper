#include <cstdio>
#include <vector>

using namespace std;

typedef vector<char> vc;
typedef vector<vc> vvc;

bool ok(vvc &v, int j) {
	int n = v.size();
	int m = v[0].size();

	for (int i = 0; i < n; i++) {
		if (v[i][j] != '?') return true;
	}

	return false;
}

void correct(vvc &v, int j) {
	int n = v.size();
	int m = v[0].size();

	if (ok(v, j)) return;

	if (j == 0) {
		correct(v, j + 1);
		for (int i = 0; i < n; i++) v[i][j] = v[i][j + 1];
	} else if (ok(v, j - 1)) {
		for (int i = 0; i < n; i++) v[i][j] = v[i][j - 1];
	} else {
		correct(v, j + 1);
		for (int i = 0; i < n; i++) v[i][j] = v[i][j + 1];
	}
}

int main(void) {
	int t;
	scanf("%d", &t);

	// Para cada caso de teste.
	for (int tc = 1; tc <= t; tc++) {
		int n, m;
		scanf("%d %d", &n, &m);

		vvc input(n, vc(m));
		vvc output(n, vc(m));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf(" %c", &input[i][j]);
				output[i][j] = input[i][j];
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (output[i][j] != '?') {
					char ch = output[i][j];

					for (int ii = i - 1; ii >= 0 and output[ii][j] == '?'; ii--) {
						output[ii][j] = ch;
					}

					for (int ii = i + 1; ii < n and output[ii][j] == '?'; ii++) {
						output[ii][j] = ch;
					}
				}
			}
		}

		for (int j = 0; j < m; j++) {
			correct(output, j);
		}

		printf("Case #%d:\n", tc);

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				printf("%c", output[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}