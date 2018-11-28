#include <iostream>

using namespace std;

string grid[30];
int visited[30][30];

int R;
int C;

void expand(int r, int c){
	int left = c;
	int right = c;
	
	while(true){
		if (left == 0) break;
		if (grid[r][left - 1] == '?'){
			grid[r][left - 1] = grid[r][c];
			visited[r][left-1] = 1;
		} else {
			break;
		}
		left--;
	}
	while(true){
		if (right == C - 1) break;
		if (grid[r][right + 1] == '?'){
			grid[r][right + 1] = grid[r][c];
			
			visited[r][right+1] = 1;
		} else {
			break;
		}
		right++;
	}
	
	int top = r;
	int bottom = r;
	
	while(true){
		bool good = true;
		if (top == 0) break;
		for(int i = left; i <= right; i++){
			if (grid[top - 1][i] != '?'){
				good = false;
				break;
			}
		}
		if (good){
			for(int i = left; i <= right; i++){
				grid[top - 1][i] = grid[r][c];
				visited[top-1][i] = 1;
			}
			top--;
		} else {
			break;
		}
	}
	
	while(true){
		bool good = true;
		if (bottom == R) break;
		for(int i = left; i <= right; i++){
			if (grid[bottom + 1][i] != '?'){
				good = false;
				break;
			}
		}
		if (good){
			for(int i = left; i <= right; i++){
				grid[bottom + 1][i] = grid[r][c];
				
				visited[bottom+1][i] = 1;
			}
			bottom++;
		} else {
			break;
		}
	}
	
}


int main(){
	int T;
	cin >> T;
	
	for(int t = 0; t < T; t++){
		cin >> R >> C;
		
		for(int i = 0; i < R; i++){
			cin >> grid[i];
		}
		for(int i = 0; i < 30; i++){
			for(int j = 0; j < 30; j++){
				visited[i][j] = 0;
			}
		}
		for(int i = 0; i < R; i++){
			for(int j = 0; j < C; j++){
				if (grid[i][j] != '?' && !visited[i][j]){
					expand(i,j);
								
				}
			}
		}
		cout << "Case #" << t+1 << ": " << endl;
		for(int i = 0; i < R; i++){
			cout << grid[i] << endl;
		}
	}
}