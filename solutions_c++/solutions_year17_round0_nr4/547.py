#include <bits/stdc++.h>
using namespace std;
#define MAXN 109

int N, M, ctimes, cplus;
char board[109][109];
bool plusboard[MAXN][MAXN], timesboard[MAXN][MAXN];
set<int> row, col, pdiag, sdiag;

void timessolve(){
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			if (!row.count(i) && !col.count(j)){
				row.insert(i);
				col.insert(j);
				timesboard[i][j] = true;
				ctimes++;
			}
		}
	}
}

void plussolve(){
	for(int j1=N-1, i1=0, i2 = N-1, j2; j1>=0; j1--){
		j2 = N-1-j1;
		if (!pdiag.count(i1+j1) && !sdiag.count(i1-j1)){
			pdiag.insert(i1+j1);
			sdiag.insert(i1-j1);
			plusboard[i1][j1] = true;
			cplus++;
		}
		if (!pdiag.count(i2+j2) && !sdiag.count(i2-j2)){
			pdiag.insert(i2+j2);
			sdiag.insert(i2-j2);
			plusboard[i2][j2] = true;
			cplus++;
		}
	}
}

struct change{
	char c; int i; int j;
	change(char _c, int _i, int _j) : c(_c), i(_i), j(_j) {}
};
vector<change> changes;

void makechanges()
{
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			if (timesboard[i][j] && plusboard[i][j]){
				if (board[i][j] != 'o') changes.push_back(change('o', i, j));
			}
			else if (timesboard[i][j]){
				if (board[i][j] != 'x') changes.push_back(change('x', i, j));
			}
			else if (plusboard[i][j]){
				if (board[i][j] != '+') changes.push_back(change('+', i, j));
			}
		}
	}
}

int main()
{
	int T, i, j;
	char c;
	scanf("%d", &T);
	for(int caseNo = 1; caseNo <= T; caseNo++){
		memset(&board, '.', sizeof board);
		memset(&timesboard, false, sizeof timesboard);
		memset(&plusboard, false, sizeof plusboard);
		scanf("%d %d", &N, &M);
		cplus = ctimes = 0;
		while (M--){
			scanf(" %c %d %d", &c, &i, &j);
			i--; j--;
			board[i][j] = c;
			if (c == 'o' || c == 'x'){
				timesboard[i][j] = true;
				row.insert(i);
				col.insert(j);
				ctimes++;
			}
			if (c == 'o' || c == '+'){
				plusboard[i][j] = true;
				pdiag.insert(i+j);
				sdiag.insert(i-j);
				cplus++;
			}
		}
		plussolve();
		timessolve();
		makechanges();
		printf("Case #%d: %d %d\n", caseNo, ctimes+cplus, changes.size());
		for(i=0; i<(int)changes.size(); i++){
			printf("%c %d %d\n", changes[i].c, changes[i].i+1, changes[i].j+1);
		}
		row.clear(); col.clear(); pdiag.clear(); sdiag.clear();
		changes.clear();
	}
	return 0;
}