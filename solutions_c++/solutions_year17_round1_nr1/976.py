#include <cstdio>
#include <vector>
#include <set>

using namespace std;

char board[30][30];
int r,c;

bool trysolve(int n){
	int orig_r=-1, orig_c=-1;
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if(board[i][j]==n){
				orig_r=i;
				orig_c=j;
			}
		}
	}
	if(orig_r==-1){
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				if(board[i][j]=='?'){ return false; }
			}
		}
		return true;
	}
	for(int lor=0; lor<=orig_r; lor++){
		for(int hir=orig_r; hir<r; hir++){
			for(int loc=0; loc<=orig_c; loc++){
				for(int hic=orig_c; hic<c; hic++){
					bool ok=true;
					for(int i=lor; i<=hir; i++){
						for(int j=loc; j<=hic; j++){
							if(board[i][j]!='?' && board[i][j]!=n){ ok=false; }
						}
					}
					if(!ok){ continue; }
					for(int i=lor; i<=hir; i++){
						for(int j=loc; j<=hic; j++){
							board[i][j]=n;
						}
					}
					if(trysolve(n+1)){
						return true;
					}
					for(int i=lor; i<=hir; i++){
						for(int j=loc; j<=hic; j++){
							board[i][j]='?';
						}
					}
					board[orig_r][orig_c]=n;
				}
			}
		}
	}
	return false;
}

void solve(){
	scanf("%d %d", &r, &c);
	vector<char> letters;
	for(int i=0; i<r; i++){
		scanf("%s", board[i]);
		for(int j=0; j<c; j++){
			if(board[i][j]!='?'){
				letters.push_back(board[i][j]);
				board[i][j]=letters.size()-1;
			}
		}
	}
	trysolve(0);
	printf("\n");
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if(board[i][j]=='?'){
				printf("?");
			}
			else{
				printf("%c", letters[board[i][j]]);
			}
		}
		printf("\n");
	}
}

int main(){
	int t;
	scanf("%d", &t);
	for(int tc=0; tc<t; tc++){
		printf("Case #%d: ", tc+1);
		solve();
	}
}
