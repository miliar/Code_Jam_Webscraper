#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

int tn;
int N, R, O, Y, G, B, V;
char a[1200];

bool arrange() {

	if (O <= B) {
		B -= O;
	}
	else return false;

	if (G <= R) {
		R -= G;
	}
	else return false;

	if (V <= Y) {
		Y -= V;
	}
	else return false;

	if (B == 0 && O > 0) {
		if (R == 0 && G == 0 && V == 0 && Y == 0) {
			for(int i = 0; i < N; i++)
				a[i] = (i % 2)? 'B' : 'O';
			return true;
		}
		return false;
	}

	if (R == 0 && G > 0) {
		if (B == 0 && O == 0 && V == 0  && Y == 0) {
			for(int i = 0; i < N; i++)
				a[i] = (i % 2)? 'R' : 'G';
			return true;
		}
		return false;
	}

	if (Y == 0 && V > 0) {
		if (B == 0 && O == 0 && R == 0 && G == 0) {
			for(int i = 0; i < N; i++)
				a[i] = (i % 2)? 'Y' : 'V';
			return true;
		}
		return false;
	}

	int i = 0;
	while (i < N) {
		char ch = '#';

		if (i == 0) {
			if (B >= Y && B >= R) ch = 'B';
			else if (Y >= R && Y >= B) ch = 'Y';
			else ch = 'R';
		}
		else {
			switch (a[i-1]) {
				case 'B': ch = (R > Y || R == Y && a[0] == 'R')? 'R' : 'Y'; break;
				case 'R': ch = (B > Y || B == Y && a[0] == 'B')? 'B' : 'Y'; break;
				case 'Y': ch = (R > B || R == B && a[0] == 'R')? 'R' : 'B'; break;
			}
		}

		//printf("i = %d, ch = %c\n", i, ch);

		switch (ch) {
			case 'R':
				//printf("R = %d\n", R);
				if (R == 0) return false;
				a[i++] = 'R';
				//printf("R = %d\n", R);
				if (R == 1) {
				//	printf("Here!\n");
					for(int j = 0; j < 2*G; j++)
						a[i++] = (j % 2 == 0)? 'G' : 'R';
				}
				R --; break;
			case 'B':
				if (B == 0) return false;
				a[i++] = 'B';
				if (B == 1) {
					for(int j = 0; j < 2*O; j++)
						a[i++] = (j % 2 == 0)? 'O' : 'B';
				}
				B --; break;
			case 'Y':
				if (Y == 0) return false;
				a[i++] = 'Y';
				if (Y == 1) {
					for(int j = 0; j < 2*V; j++)
						a[i++] = (j % 2 == 0)? 'V' : 'Y';
				}
				Y --; break;
		}
	}

	if (a[N-1] == a[0]) return false;

	return true;

}

int main() {

	scanf("%d", &tn);
	for(int ctn = 0; ctn < tn; ctn ++) {

		scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		memset(a, 0, sizeof(a));

		bool flag = arrange();
		printf("Case #%d: ", ctn+1);
		if (flag) {
			printf("%s\n", a);
		}
		else {
			printf("IMPOSSIBLE\n");
		}

	}

	return 0;

}