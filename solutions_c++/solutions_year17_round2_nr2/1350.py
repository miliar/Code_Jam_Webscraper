#include <cstdio>

using namespace std;


void proc(int caseno) {
	int N, R, O, Y, G, B, V;
	scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

	if ((O > 0 && !(B >= O + 1 || (B == O && B + O == N)))
		|| (G > 0 && !(R >= G + 1 || (R == G && R + G ==N)))
		|| (V > 0 && !(Y >= V + 1 || (Y == V && Y + V == N)))) {
		printf("Case #%d: IMPOSSIBLE\n", caseno);
		return;
	}

	int beff = B - O;
	int reff = R - G;
	int yeff = Y - V;
//	printf("eff B R Y %d %d %d\n", beff, reff, yeff);

	if (beff < 0 || reff < 0 || yeff < 0 || beff > reff + yeff || reff > beff + yeff || yeff > reff + beff) {
		printf("Case #%d: IMPOSSIBLE\n", caseno);
		return;
	}


	printf("Case #%d: ", caseno);

	char last = 'Y';
	for (int i = 0; i < N;) {
		if (B > 0 && ((last == 'Y' && B >= R) || (last == 'R' && B >= Y))) {
			last = 'B';
			printf("B");
			B--; i++;

			while(O > 0) {
				printf("O");
				O--; i++;
				if (B > 0) { 
					printf("B");
					B--; i++;
				}
			}
		} else if (R > 0 && ((last == 'B' && R >= Y) || (last == 'Y'))) {
			last = 'R';
			printf("R");
			R--; i++;

			while(G > 0) {
				printf("G");
				G--; i++;
				if (R > 0) {
					printf("R");
					R--; i++;
				}
			}
		} else if (Y > 0) {
			last = 'Y';
			printf("Y");
			Y--; i++;
			while(V > 0) {
				printf("V");
				V--; i++;
				if (Y > 0) {
					printf("Y");
					Y--; i++;
				}
			}
		}
	}

	printf("\n");
}

int main() {
	int c;
	scanf("%d", &c);
	for (int i = 0; i < c; i++)
		proc(i + 1);
}


