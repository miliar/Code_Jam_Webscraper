#include <iostream>
#include <cassert>

using namespace std;

#define forsn(i,s,n) for (int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)
#define dforsn(i,s,n) for (int i = (int)(n) - 1;i >= (s);i--)
#define dforn(i,n) dforsn(i,0,n)
#define all(v) (v).begin(), (v).end()

char original[32][32];
char board[32][32];
int R, C; 

bool can_advance(int m, int M, int c) {
	if (c == C || c < 0) return false;
	forsn(i, m, M) {
		if (board[i][c] != '?') return false;
	}
	return true;
}

void expand(int i, int j) {
	int m = i - 1;
	while (m >= 0 && board[m][j] == '?') {
		m--;
	}
	m++;
	
	int M = i + 1;
	while (M < R && board[M][j] == '?') {
		M++;
	}
	
	int cc = j;
	do {
		forsn(x, m, M) board[x][cc] = board[i][j];
		cc++;
	} while (can_advance(m, M, cc));
	
	cc = j;
	do {
		forsn(x, m, M) board[x][cc] = board[i][j];
		cc--;
	} while (can_advance(m, M, cc));
}

int main() {
	int T; cin >> T;
	forn(caso, T) {
		cin >> R >> C;
		forn(i,R) forn(j,C) cin >> original[i][j];
		forn(i,R) forn(j,C) board[i][j] = original[i][j];
		
		forn(i,C) forn(j,R) if (original[j][i] != '?') {
			expand(j, i);
		}
		
		cout << "Case #" << caso + 1 << ":\n";
		forn(i,R) {
			forn(j, C) {
				assert(board[i][j] != '?');
				cout << board[i][j];
			}
			cout << endl;
		}
	}
}
