#include <iostream>

using namespace std;

int R, C;
char mat[200][200];

void ans() {
	static int tc = 1;
	cout << "Case #" << tc++ << ":\n";
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cout << mat[i][j];
		}
		cout << '\n';
	}
}

int main() {
	int T;
	cin >> T;
	while (T--) {
		cin >> R >> C;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				cin >> mat[i][j];
				if (j > 0 && mat[i][j] == '?' && mat[i][j - 1] != '?') {
					mat[i][j] =  mat[i][j - 1];
				}
			}
			bool allQ = true;
			for (int j = 0; j < C; j++) {
				if (mat[i][j] != '?') allQ = false;
			}
			if (allQ) {
				continue;
			}
			if (mat[i][0] == '?') {
				char first = '?';
				for (int j = 0; j < C && first == '?'; j++) {
					first = mat[i][j];
				}
				for (int j = 0; j < C && mat[i][j] == '?'; j++) {
					mat[i][j] = first;
				}
			}
		}
		bool change = true;
		while (change) {
			change = false;
			for (int i = 0; i < R; i++) {
				if (mat[i][0] != '?') {
					if (i > 0 && mat[i - 1][0] == '?') {
						for (int j = 0; j < C; j++) {
							mat[i - 1][j] = mat[i][j];
						}
						change = true;
					}
					if (i + 1 < R && mat[i + 1][0] == '?') {
						for (int j = 0; j < C; j++) {
							mat[i + 1][j] = mat[i][j];
						}
						change = true;
					}
				}
			}
		}
		ans();
	}
}
