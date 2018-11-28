#include <bits/stdc++.h>
using namespace std;

char Cake[30][30];
int R, C;

void fill(int i, int j, char filler) {
	if (filler == '?' || j < 0 || j > C)
		return;
	else if (Cake[i][j] == '?') {
		Cake[i][j] = filler;
		fill(i, j - 1, Cake[i][j]);
		fill(i, j + 1, Cake[i][j]);
	}
}

void copy(int i, int j) {

}

int main() {

	freopen("A-large (1).in", "r", stdin);
	freopen("A-large (1).out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		memset(Cake, 0, sizeof(Cake));
		cin >> R;
		cin >> C;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				cin >> Cake[i][j];

		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				if (Cake[i][j] != '?') {
					fill(i, j + 1, Cake[i][j]);
					fill(i, j - 1, Cake[i][j]);
				}

		for (int i = 0; i < R; i++)
			if (Cake[i][0] == '?' && Cake[i - 1][0] != '?' && i - 1 >= 0) {
				strcpy(Cake[i], Cake[i - 1]);
			}

		for (int i = R-1; i >= 0; i--)
			if (Cake[i][0] == '?' && Cake[i + 1][0] != '?' && i + 1 < R) {
				strcpy(Cake[i], Cake[i + 1]);
			}

		cout << "Case #" << t + 1 << ":\n";
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++)
				cout << Cake[i][j];
			cout << endl;
		}
	}
}
