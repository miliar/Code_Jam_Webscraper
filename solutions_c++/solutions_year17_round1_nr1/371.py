#include <bits/stdc++.h>
using namespace std;

int T;
int R, C;

int main(){
	cin >> T;
	for (int q = 1; q<=T; q++){
		cout << "Case #" << q << ": " << endl;


		cin >> R >> C;

		string a[100];

		for(int i = 0; i<R; i++){
			cin >> a[i];
		}

		// work row by row:

		for (int i = 0; i<R; i++){
			// find out whether row is empty:
			bool isEmpty = true;
			char color = '?';

			for (int j = 0; j<C; j++){

				if (a[i][j] == '?'){
					a[i][j] = color;
				}
				else{
					color = a[i][j];
					if (isEmpty){
						for (int jj = 0; jj < j; jj++){
							a[i][jj] = color;
						}
					}
					isEmpty = false;
				}
			}

		}

		for (int j = 0; j<C; j++){
			// find out whether col is empty:
			bool isEmpty = true;
			char color = '?';

			for (int i = 0; i<R; i++){

				if (a[i][j] == '?'){
					a[i][j] = color;
				}
				else{
					color = a[i][j];
					if (isEmpty){
						for (int ii = 0; ii < i; ii++){
							a[ii][j] = color;
						}
					}
					isEmpty = false;
				}
			}

		}

		for (int i = 0; i<R; i++){
			cout << a[i] << endl;
		}


		
	}
}