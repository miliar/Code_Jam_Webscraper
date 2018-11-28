#include <iostream>
using namespace std;

void print_map(char** map, int r, int c) {
	for(int i = 1; i <= r; ++i) {
		for(int j = 1; j <= c; ++j) {
			cout << map[i][j];
		}
		cout << endl;
	}
}

int main() {
    int ncase = 0;
    cin >> ncase;
    for (int round = 1; round <= ncase; ++round) {
		int R,C;
		cin >> R >> C;
		char** map;
		map = (char**)malloc(sizeof(char*) * R);
		int min_pos_in_c[40] = {0};
		for(int i = 1; i <= R; ++i) {
			map[i] = (char*)malloc(sizeof(char) * C);
			for(int j = 1; j <= C; ++j) {
				cin >> map[i][j];
				if (min_pos_in_c[j] == 0 && map[i][j] != '?') {
					min_pos_in_c[j] = i;
				}
			}
		}
		for(int j = 1; j <= C; ++j) {
			char last = '?';
			for(int i = 1; i <= R; ++i) {
				if(i < min_pos_in_c[j])
					map[i][j] = map[min_pos_in_c[j]][j];
				else if (map[i][j] == '?') {
					map[i][j] = last;
				}
				last = map[i][j];
			}
		}
		int last_col = -1;
		for(int j = 1; j <= C; ++j) {
			if (map[1][j] != '?') {
				last_col = j;
				continue;
			} else {
				if (last_col > 0) {
				for(int i = 1; i <= R; ++i) {
					map[i][j] = map[i][last_col];
				}
				}
			}
		}
		for(int j = C; j >= 1; --j) {
			if (map[1][j] != '?') {
				last_col = j;
				continue;
			} else {
				if (last_col > 0) {
				for(int i = 1; i <= R; ++i) {
					map[i][j] = map[i][last_col];
				}
				}
			}
		}
        cout << "Case #" << round << ":" << endl;
		print_map((char**)map, R, C);
//        cout << endl;
    }
    return 0;
}
