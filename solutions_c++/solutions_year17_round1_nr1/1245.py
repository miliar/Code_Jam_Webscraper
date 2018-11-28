#include <iostream>
using namespace std;

const int maxn = 25 + 2;
char map[maxn][maxn];

void solve() {
	int row, col;
	cin >> row >> col;
	for(int i = 0; i < row; i++) {
		for(int j = 0; j < col; j++) {
			cin >> map[i][j];
			if(map[i][j] == '?' && i > 0 && map[i-1][j] != '?')
				map[i][j] = map[i-1][j];
			if(map[i][j] != '?') {
				int cur = i;
				while(cur--) {
					if(map[cur][j] == '?')
						map[cur][j] = map[i][j];
					else break;
				}
			}
		}
	}
	int cur = 0;
	while(map[0][cur] == '?') cur++;
	for(int j = cur-1; j >= 0; j--)
		for(int i = 0; i < row; i++) map[i][j] = map[i][j+1];
	for(int j = 1; j < col; j++) if(map[0][j] == '?')
		for(int i = 0; i < row; i++) map[i][j] = map[i][j-1];
	for(int i = 0; i < row; i++) {
		for(int j = 0; j < col; j++) {
			cout << map[i][j];
		}
		cout << endl;
	}

}




int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ":" << endl;
		solve();
	}
	return 0;
}
