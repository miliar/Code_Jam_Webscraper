#include <iostream>
#include <string>
#include <vector>
#include <queue>
/*

Cake

*/

using namespace std;

char findNext(vector<vector<char>> &grid, int i, int j, int C){
	char res = '#';
	for (int k = j; k<C ; ++k){
		if (grid[i][k] != '?'){
			res = grid[i][k];
			break;
		}	
	}
//	cout << "Next char is "<<res <<endl;
	return res;
}


int closestRowNonEmpty(vector<vector<char>> &grid, int i, int R, int C){
	for (int p = i+1; p<R; ++p){
		if (grid[p][0] != '?'){
			return p;
		}
	}
	for (int p = i-1; p>=0; p--){
		if (grid[p][0] != '?'){
			return p;
		}
	}

}


void output(vector<vector<char>> &grid, int R, int C){
	for (int i = 0; i<R ; ++i){
		for (int j = 0; j<C ; ++j){
		cout << grid[i][j];
		}
		cout << endl;
	}
}
void resolve(vector<vector<char>> &grid, int k, int R, int C){
	//cout << "R = "<< R << endl;
	//cout << "C = "<< C << endl;
	//cout << grid.size() << " "<<grid[0].size() << endl;
	queue <int> toCopy;
	
//	char current = ' '; 
	for (int i = 0; i<R ; ++i){
		char t = '#';
		for (int j = 0; j<C ; ++j){
			char current = grid[i][j];
			if (t == '#'){
				t = findNext(grid, i, j, C);
				if ( t == '#' ){
					//there is no char on this row, skip it and fill it later as a clone of next row
					toCopy.push(i);
					break;
				}else{
					grid[i][j] = t;
				}
			}else if (current == '?'){
				grid[i][j] = t;
			}else{
				t = current;
			}
//			output(grid, R, C);	
		}
	}
	
	//copy

	while(!toCopy.empty()){
		int i = toCopy.front(); toCopy.pop();
		int k = closestRowNonEmpty(grid, i, R, C);
		for(int j = 0; j<C;  ++j){
			grid[i][j] = grid[k][j];
		}
	}
	
	cout << "Case #" << k+1 <<":"<<endl;
	output(grid, R, C);	

}

int main(){
	int n, R, C; 
	cin >> n; cin.ignore();

	for (int k = 0; k<n; ++k){
		cin >> R; cin >> C ; cin.ignore();
		vector<vector<char>> grid =  vector<vector<char>>(R);
		for (int i = 0; i<R; ++i){
			grid[i]=vector<char>(C);
		}
		for (int i = 0; i<R ; ++i){
			for (int j = 0; j<C ; ++j){
				cin >> grid[i][j]; 
			}
			cin.ignore();
		}
//		output(grid, R, C);
//		cout << "---"<<endl;
		resolve(grid, k, R, C);
	}
}
