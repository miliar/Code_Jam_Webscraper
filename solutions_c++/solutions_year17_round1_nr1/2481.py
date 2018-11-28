#include <stdio.h>
#include <algorithm>

using namespace std;

char a[30][30], b[30][30];
int use[30];

void Do(int r, int c, int x, int y) {


	int px = -1, py = -1;
	char ch = -1;
	for (int i = x; i <= r; i++) {
		for (int j = y; j <= c; j++) {
			char key = '?';
			bool ok = 1;
			for (int l = x; l <= i; l++) {
				for (int r = y; r <= j; r++) {
					if (a[l][r] != '?') {
						if (key == '?')
							key = a[l][r];
						else
							ok = 0;
					}
				}
			}
			if (key != '?') {
				for (int le = 1; le <= r; le++)
					for (int ri = 1; ri <= c; ri++)
						if (!(x <= le && le <= i && y <= ri && ri <= j) && a[le][ri] == key)
							ok = 0;
			}
					
			if (ok && key != '?') {
				px = i, py = j;
				ch = key;
			}
		}
	}
	
	if( ch != '?')
		for (int l = x; l <= px; l++) {
			for (int r = y; r <= py; r++) {
				a[l][r] = ch;
			}
		}
}

bool solve() {
	int r, c;
	scanf("%d %d", &r, &c);

	for (int i = 1; i <= r; i++)for (int j = 1; j <= c; j++) b[i][j] = a[i][j];

	for (int i = 0; i < 26; i++) use[i] = 0;

	for (int i = 1; i <= r; i++) {
		
		scanf("%s", &a[i][1]);
		for (int j = 1; j <= c; j++) {
			use[a[i][j] - 'A'] = 1;
			b[i][j] = a[i][j];
		}
	}

	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			Do(r, c, i, j);
		}
	}

	bool ok = 1;
	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			printf("%c", a[i][j]);
		}
		puts("");
	}

	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
			if (a[i][j] != b[i][j] && b[i][j] != '?')
				return 0;

	for (int i = 0; i < 26; i++) {
		int lx = 30, ly = 30, rx = -1, ry = -1;
		for (int j = 1; j <= r; j++) {
			for (int k = 1; k <= c; k++) {
				if (a[j][k] == i + 'A') {
					lx = min(lx, j);
					ly = min(ly, k);
					rx = max(rx, j);
					ry = max(ry, k);

				}
			}
		}
		if (lx != 30) {
			if (!use[i]) return 0;
			for (int x = lx; x <= rx; x++)
				for (int y = ly; y <= ry; y++)
					if ( a[x][y] != i + 'A')
						return 0;
		}
		else
			if (use[i]) return 0;
	}
	return ok;
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int R = 1; R <= T; R++) {
		printf("Case #%d:", R);
		puts("");
		if (!solve())
			printf("this %d\n", R);
		
	}

}