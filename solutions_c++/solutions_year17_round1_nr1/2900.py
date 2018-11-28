#include <iostream>

using namespace std;

char board[100][100];
bool liter[300];
int l[300];
int r[300];
int g[300];
int d[300];

int main() {
	int z;
	cin >> z;
	
	for(int zz = 1; zz <= z; zz++) {
		int R, C;
		cin >> R >> C;
		
		for(int i = 'A'; i <= 'Z'; i++) {
			liter[i] = 0;
			l[i] = 200;
			r[i] = -1;
			g[i] = 200;
			d[i] = -1;
		}
		
		for(int i = 1; i <= R; i++) {
				for(int j = 1; j <= C; j++) {
					cin >> board[i][j];
					
				}
		}
		
		
		cout << "Case #" << zz << ":" << endl;
		
	for(int pp=1;pp<=10;pp++){
		for(int i = 1; i <= R; i++) {
				for(int j = 1; j <= C; j++) {
					l[board[i][j]] = min(l[board[i][j]], j);
					r[board[i][j]] = max(r[board[i][j]], j);
					g[board[i][j]] = min(g[board[i][j]], i);
					d[board[i][j]] = max(d[board[i][j]], i);
				}
			}
		
		for(int i = 'A'; i <= 'Z'; i++) {
			for(int p = g[i]; p <= d[i]; p++) {
				for(int q = l[i]; q <= r[i]; q++) {
					board[p][q] = i;
				}
			}
		}
	for(int i = 1; i < R; i++) {
			int wsp = 0;
			for(int j = 1; j <= C; j++) {
				if(board[i][j] == board[i+1][j] || board[i][j] == '?' || board[i+1][j] == '?') {
					wsp++;
				}
			}
			
			if(wsp == C) {
				for(int j = 1; j <= C; j++) {
					if(board[i][j] == '?') {
						board[i][j] = board[i+1][j];
					}
					if(board[i+1][j] == '?') {
						board[i+1][j] = board[i][j];
					}
				}
			}
		}
		
		for(int i = 1; i < C; i++) {
			int wsp = 0;
			for(int j = 1; j <= R; j++) {
				if(board[j][i] == board[j][i+1]  ||board[j][i] == '?' || board[j][i+1] == '?') {
					wsp++;
				}
			}
			
			if(wsp == R) {
				for(int j = 1; j <= R; j++) {
					if(board[j][i] == '?') {
						board[j][i] = board[j][i+1];
					}
					if(board[j][i+1] == '?') {
						board[j][i+1] = board[j][i];
					}
				}
			}
		}
		
		
		for(int i = 2; i <= R; i++) {
			int wsp = 0;
			for(int j = 1; j <= C; j++) {
				if(board[i][j] == board[i-1][j] || board[i][j] == '?' || board[i-1][j] == '?') {
					wsp++;
				}
			}
			
			if(wsp == C) {
				for(int j = 1; j <= C; j++) {
					if(board[i][j] == '?') {
						board[i][j] = board[i-1][j];
					}
					if(board[i-1][j] == '?') {
						board[i-1][j] = board[i][j];
					}
				}
			}
		}
		
		for(int i = 2; i <= C; i++) {
			int wsp = 0;
			for(int j = 1; j <= R; j++) {
				if(board[j][i] == board[j][i-1]  ||board[j][i] == '?' || board[j][i-1] == '?') {
					wsp++;
				}
			}
			
			if(wsp == R) {
				for(int j = 1; j <= R; j++) {
					if(board[j][i] == '?') {
						board[j][i] = board[j][i-1];
					}
					if(board[j][i-1] == '?') {
						board[j][i-1] = board[j][i];
					}
				}
			}
		}
		
		for(int i = 2; i < R; i++) {
			for(int j = 1; j <= C; j++) {
				if(board[i][j] != '?' && board[i-1][j] != board[i][j] && board[i+1][j] != board[i][j]) {
					int p = j -1;
					while(p>=1 && board[i][p]=='?') {
						board[i][p] = board[i][j];
						p--;
					}
					p = j+1;
					while(p<=C&& board[i][p]=='?') {
						board[i][p] = board[i][j];
						p++;
					}
				}
			}
		}
		
		for(int j = 1; j <= C; j++) {
			int i = 1;
				if(board[i][j] != '?' && board[i+1][j] != board[i][j]) {
					int p = j -1;
					while(p>=1 && board[i][p]=='?') {
						board[i][p] = board[i][j];
						p--;
					}
					p = j+1;
					while(p<=C&& board[i][p]=='?') {
						board[i][p] = board[i][j];
						p++;
					}
				}
			}
			
			for(int j = 1; j <= C; j++) {
			int i = R;
				if(board[i][j] != '?' && board[R-1][j] != board[i][j]) {
					int p = j -1;
					while(p>=1 && board[i][p]=='?') {
						board[i][p] = board[i][j];
						p--;
					}
					p = j+1;
					while(p<=C&& board[i][p]=='?') {
						board[i][p] = board[i][j];
						p++;
					}
				}
			}
			
			
			for(int j = 1; j <= C; j++) {
			int i = 1;
				if(board[i][j] != '?' && board[i+1][j] != board[i][j]) {
					int p = j -1;
					while(p>=1 && board[i][p]=='?') {
						board[i][p] = board[i][j];
						p--;
					}
					p = j+1;
					while(p<=C&& board[i][p]=='?') {
						board[i][p] = board[i][j];
						p++;
					}
				}
			}
			
			for(int j = 1; j <= C; j++) {
			int i = R;
				if(board[i][j] != '?' && board[R-1][j] != board[i][j]) {
					int p = j -1;
					while(p>=1 && board[i][p]=='?') {
						board[i][p] = board[i][j];
						p--;
					}
					p = j+1;
					while(p<=C&& board[i][p]=='?') {
						board[i][p] = board[i][j];
						p++;
					}
				}
				}
				
				
				
		for(int i = 2; i < C; i++) {
			for(int j = 1; j <= R; j++) {
				if(board[j][i] != '?' && board[j][i-1] != board[j][i-1] && board[j][i+1] != board[j][i]) {
					int p = i -1;
					while(p>=1 && board[j][p]=='?') {
						board[j][p] = board[j][i];
						p--;
					}
					p = i+1;
					while(p<=C&& board[i][p]=='?') {
						board[j][p] = board[j][i];
						p++;
					}
				}
			}
			
		}
		
		for(int j = 1; j <= R; j++) {
			int i = 1;
				if(board[j][i] != '?' && board[j][i+1] != board[j][i]) {
					int p = i -1;
					while(p>=1 && board[j][p]=='?') {
						board[j][p] = board[j][i];
						p--;
					}
					p = i+1;
					while(p<=C&& board[i][p]=='?') {
						board[j][p] = board[j][i];
						p++;
					}
				}
			}
			
			for(int j = 1; j <= R; j++) {
				int i = C;
				if(board[j][i] != '?' && board[j][i-1] != board[j][i-1]) {
					int p = i -1;
					while(p>=1 && board[j][p]=='?') {
						board[j][p] = board[j][i];
						p--;
					}
					p = i+1;
					while(p<=C&& board[i][p]=='?') {
						board[j][p] = board[j][i];
						p++;
					}
				}
			}
	}
		
		for(int pp=1;pp<=30;pp++){
		for(int i = 1; i <= R; i++) {
			for(int j = 2; j <= C; j++) {
				if(board[i][j] =='?') {
					board[i][j] = board[i][j-1];
				}
			}
		}
		for(int i = 1; i <= R; i++) {
			for(int j = 1; j < C; j++) {
				if(board[i][j] =='?') {
					board[i][j] = board[i][j+1];
				}
			}
		}
	}

			
		
		for(int i = 1; i <= R; i++) {
				for(int j = 1; j <= C; j++) {
					cout <<  board[i][j];
				}
				cout << endl;
		}
	}
	
	return 0;
}
