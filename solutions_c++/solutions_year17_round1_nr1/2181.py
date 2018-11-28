#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>

typedef long long ll;

using namespace std;

char cake[25][25];
bool empty[25];
int c, r;

void solve() {
	memset(empty, 0, sizeof(empty));
	for (int i=0; i<r; ++i) {
		int pre=0;
		char ch = '\0';
		bool start = true;
		for (int j=0; j<c; ++j) {
			if (cake[i][j] != '?') {
				ch = cake[i][j];
				if (start) {
					for (int k=pre; k<j; ++k) cake[i][k] = ch;
					start=false;
				}
			} else {
				if (ch != '\0') {
					cake[i][j] = ch;
				}
			}
		}
		if (pre==0 && ch=='\0' && start) empty[i] = true;
	}

	for (int i=0; i<r; ++i) {
		if (empty[i]) {
			int j=0;
			for (j=i; j< r; ++j) {
				if (!empty[j]) break;
			}
			if (j == r) {
				for (j=i; j>0; --j)
					if (!empty[j]) break;
			}
			for (int k=0; k<c; ++k) {
				cake[i][k] = cake[j][k];
				empty[i] = false;
			}
		}
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("output", "w", stdout);

	int T;
	cin >> T;
	for (int case_n=0; case_n < T; ++case_n){
		cin >> r >> c;
		memset(cake, 0, sizeof(cake));
		for (int i=0; i < r; ++i){
			for (int j=0; j<c;++j){
				cin >> cake[i][j];
			}
		}
		solve();
		printf("Case #%d:\n", case_n+1);
		for (int i=0; i < r; ++i){
			for (int j=0; j<c;++j){
				cout << cake[i][j];
			}
			cout << endl;
		}

	}


	return 0;
}


