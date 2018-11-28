#include <bits/stdc++.h>
using namespace std;

//Aidans Wonderful Shortcuts//
#define pb push_back
#define mp make_pair
#define fi first
#define se second
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

void solve(int N, int M, char* modelTypes, int* modelRow, int* modelCol);

int main(){

    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

	int T, N, M;
	cin >> T;

	for (int c = 1; c <= T; c++) {
		cin >> N >> M;

		char modelTypes [M+10];
		int R [M+10];
		int C [M+10];

		for(int j = 0; j < M; j++){
			cin >> modelTypes[j] >> R[j] >> C[j];
		}
		cout << "Case #" << c << ": ";
		solve(N, M, modelTypes, R, C);
	}
	return 0;
}

void solve(int N, int M, char* modelTypes, int* R, int* C){
	vi xRows;
	vi xCols;
	vi tSub;
	vi tAdd;
	int score = 0;
	for(int i = 0; i < M; i++){
		if(modelTypes[i]=='o'){
			xRows.pb(R[i]);
			xCols.pb(C[i]);
			tSub.pb(R[i]-C[i]);
			tAdd.pb(R[i]+C[i]-N-1);
			score += 2;
		}else if(modelTypes[i]=='x'){
			xRows.pb(R[i]);
			xCols.pb(C[i]);
			score++;
		}else if(modelTypes[i]=='+'){
			tSub.pb(R[i]-C[i]);
			tAdd.pb(R[i]+C[i]-N-1);
			score++;
		}
	}
	vi newRowx;
	vi newColx;
	for(int i = 1; i <= N; i++){
		bool contains = false;
		for(int j : xRows){
			if(j == i){
				contains = true;
				break;
			}
		}
		if(!contains){
				newRowx.pb(i);
		}
	}
	for(int i = 1; i <= N; i++){
		bool contains = false;
		for(int j : xCols){
			if(j == i){
				contains = true;
				break;
			}
		}
		if(!contains){
			newColx.pb(i);
		}
	}


	vi searchPattern;
	for(int i = N-1; i >= 0; i--){
		searchPattern.pb(i);
		searchPattern.pb(-i);
	}

	vi newRowt;
	vi newColt;
	for(int subDiag : searchPattern){
		for(int posDiag : searchPattern){
			if((subDiag+posDiag+N+1)%2!=0){
				continue;
			}
			int testRow = (subDiag+posDiag+N+1)/2;
			if(testRow < 1 || testRow>N){
				continue;
			}
			int testCol = (posDiag-subDiag+N+1)/2;
			if(testCol < 1 || testCol > N){
				continue;
			}
			bool openSquare = true;
			for(int diag : tSub){
				if(diag == subDiag){
					openSquare = false;
					break;
				}
			}
			for(int diag : tAdd){
				if(diag == posDiag){
					openSquare = false;
					break;
				}
			}
			if(openSquare){
				newRowt.pb(testRow);
				newColt.pb(testCol);
				tSub.pb(testRow-testCol);
				tAdd.pb(testRow+testCol-N-1);
			}
		}
	}


	vector<char> newModelType;
	vi newModelRow;
	vi newModelCol;
	int changes = 0;
	for(int i = 0; i < newRowx.size(); i++){
		int row = newRowx[i];
		int col = newColx[i];
		char type = 'x';
		for(int j = 0; j < M; j++){
			if(R[j]==row && C[j]==col){
				type = 'o';
			}
		}
		for(int k = 0; k < newRowt.size(); k++){
			if(newRowt[k]==row && newColt[k]==col){
				type = 'o';
				score++;
				newRowt[k] = -1;
				newColt[k] = -1;
			}
		}
		newModelType.pb(type);
		newModelRow.pb(row);
		newModelCol.pb(col);
		changes++;
		score++;
	}

	for(int i = 0; i < newRowt.size(); i++){
		int row = newRowt[i];
		int col = newColt[i];
		if(row<0 || col<0){
			continue;
		}
		char type = '+';
		for(int j = 0; j < M; j++){
			if(R[j]==row && C[j]==col){
				type = 'o';
			}
		}
		newModelType.pb(type);
		newModelRow.pb(row);
		newModelCol.pb(col);
		changes++;
		score++;
	}

	cout << score << " " << changes << endl;
	for(int i = 0; i < changes; i++){
		cout << newModelType[i] << " " << newModelRow[i] << " " << newModelCol[i] << endl;
	}

}
