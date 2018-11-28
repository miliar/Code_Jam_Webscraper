#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin >> t;
	for( int m = 1; m <= t; m++){
		int r , c;
		cin >> r >> c;
		char ar[r][c];
		vector<char> store;
		for( int i = 0; i < r; i++ ){
			scanf("%s", ar[i] );
		}
		char stor;
		int j = 0 , l = store.size();
		for( int i = 0; i < c; i++ ){
			for( j = 0; j < r; j++ ){
				if( ar[j][i] != '?' ){
					stor = ar[j][i];
					for( int k = j - 1; k >= 0; k-- ){//up
						if( ar[k][i] == '?' ){
							ar[k][i] = stor;
						}
						else{
							break;
						}
					}
					for( int k = j + 1; k < r; k++ ){//down
						if( ar[k][i] == '?' ){
							ar[k][i] = stor;
						}
						else{
							break;
						}
					}
				}
			}
		}
		for( int i = 0; i < r;i++ ){
			for( int j = 0;j < c; j++ ){
				if( ar[i][j] == '?' ){
					int start = j;
					for( int k = j - 1; k >= 0; k-- ){
						if( ar[i][k] != '?' ){
							start = k;
							break;
						}
					}
					for( int k = start + 1; k <= j; k++ ){
						ar[i][k] = ar[i][start];
					}
					for( int k = j + 1; k < c; k++ ){
						if( ar[i][k] != '?' ){
							start = k;
							break;
						}
					}
					for( int k = start - 1; k >= j; k-- ){
						ar[i][k] = ar[i][start];
					}
				}
			}
		}
		printf("Case #%d:\n",m);
		for( int i = 0; i < r; i++ ){
			for( int j = 0; j < c; j++ ){
				 printf("%c", ar[i][j]);
			}
			cout << "\n";
		}
	}
}