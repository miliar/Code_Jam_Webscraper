#define _CRT_SECURE_NO_WARNINGS
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

#define MEMSET(x, WITH) memset(x, (WITH), sizeof(x))
#define FOR(i, E) for (int i=0; i<(E); i++)
typedef long long ll;
//const ll MOD = 1000000007;
//const double PI = atan(1) * 4;


#include <set>
int R, C;
char board[33][33];

bool inRange(int i, int j) {
	return 0<=i && i<R && 0<=j && j<C;
}

bool allQ(int R1, int C1, int R2, int C2) {
	if (!inRange(R1, C1) || !inRange(R2, C2)) return false;
	for (int i=R1; i<=R2; i++)
		for (int j=C1; j<=C2; j++)
			if (board[i][j] != '?') 
				return false;
	return true;
}

void fillchar(int R1, int C1, int R2, int C2, char c) {
	//printf("fill %d %d %d %d\n", R1, C1, R2, C2);
	for (int i=R1; i<=R2; i++)
		for (int j=C1; j<=C2; j++)
			board[i][j] = c;
}

bool qExist() {
	FOR(i, R) FOR(j, C) if (board[i][j] == '?') return true;
	return false;
}



int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		printf("Case #%d: ", tc);
		MEMSET(board, 0);

		scanf("%d%d", &R, &C);
		FOR(i, R) scanf("%s", board[i]);

		set<char> S;
		FOR(i, R) FOR(j, C) if (board[i][j] != '?') S.insert(board[i][j]);

		//for (char c : S) cout << c << endl;
		//puts("insert");

		for (char c : S) {
			int U = -1, D;
			FOR(i, R) FOR(j, C) if (board[i][j] == c) {
				if (U == -1) 
					U = i;
				D = i;
				//puts("fuck");
			}
			//puts("fuckfuck");

			int L = -1, RR;
			FOR(j, C) FOR(i, R) if (board[i][j] == c) {
				if (L == -1) 
					L = j;
				RR = j;
				//puts("break;");
			}

			assert(U != -1);
			assert(L != -1);

			for (int i=U; i<=D; i++)
				for (int j=L; j<=RR; j++) board[i][j] = c;
		}

		
		//puts("aaaaaa");
		//exit(0);


		int cnt = 0;
		while (qExist()) {


			for (char c : S) {
				int I, J;
				FOR(i, R) FOR(j, C) if (board[i][j] == c) {
					I = i;
					J = j;
					goto E1;
				}
				E1:

				int II = I;
				while (board[II+1][J] == c) II++;

				int JJ = J;
				while (board[I][JJ+1] == c) JJ++;
				//printf("square %d %d %d %d\n", I, J, II, JJ);


				if (allQ(I-1, J, I-1, JJ))
					fillchar(I-1, J, I-1, JJ, c);

				if (allQ(II+1, J, II+1, JJ))
					fillchar(II+1, J, II+1, JJ, c);


				//FOR(i, R) printf("debug %s\n", board[i]);
				//puts("qqq");
			}

			for (char c : S) {
				int I, J;
				FOR(i, R) FOR(j, C) if (board[i][j] == c) {
					I = i;
					J = j;
					goto E2;
				}
				E2:

				int II = I;
				while (board[II+1][J] == c) II++;

				int JJ = J;
				while (board[I][JJ+1] == c) JJ++;
				//printf("square %d %d %d %d\n", I, J, II, JJ);


				if (allQ(I, J-1, II, J-1)) {
					fillchar(I, J-1, II, J-1, c);
				}

				if (allQ(I, JJ+1, II, JJ+1))
					fillchar(I, JJ+1, II, JJ+1, c);

				//FOR(i, R) printf("debug %s\n", board[i]);
				//puts("qqq");
			}
		}

		

		puts("");
		FOR(i, R) puts(board[i]);






	}


	return 0;
}
