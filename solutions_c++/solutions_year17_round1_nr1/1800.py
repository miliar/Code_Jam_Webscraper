#include <iostream>

using namespace std;

int main() {

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
			int R, C;
			cin >> R >> C;
			getchar();
			char array[25][25] = {{0}};

			for(int i = 0; i < R; i++) {
				for(int j = 0; j < C; j++) {
					array[i][j] = getchar();
				}
				getchar();
			}

			// for(int i = 0; i < R; i++) {
			// 	for(int j = 0; j < C; j++) {
			// 		cout << array[i][j];
			// 	}
			// 	cout << endl;
			// }

			for(int i = 0; i < R; i++) {
				char fir_char = '?';
				for(int j = 0; j < C; j++) {
					if(array[i][j] != '?') {
						fir_char = array[i][j];
						break;
					}
				}
				for(int j = 0; j < C; j++) {
					if(array[i][j] == '?') {
						array[i][j] = fir_char;
					}
					else {
						fir_char = array[i][j];
					}
				}
			}

			int fir_line = 0;
			for(int i = 0; i < R; i++) {
				if(array[i][0] != '?') {
					fir_line = i;
					break;
				}
			}
			for(int i = 0; i < R; i++) {
				if(array[i][0] == '?') {
					for(int j = 0; j < C; j++) {
						array[i][j] = array[fir_line][j];
					}
				}
				else {
					fir_line = i;
				}
			}

			cout << "Case #" << t + 1 << ": " << endl;
			for(int i = 0; i < R; i++) {
				for(int j = 0; j < C; j++) {
					cout << array[i][j];
				}
				cout << endl;
			}

	}
	return 0;
}
