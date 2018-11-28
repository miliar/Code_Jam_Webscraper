#include<bits/stdc++.h>
using namespace std;

void solve(int N, int M, char* modelTypes, int* modelRow, int* modelCol){
	vector<int> xRows;
	vector<int> xCols;
	vector<int> tSub;
	vector<int> tAdd;
	int score = 0;
	for(int i = 0; i < M; i++){
		if(modelTypes[i]=='o'){
			xRows.push_back(modelRow[i]);
			xCols.push_back(modelCol[i]);
			tSub.push_back(modelRow[i]-modelCol[i]);
			tAdd.push_back(modelRow[i]+modelCol[i]-N-1);
			score += 2;
		}else if(modelTypes[i]=='x'){
			xRows.push_back(modelRow[i]);
			xCols.push_back(modelCol[i]);
			score++;
		}else if(modelTypes[i]=='+'){
			tSub.push_back(modelRow[i]-modelCol[i]);
			tAdd.push_back(modelRow[i]+modelCol[i]-N-1);
			score++;
		}
	}
	vector<int> newRowx;
	vector<int> newColx;
	for(int i = 1; i <= N; i++){
		bool contains = false;
		for( int ii = 0 ; ii < xRows.size() ; ii++){
            int j = xRows[ii];
			if(j == i){
				contains = true;
				break;
			}
		}
		if(!contains){
				newRowx.push_back(i);
		}
	}
	for(int i = 1; i <= N; i++){
		bool contains = false;
		for(int ii = 0 ; ii < xCols.size() ; ii++){
            int j = xCols[ii];
			if(j == i){
				contains = true;
				break;
			}
		}
		if(!contains){
			newColx.push_back(i);
		}
	}


	vector<int> searchPattern;
	for(int i = N-1; i >= 0; i--){
		searchPattern.push_back(i);
		searchPattern.push_back(-i);
	}

	vector<int> newRowt;
	vector<int> newColt;
	for(int ii = 0 ; ii < searchPattern.size();ii++){
            int subDiag = searchPattern[ii];
		for(int jj = 0 ; jj < searchPattern.size();jj++){
		    int posDiag = searchPattern[jj];
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
			for(int kk = 0 ; kk < tSub.size() ; kk++){
			    int diag = tSub[kk];
				if(diag == subDiag){
					openSquare = false;
					break;
				}
			}
			for(int hh = 0 ; hh < tAdd.size() ; hh++){
			    int diag = tAdd[hh];
				if(diag == posDiag){
					openSquare = false;
					break;
				}
			}
			if(openSquare){
				newRowt.push_back(testRow);
				newColt.push_back(testCol);
				tSub.push_back(testRow-testCol);
				tAdd.push_back(testRow+testCol-N-1);
			}
		}
	}


	vector<char> newModelType;
	vector<int> newModelRow;
	vector<int> newModelCol;
	int changes = 0;
	for(int i = 0; i < newRowx.size(); i++){
		int row = newRowx[i];
		int col = newColx[i];
		char type = 'x';
		for(int j = 0; j < M; j++){
			if(modelRow[j]==row && modelCol[j]==col){
				type = 'o';
			}
		}
		//cout << "b";
		for(int k = 0; k < newRowt.size(); k++){
			if(newRowt[k]==row && newColt[k]==col){
				type = 'o';
				score++;
				newRowt[k] = -1;
				newColt[k] = -1;
			}
		}
		newModelType.push_back(type);
		newModelRow.push_back(row);
		newModelCol.push_back(col);
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
			if(modelRow[j]==row && modelCol[j]==col){
				type = 'o';
			}
		}
		newModelType.push_back(type);
		newModelRow.push_back(row);
		newModelCol.push_back(col);
		changes++;
		score++;
	}

	cout << score << " " << changes << endl;
	for(int i = 0; i < changes; i++){
		cout << newModelType[i] << " " << newModelRow[i] << " " << newModelCol[i] << endl;
	}

}

int main()
{
	using namespace std;
	int T, N, M;
	freopen("test.in","r",stdin);
	freopen("res.txt","w",stdout);
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> N >> M;
		char modelTypes [M];
		int modelRow [M];
		int modelCol [M];
		for(int j = 0; j < M; j++){
			cin >> modelTypes[j] >> modelRow[j] >> modelCol[j];
		}
		cout << "Case #" << i << ": ";
		solve(N, M, modelTypes, modelRow, modelCol);
	}
	return 0;
}
