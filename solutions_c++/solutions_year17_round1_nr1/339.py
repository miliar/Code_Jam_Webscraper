#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int N = 30;
char grid[N][N];
char first[N];
int r, c;

void go () {

	for (int j = 0; j < c; j++) {
		char at = '?';
		first[j] = '?';
		for (int i = 0; i < r; i++) {
			if (grid[i][j] != '?') 
				at = grid[i][j]; 

			grid[i][j] = at;

			if (first[j] == '?')
				first[j] = at;
		}
	}


	for (int j = 0; j < c; j++) 
		for (int i = 0; i < r; i++) 
			if (grid[i][j] == '?')
				grid[i][j] = first[j];

	bool f = 1;
	while (f) {
		f = 0;
		for (int j = 0; j < c - 1; j++) 
			for (int i = 0; i < r; i++) 
				if (grid[i][j] == '?' and grid[i][j + 1] != '?') {
					f = 1;
					grid[i][j] = grid[i][j+1];
				}
	}

	f = 1;
	while (f) {
		f = 0;
		for (int j = 1; j < c; j++) 
			for (int i = 0; i < r; i++) 
				if (grid[i][j] == '?' and grid[i][j - 1] != '?') {
					f = 1;
					grid[i][j] = grid[i][j-1];
				}
	}
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int T;	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> r >> c;
		for (int i = 0; i < r; i++)
			cin >> grid[i];
		go ();
		cout << "Case #" << t << ":\n";
		for (int i = 0; i < r; i++)
			cout << grid[i] << endl;
	}

	return 0;
}
