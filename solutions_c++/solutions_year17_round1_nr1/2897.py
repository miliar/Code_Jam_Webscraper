#include<stdio.h>
#include<iostream>

using namespace std;
typedef struct blob_{
	int x1, y1, x2, y2;
	int cnt;
	char ch;
}blob;
int r, c, n = 0;
bool is_vailable(const int y, const int x){
	return y >= 0 && x >= 0 && y < r&&x < c;
}
int paramater[2][2] = { { 0, -1 }, { -1, 0 } };
int main(){

	int test;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	for (int tc = 1; tc <= test; ++tc){
		char  mat[25][25];
		//scanf("%d %d ", &r, &c);
		cin >> r >> c;
		for (int i = 0; i < r; ++i){
			for (int j = 0; j < c; ++j){
				cin >> mat[i][j];
				//scanf("%c", &mat[i][j]);
			}
		}
		for (int i = 0; i < r; ++i){
			for (int j = 0; j < c; ++j){
				if (mat[i][j] == '?'){
					//left
					if (is_vailable(i, j - 1) && mat[i][j - 1] != '?'){
						mat[i][j] = mat[i][j - 1];
						continue;
					}

				}
			}

		}
		for (int i = r - 1; i >= 0; --i){
			for (int j = c - 1; j >= 0; --j){
				if (mat[i][j] == '?'){

					//left
					if (is_vailable(i, j + 1) && mat[i][j + 1] != '?'){
						mat[i][j] = mat[i][j + 1];
						continue;
					}

				}
			}
		}
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (mat[i][j] == '?')
					//up
					if (is_vailable(i - 1, j) && mat[i - 1][j] != '?'){
						mat[i][j] = mat[i - 1][j];
						continue;
					}
		for (int i = r - 1; i >= 0; --i)
			for (int j = c - 1; j >= 0; --j)
				//up	
				if (mat[i][j] == '?')
					if (is_vailable(i + 1, j) && mat[i + 1][j] != '?'){
						mat[i][j] = mat[i + 1][j];
						continue;
					}
		/*for (int k = 0; k < n; k++){
			for (int i = b[k].y1; i <= b[k].y2; ++i){
			for (int j = b[k].x1; j <= b[k].x2; ++j){
			mat[i][j] = b[k].ch;
			}
			}
			}*/

		cout << "Case #" << tc << ":" << endl;
		for (int i = 0; i < r; ++i){
			for (int j = 0; j < c; ++j){
				printf("%c", mat[i][j]);
			}
			printf("\n");
		}
	}
}