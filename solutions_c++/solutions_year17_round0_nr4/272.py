//oh man what am i doing?
#include <stdio.h>
#include <string.h>

char sampah[3];
char stage0[110][110];
char stage1[110][110];
int N;

bool dUp[210], dDown[210];
bool col[110], row[110];

bool CanPutModel(int y, int x, int model){
	char checkAs = model;
	
	if(model == 'o'){
		if(stage1[y][x] == 'o') checkAs = '.';
		else if(stage1[y][x] == '+') checkAs = 'x';
		else if(stage1[y][x] == 'x') checkAs = '+';
	}
	else if(model == '+'){
		if(stage1[y][x] == '+') checkAs = '.';
	}
	else if(model == 'x'){
		if(stage1[y][x] == 'x') checkAs = '.';
	}
	
	if(checkAs == '.') return true;
	
	int idUp = x+y-1;
	int idDown = x-y+N;
	if(checkAs == '+'){
		if(dUp[idUp] || dDown[idDown]) return false;
		return true;
	}
	if(checkAs == 'x'){
		if(col[x] || row[y]) return false;
		return true;
	}
	if(checkAs == 'o'){
		if(dUp[idUp] || dDown[idDown] || col[x] || row[y]) return false;
		return true;
	}
	return true;
}

void PutModel(int y, int x, char model){
	char putAs = model;
	
	if(model == 'o'){
		if(stage1[y][x] == 'o') putAs = '.';
		else if(stage1[y][x] == '+') putAs = 'x';
		else if(stage1[y][x] == 'x') putAs = '+';
	}
	else if(model == '+'){
		if(stage1[y][x] == '+') putAs = '.';
	}
	else if(model == 'x'){
		if(stage1[y][x] == 'x') putAs = '.';
	}
	
	int idUp = x+y-1;
	int idDown = x-y+N;
	if(putAs == '.'){
		stage1[y][x] = model;
	}
	else if(putAs == '+'){
		dUp[idUp] = true;
		dDown[idDown] = true;
		stage1[y][x] = model;
	}
	else if(putAs == 'x'){
		col[x] = true;
		row[y] = true;
		stage1[y][x] = model;
	}
	else if(putAs == 'o'){
		dUp[idUp] = true;
		dDown[idDown] = true;
		col[x] = true;
		row[y] = true;
		stage1[y][x] = model;
	}
}

int main(){
	int jcase;
	char model;
	int y, x;
	int M;
	
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%d %d", &N, &M);
		
		for(int i=1; i<=N; i++){
			for(int j=1; j<=N; j++) stage0[i][j] = stage1[i][j] = '.';
		}
		memset(dUp, false, sizeof(dUp));
		memset(dDown, false, sizeof(dDown));
		memset(col, false, sizeof(row));
		memset(row, false, sizeof(col));
		
		for(int i=0; i<M; i++){
			gets(sampah);
			scanf("%c %d %d", &model, &y, &x);
			stage0[y][x] = model;
			PutModel(y, x, model);
		}
		
		int loop = (N+1)/2;
		for(int k=0; k<loop; k++){
			for(int i=1; i<=N; i++){
				if(stage1[k+1][i] != '.') continue;
				if(CanPutModel(k+1, i, '+')) PutModel(k+1, i, '+');
			}
			for(int i=1; i<=N; i++){
				if(stage1[i][N-k] != '.') continue;
				if(CanPutModel(i, N-k, '+')) PutModel(i, N-k, '+');
			}
			for(int i=N; i>=1; i--){
				if(stage1[N-k][i] != '.') continue;
				if(CanPutModel(N-k, i, '+')) PutModel(N-k, i, '+');
			}
			for(int i=N; i>=1; i--){
				if(stage1[i][k+1] != '.') continue;
				if(CanPutModel(i, k+1, '+')) PutModel(i, k+1, '+');
			}
		}
		for(int i=1; i<=N; i++){
			for(int j=1; j<=N; j++){
				if(stage1[i][j] != '.') continue;
				if(CanPutModel(i, j, '+')) PutModel(i, j, '+');
			}
		}
		for(int i=1; i<=N; i++){
			for(int j=1; j<=N; j++){
				if(stage1[i][j] != '.') continue;
				if(CanPutModel(i, j, 'x')) PutModel(i, j, 'x');
			}
		}
		
		for(int i=1; i<=N; i++){
			for(int j=1; j<=N; j++){
				if(CanPutModel(i, j, 'o')) PutModel(i, j, 'o');
			}
		}
		/*
		for(int i=1; i<=N; i++){
			for(int j=1; j<=N; j++){
				printf("%c", stage1[i][j]);
			}
			printf("\n");
		}
		printf("\n");
		*/
		
		int numDiff = 0;
		int val = 0;
		
		for(int i=1; i<=N; i++){
			for(int j=1; j<=N; j++){
				if(stage0[i][j] != stage1[i][j]) numDiff++;
				if(stage1[i][j] == '+') val++;
				else if(stage1[i][j] == 'x') val++;
				else if(stage1[i][j] == 'o') val+=2;
			}
		}
		
		printf("Case #%d: %d %d\n", icase+1, val, numDiff);
		for(int i=1; i<=N; i++){
			for(int j=1; j<=N; j++){
				if(stage0[i][j] != stage1[i][j]) printf("%c %d %d\n", stage1[i][j], i, j);
			}
		}
		
	}
	
	return 0;
}
