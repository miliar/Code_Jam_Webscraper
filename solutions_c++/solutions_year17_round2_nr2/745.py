#include <cstdio>
#include <string>

using namespace std;

string ans;
bool ok;
int C[10];
int cases, N;

void pR() {
	ans += 'R';
	C[0]--;
}

void pB() {
	ans += 'B';
	C[4]--;
}

void pY() {
	ans += 'Y';
	C[2]--;
}

void pc(int col) {
	if(col == 0) {
		if(C[2] > 0) pY();
		else pB();
	}
	if(col == 2) {
		if(C[0] > 0) pR();
		else pB();
	}
	if(col == 4) {
		if(C[0] > 0) pR();
		else pY();
	}
}

void p2c(int col) {
	if(col == 0) {
		if(C[2] == 0 || C[4] == 0) {
			ok = false;
			return;
		}
		pY(); pB();
	}
	if(col == 2) {
		if(C[0] == 0 || C[4] == 0) {
			ok = false;
			return;
		}
		pR(); pB();
	}
	if(col == 4) {
		if(C[0] == 0 || C[2] == 0) {
			ok = false;
			return;
		}
		pR(); pY();
	}
}

void gao(char v, int x, int col) {
	int spaceLeft = N - x;
	if(spaceLeft < x) {
		puts("IMPOSSIBLE");
		return ;
	}
	int tooMany = spaceLeft - x;
	ok = true;
	ans = "";
	for(int i = 0; i < x; ++i) {
		ans += v;
		if(tooMany > 0) {
			p2c(col);
			--tooMany;
		} else {
			pc(col);
		}
	}
	if(!ok) {
		puts("IMPOSSIBLE");
		return ;
	}
	printf("%s\n", ans.c_str());
}

int main() {
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx) {
		scanf("%d", &N);
		for(int i = 0; i < 6; ++i)
			scanf("%d", &C[i]);
		printf("Case #%d: ", xx);
		if(C[0] >= C[2] && C[0] >= C[4]) {
			gao('R', C[0], 0);
		} else if(C[2] >= C[0] && C[2] >= C[4]) {
			gao('Y', C[2], 2);
		} else if(C[4] >= C[0] && C[4] >= C[2]) {
			gao('B', C[4], 4);
		}
	}
}
