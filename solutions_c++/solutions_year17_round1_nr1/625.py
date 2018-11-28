
#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

typedef long long i64;
typedef unsigned long long ui64;

int main(){
	int T;
	cin >> T;
	for (int t=1;t<=T;t++){
		int R, C;
		cin >> R >> C;
		vector< vector<char> > grid(R, vector<char>(C,'?'));
		for (int r=0;r<R;r++){
			for (int c=0;c<C;c++){
				char s;
				cin >> s;
				grid[r][c] = s;
			}
		}
		for (int c=0;c<C;c++){
			for (int r=0;r<R-1;r++){
				if (grid[r+1][c] == '?' && grid[r][c] != '?'){
					grid[r+1][c] = grid[r][c];
				}
			}
		}

		for (int c=0;c<C;c++){
			for (int r=R-1;r>=1;r--){
				if (grid[r-1][c] == '?' && grid[r][c] != '?'){
					grid[r-1][c] = grid[r][c];
				}
			}
		}
		for (int c=0;c<C-1;c++){
			if (grid[0][c+1]=='?' && grid[0][c]!='?'){
				for (int r=0;r<R;r++){
					grid[r][c+1] = grid[r][c];
				}
			}
		}

		for (int c=C-1;c>=1;c--){
			if (grid[0][c-1]=='?' && grid[0][c]!='?'){
				for (int r=0;r<R;r++){
					grid[r][c-1] = grid[r][c];
				}
			}
		}
		cout << "Case #"<<t<<":\n";
		for (int r=0;r<R;r++){
			for (int c=0;c<C;c++){
				cout << grid[r][c];
			}
			cout << endl;
		}
	}

}