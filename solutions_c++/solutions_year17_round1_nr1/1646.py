#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;

const int MAX_RC = 25;

void solve() {
	int r;
	int c;
	scanf("%d %d\n", &r, &c);

	char arr[MAX_RC][MAX_RC];
	for (int i=0; i<r; i++) {
		for (int j=0; j<c; j++) {
			arr[i][j] = getchar();
		}
		getchar();
	}

	for (int i=0; i<r; i++) {
		char prev = '?';
		for (int j=0; j<c; j++) {
			if (arr[i][j] == '?') {
				if (prev != '?') {
					arr[i][j] = prev;
				}
			} else {
				if (prev == '?') {
					for (int jj=0; jj<j; jj++) arr[i][jj] = arr[i][j];
				}
				prev = arr[i][j];
			}
		}
	}

	bool first = true;
	for (int i=0; i<r; i++) {
		if (arr[i][0] == '?') {
			if (!first) copy(arr[i-1], arr[i], arr[i]);
		} else {
			if (first) {
				for (int ii=0; ii<i; ii++) copy(arr[i], arr[i+1], arr[ii]);
			}
			first = false;
		}
	}

	for (int i=0; i<r; i++) {
		for (int j=0; j<c; j++) {
			putchar(arr[i][j]);
		}
		putchar('\n');
	}
}

int main() {
	int t;
	scanf("%d\n", &t);

	for (int i=1; i<=t; i++) {
		printf("Case #%d:\n", i);
		solve();
	}
}
