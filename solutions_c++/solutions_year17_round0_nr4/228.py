#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
char cell[200][200];
bool flagx[200], flagy[200];
int a[200][200];
int vis[200];
int mat[200], add[200][200];
int tim, Case, n, m, ans;

bool dfs(int x, int N){
	if (vis[x] == tim) return false;
	vis[x] = tim;
	for (int i=0; i<N; i++){
		if (a[x][i] == 1 && ( mat[i]==-1 || dfs(mat[i], N) ) ){
			mat[i] = x;
			return true;
		}
	}
	return false;
}

int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&Case);
	for (int CASE=1; CASE<=Case; CASE++){
		scanf("%d%d",&n,&m);
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				cell[i][j] = ' ';
		ans = 0;
		for (int i=0; i<m; i++){
			char c = getchar();
			while (c!='o'&&c!='x'&&c!='+')
				c = getchar();
			int x, y;
			scanf("%d%d",&x,&y);
			cell[--x][--y] = c;
			ans++;
			if (c == 'o') ans++;
		}
		memset(add, 0, sizeof(add));
		
		memset(flagx,true,sizeof(flagx));
		memset(flagy,true,sizeof(flagy));
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
			if (cell[i][j] == 'o' || cell[i][j] == 'x')
				flagx[i] = flagy[j] = false;
		memset(a, 0, sizeof(a));
		for (int i=0; i<n; i++) if (flagx[i])
			for (int j=0; j<n; j++)	if (flagy[j])
			if (cell[i][j]!='o' && cell[i][j]!='x')
				a[i][j] = 1;
		for (int i=0; i<n; i++)
			mat[i] = -1;
		for (int i=0; i<n; i++){
			tim++;
			dfs(i, n);
		}
		for (int i=0; i<n; i++){
			if (mat[i]==-1) continue;
			add[mat[i]][i] ^= 1;
			ans++;
		}
		
		memset(flagx,true,sizeof(flagx));
		memset(flagy,true,sizeof(flagy));
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
			if (cell[i][j] == 'o' || cell[i][j] == '+')
				flagx[i+j] = flagy[i+n-j-1] = false;
		memset(a, 0, sizeof(a));
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
			if (flagx[i+j] && flagy[i+n-j-1] && cell[i][j]!='o' && cell[i][j]!='+')
				a[i+j][i+n-j-1] = 1;
		for (int i=0; i<n+n-1; i++)
			mat[i] = -1;
		for (int i=0; i<n+n-1; i++){
			tim++;
			dfs(i, n+n-1);
		}
		
		for (int i=0; i<n+n-1; i++){
			if (mat[i]==-1) continue;
			add[(i+mat[i]-n+1)/2][(mat[i]-i+n-1)/2] ^= 2;
			ans++;
		}
		
		int cnt = 0;
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				if (add[i][j] > 0)
					cnt++;
		printf("Case #%d: %d %d\n", CASE, ans, cnt);
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				if (add[i][j] > 0){
					if (add[i][j] == 3 || cell[i][j] != ' ')
						printf("o %d %d\n", i+1, j+1);
					else if (add[i][j] == 1){
						//if (cell[i][j] == 'x') printf("Error\n");
						printf("x %d %d\n", i+1, j+1);
					}
					else{
						//if (cell[i][j] == '+') printf("Error\n");
						printf("+ %d %d\n", i+1, j+1);
					}
				}
		
	}
	return 0;
}
