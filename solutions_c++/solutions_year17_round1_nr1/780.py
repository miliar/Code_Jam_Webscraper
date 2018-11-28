#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

const int SIZE = 25;
int solved[SIZE][SIZE][SIZE][SIZE];
char solution[SIZE][SIZE][SIZE][SIZE][SIZE][SIZE];

int n, m;
vector<string> mat;

int numLetters[SIZE][SIZE][26];
void calcNumLetters() {
	memset(numLetters, 0, sizeof(numLetters));
	if (mat[0][0] != '?')
		numLetters[0][0][mat[0][0] - 'A'] = 1;
	for (int i = 1; i < n; i++) {
		memcpy(numLetters[i][0], numLetters[i - 1][0], sizeof(numLetters[i][0]));
		if (mat[i][0] != '?')
			numLetters[i][0][mat[i][0] - 'A']++;
	}
	for (int j = 1; j < m; j++) {
		memcpy(numLetters[0][j], numLetters[0][j - 1], sizeof(numLetters[0][j]));
		if (mat[0][j] != '?')
			numLetters[0][j][mat[0][j] - 'A']++;
	}
	for (int i = 1; i < n; i++) {
		for (int j = 1; j < m; j++) {
			for (int k = 0; k < 26; k++) {
				numLetters[i][j][k] = numLetters[i - 1][j][k] + numLetters[i][j - 1][k] - numLetters[i - 1][j - 1][k];
			}
			if (mat[i][j] != '?')
				numLetters[i][j][mat[i][j] - 'A']++;
		}
	}
}

int numLetters2[SIZE][SIZE][SIZE][SIZE];
int getNumLetters(int x1, int y1, int x2, int y2) {
	if (numLetters2[x1][y1][x2][y2] != -1)
		 return numLetters2[x1][y1][x2][y2];
	int res[26];
	memcpy(res, numLetters[x2][y2], sizeof(res)); 
	for (int k = 0; k < 26; k++)
	{
		if (x1 > 0) {
			res[k] -= numLetters[x1 - 1][y2][k];
		}
		if (y1 > 0) {
			res[k] -= numLetters[x2][y1 - 1][k];
		}
		if (x1 > 0 && y1 > 0) {
			res[k] += numLetters[x1 - 1][y1 - 1][k];
		}
	}
	int cnt = 0;
	for (int k = 0; k < 26; k++)
	{
		if (res[k] != 0)
			cnt++;
	}
	numLetters2[x1][y1][x2][y2] =cnt;
	return cnt;
}

char getLetter(int x1, int y1, int i, int j) {
	char letter = '0';
	for (int k = x1; k<= i; k++) {
		for (int l = y1; letter == '0' && l<= j; l++) {
			if (mat[k][l] != '?') {
				letter = mat[k][l];
				break;
			}
		}
	}
	return letter;
}

bool hasSolution(int x1, int y1, int x2, int y2) {
	if (solved[x1][y1][x2][y2] != -1) {
		return solved[x1][y1][x2][y2];
	}

	bool hasLetter[26];
	memset(hasLetter, false, sizeof(hasLetter));
	for (int i = x1; i <= x2; i++) {
		for (int j = y1; j <= y2; j++) {
			if (mat[i][j] != '?') {
				hasLetter[mat[i][j] - 'A'] = true;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (mat[i][j] != '?' && !(i >= x1 && i <= x2 && j >= y1 && j <= y2)) {
				if (hasLetter[mat[i][j] - 'A']) {
					solved[x1][y1][x2][y2] = 0;
					return 0;
				}
			}
		}
	}

	for (int i = x1; i <= x2; i++) {
		for (int j = y1; j <= y2; j++) {
			if (getNumLetters(x1, y1, i, j) != 1)
				continue;
			if ((i == x2 || hasSolution(i + 1, y1, x2, y2)) && (j == y2 || hasSolution(x1, j + 1, i, y2))) {
				solved[x1][y1][x2][y2] = 1;
				char letter = getLetter(x1, y1, i, j);
				for (int k = x1; k<= x2; k++) {
					for (int l = y1; l<= y2; l++) {
						if (k <= i && l <= j) {
							solution[x1][y1][x2][y2][k][l] = letter;
						} else if (k <= i) {
							solution[x1][y1][x2][y2][k][l] = solution[x1][j + 1][i][y2][k][l];
						} else {
							solution[x1][y1][x2][y2][k][l] = solution[i + 1][y1][x2][y2][k][l];
						}
					}
				}
				return true;
			}
			if ((j == y2 || hasSolution(x1, j + 1, x2, y2)) && (i == x2 || hasSolution(i + 1, y1, x2, j))) {
				solved[x1][y1][x2][y2] = 1;
				char letter = getLetter(x1, y1, i, j);
				for (int k = x1; k<= x2; k++) {
					for (int l = y1; l<= y2; l++) {
						if (k <= i && l <= j) {
							solution[x1][y1][x2][y2][k][l] = letter;
						} else if (l <= j) {
							solution[x1][y1][x2][y2][k][l] = solution[i + 1][y1][x2][j][k][l];
						} else {
							solution[x1][y1][x2][y2][k][l] = solution[x1][j + 1][x2][y2][k][l];
						}
					}
				}
				return true;
			}
		}
	}
	solved[x1][y1][x2][y2] = 0;
	return false;
}

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d:\n", testCounter + 1);
		memset(solved, -1, sizeof(solved));

		cin >> n >>m;
		mat.resize(n);
		for (int i = 0; i < n; i++)
			cin >> mat[i];

		memset(numLetters2, -1, sizeof(numLetters2));
		calcNumLetters();
		hasSolution(0, 0, n - 1, m - 1);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << solution[0][0][n -1][m -1][i][j];
			}
			cout << endl;
		}
	}
	return 0;
}


