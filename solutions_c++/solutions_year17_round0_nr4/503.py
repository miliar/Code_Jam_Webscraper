#include "string" 
#include "iostream"
#include "sstream"
#include "vector"
#include "map"
#include "queue"
#include "algorithm"
#include "functional"
#include "set"
#include "tuple"
using namespace std;

#define LL long long
#define UL unsigned long long

#define VC vector<char>
#define VI vector<int>
#define VU vector<unsigned int>
#define VL vector<long long>
#define VUL vector<unsigned long long>
#define VS vector<string>
#define VD vector<double>
#define VB vector<bool>
#define VC_IT VC::iterator;
#define VI_IT VI::iterator
#define VU_IT VU::iterator
#define VL_IT VL::iterator
#define VUL_IT VUL::iterator
#define VS_IT VS::iterator
#define VD_IT VD::iterator
#define VB_IT VB::iterator;

int N;
int score;

void placeRook(int row, int col, VB& rows, VB& cols) {
	rows[row] = true;
	cols[col] = true;
	score++;
}

void safeSet(int i, VB& v) {
	if (i >= 0 && i < v.size())
		v[i] = true;
}

void placeBishop(int row, int col, VB& top, VB& bottom, VB& left, VB& right) {
	int N1 = N - 1;
	int s = row + col;
	int d = row - col;

	safeSet(-1 * d, top);
	safeSet(s, top);
	safeSet(N1 - d, bottom);
	safeSet(s - N1, bottom);
	safeSet(d, left);
	safeSet(s, left);
	safeSet(s - N1, right);
	safeSet(d + N1, right);
	score++;
}

void doCase(int iCase) {
	printf("Case #%d: ", iCase);

	int M;
	cin >> N >> M; cin.ignore(999, '\n');

	VB rookRows(N, false);
	VB rookCols(N, false);
	VB bishopTop(N, false);
	VB bishopRight(N, false);
	VB bishopLeft(N, false);
	VB bishopBottom(N, false);

	vector< VB > origPieces(N, VB(N, false));
	score = 0;

	for (int i = 0; i < M; i++) {
		char t;
		int row, col;
		cin >> t >> row >> col; cin.ignore(999, '\n');
		row = row - 1; col = col - 1;

		origPieces[row][col] = true;
		if (t == '+') {
			placeBishop(row, col, bishopTop, bishopBottom, bishopLeft, bishopRight);
		}
		else if (t == 'x') {
			placeRook(row, col, rookRows, rookCols);
		}
		else {
			placeBishop(row, col, bishopTop, bishopBottom, bishopLeft, bishopRight);
			placeRook(row, col, rookRows, rookCols);
		}
	}

	vector< VC > moves = vector< VC >(N, VC(N, ' '));
	int numMoves = 0;

	// place the rooks
	while (true) {
		int r = 0, c = 0;
		for (; r < N; r++) {
			if (!rookRows[r])
				break;
		}
		for (; c < N; c++) {
			if (!rookCols[c])
				break;
		}

		if (r < N && c < N) {
			placeRook(r, c, rookRows, rookCols);
			moves[r][c] = 'x';
			numMoves++;
		}
		else {
			break;
		}
	}

	// place the bishops
	for (int i = 0; i < N; i++) {
		if (!bishopTop[i]) {
			placeBishop(0, i, bishopTop, bishopBottom, bishopLeft, bishopRight);
			if (moves[0][i] == ' ')
				numMoves++, moves[0][i] = '+';
			else
				moves[0][i] = 'o';
		}
		if (!bishopRight[i]) {
			placeBishop(i, N - 1, bishopTop, bishopBottom, bishopLeft, bishopRight);
			if (moves[i][N - 1] == ' ')
				numMoves++, moves[i][N - 1] = '+';
			else
				moves[i][N - 1] = 'o';
		}
		if (!bishopLeft[i]) {
			placeBishop(i, 0, bishopTop, bishopBottom, bishopLeft, bishopRight);
			if (moves[i][0] == ' ')
				numMoves++, moves[i][0] = '+';
			else
				moves[i][0] = 'o';
		}
		if (!bishopBottom[i]) {
			placeBishop(N - 1, i, bishopTop, bishopBottom, bishopLeft, bishopRight);
			if (moves[N - 1][i] == ' ')
				numMoves++, moves[N - 1][i] = '+';
			else
				moves[N - 1][i] = 'o';
		}
	}

	printf("%d %d\n", score, numMoves);
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			if (moves[r][c] != ' ') {
				char ch;
				if (origPieces[r][c])
					ch = 'o';
				else
					ch = moves[r][c];

				printf("%c %d %d\n", ch, r + 1, c + 1);
			}
		}
	}
}

void main(void) {
	int nCases;
	cin >> nCases;
	cin.ignore(999, '\n');

	for (int iCase = 1; iCase <= nCases; iCase++) {
		doCase(iCase);
	}
}