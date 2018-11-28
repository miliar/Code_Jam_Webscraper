#include <cstdio>
#include <cstring>

using namespace std;

#define N (0)
#define R (1)
#define Y (2)
#define B (4)
#define O (R|Y)
#define G (Y|B)
#define V (R|B)
char colorToChar[] = {'.', 'R', 'Y', 'O', 'B', 'V', 'G'};

bool fill(int* stable, int* colors) {
	int i;
	int toFill, amount = 0;

	/*printf("%d %d %d %d %d %d : ", colors[R], colors[Y], colors[B], colors[O], colors[G], colors[V]);
	for(i = 0; i < colors[N]; i++) {
		putchar(colorToChar[stable[i]]);
	}
	putchar('\n');*/

	if(colors[R] > amount) {
		toFill = R;
		amount = colors[R];
	}
	if(colors[Y] > amount) {
		toFill = Y;
		amount = colors[Y];
	}
	if(colors[B] > amount) {
		toFill = B;
		amount = colors[B];
	}
	if(colors[O] > amount) {
		toFill = O;
		amount = colors[O];
	}
	if(colors[G] > amount) {
		toFill = G;
		amount = colors[G];
	}
	if(colors[V] > amount) {
		toFill = V;
		amount = colors[V];
	}
	if(amount == 0) {
		return true;
	}
	for(i = 0; i < colors[N]; i++) {
		if(stable[i] == 0) {
			if((stable[(i + colors[N] - 1) % colors[N]] & toFill) == 0
				&& (stable[(i + 1) % colors[N]] & toFill) == 0) {
				stable[i] = toFill;
				--colors[toFill];
				if(fill(stable, colors)) {
					return true;
				} else {
					stable[i] = 0;
					++colors[toFill];
				}
			}
		}
	}
	return false;
}
int main() {
	int t, cs;
	int colors[7];
	int base[3];
	int stable[1001];
	int i;

	scanf("%d", &t);
	for(cs = 1; cs <= t; cs++) {
		scanf("%d%d%d%d%d%d%d", &colors[N], &colors[R], &colors[O], &colors[Y], &colors[G], &colors[B], &colors[V]);
		base[0] = colors[R] + colors[O] + colors[V];
		base[1] = colors[Y] + colors[O] + colors[G];
		base[2] = colors[B] + colors[G] + colors[V];
		for(i = 0; i < 3; i++) {
			if(base[i] > colors[N] / 2) {
				printf("Case #%d: IMPOSSIBLE\n", cs);
				goto nextCase;
			}
		}
		memset(stable, 0, sizeof(int) * colors[N]);

		printf("Case #%d: ", cs);
		if(fill(stable, colors)) {
			for(i = 0; i < colors[N]; i++) {
				putchar(colorToChar[stable[i]]);
			}
			putchar('\n');
		} else {
			puts("IMPOSSIBLE");
		}
nextCase:
		;
	}
}