#include <bits/stdc++.h>
#define LL long long
#define INF 0x3f3f3f3f
#define VI vector<int>
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
using namespace std;
char A[110][110], B[110][110];
int n, m, t;
char buf[3];
bool v[110];
bool can(int x, int y){
	if(B[x][y] != '.') return false;
	int P = 0, X = 0, O = 0;
	for(int i = 0; i < n; i++){
		if(B[x][i] == '+') P++;
		else if(B[x][i] == 'o') O++;
		else if(B[x][i] == 'x') X++;
	}
	if(X || O) return false;
	P = 0; O = 0; X = 0;
	for(int i = 0; i < n; i++){
		if(B[i][y] == '+') P++;
		else if(B[i][y] == 'o') O++;
		else if(B[i][y] == 'x') X++;
	}
	if(X || O) return false;
	P = 0; O = 0; X = 0;
	int nx = x - 1, ny = y - 1;
	while(nx >= 0 && nx < n && ny >= 0 && ny < n){
		if(B[nx][ny] == '+') P++;
		else if(B[nx][ny] == 'o') O++;
		else if(B[nx][ny] == 'x') X++;
		nx--; ny--;
	}
	nx = x + 1; ny = y + 1;
	while(nx >= 0 && nx < n && ny >= 0 && ny < n){
		if(B[nx][ny] == '+') P++;
		else if(B[nx][ny] == 'o') O++;
		else if(B[nx][ny] == 'x') X++;
		nx++; ny++;
	}
	if(P > 1) return false;
	nx = x + 1; ny = y - 1;
	P = 0; O = 0; X = 0;
	while(nx >= 0 && nx < n && ny >= 0 && ny < n){
		if(B[nx][ny] == '+') P++;
		else if(B[nx][ny] == 'o') O++;
		else if(B[nx][ny] == 'x') X++;
		nx++; ny--;
	}
	nx = x - 1; ny = y + 1;
	P = 0; O = 0; X = 0;
	while(nx >= 0 && nx < n && ny >= 0 && ny < n){
		if(B[nx][ny] == '+') P++;
		else if(B[nx][ny] == 'o') O++;
		else if(B[nx][ny] == 'x') X++;
		nx--; ny++;
	}
	if(P > 1) return false;
	return true;
}
int main(){
	scanf("%d", &t);
	for(int c = 1; c <= t; c++){
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) A[i][j] = B[i][j] = '.';
		for(int i = 0; i < m; i++){
			int x, y;
			scanf("%s %d %d", buf, &x, &y);
			A[x-1][y-1] = buf[0];
		}
		memset(v, false, sizeof(v));
		int p = 0, o = 0;
		for(int i = 0; i < n; i++){
			if(A[0][i] == 'x'){
				B[0][i] = 'o';
				o = 1;
			}else if(A[0][i] == '+') p++;
			else if(A[0][i] == 'o'){
				B[0][i] = 'o';
				o = 1;
			}
		}
		if(!o) B[0][0] = 'o';
		for(int i = 0; i < n; i++){
			if(B[0][i] != 'o') B[0][i] = '+';
		}
		for(int i = 1; i < n - 1 && (n != 1); i++) B[n-1][i] = '+';
		for(int i = n - 1; i >= 0; i--){
			for(int j = n - 1; j >= 0; j--){
				if(can(j, i)) B[j][i] = 'x';
			}
		}
		int total = 0, ch = 0;

		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(B[i][j] == 'x' || B[i][j] == '+') total++;
				else if(B[i][j] == 'o') total+=2;
				if(A[i][j] != B[i][j]) ch++;
			}
		}
		printf("Case #%d: %d %d\n", c, total, ch);
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(A[i][j] != B[i][j]) printf("%c %d %d\n", B[i][j], i + 1, j + 1);
				//printf("%c", B[i][j]);
			}
			//printf("\n");
		}
	}
	return 0;
}