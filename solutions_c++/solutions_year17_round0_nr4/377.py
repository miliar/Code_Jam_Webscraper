#include <stdio.h>
#include <string.h>

#define SWAP(X, Y) (X)^=(Y)^=(X)^=(Y)

int T;
int n, m;
char map[100][100];
char res[100][100];
int v[4][300];
int p;

int val(char ch) {
	switch(ch) {
	case 'o': return 3;
	case '+': return 1;
	case 'x': return 2;
	}
	return 0;
}

int vv(int c) {
	return (c==3)?2:(c==0)?0:1;
}

void setCh(int x, int y, char ch, int init = 0) {
	int ov = res[x][y] | map[x][y];
	int nv = val(ch);
	if((ov|nv) == ov) return;
	
	if(init) map[x][y] |= nv;
	else res[x][y] |= nv;
	
	p += vv(ov|nv) - vv(ov);
	if((ov|nv) & 1) {
		v[2][y-x+n-1] = y+x;
		v[3][y+x] = y-x+n-1;
	}
	if((ov|nv) & 2) {
		v[0][x] = y;
		v[1][y] = x;
	}
}

char toCh(int x, int y) {
	int v = map[x][y] | res[x][y];
	return " +xo"[v];
}

/* DFS for bishop */
int da[300], db[300];
int vs[300];
int nn;
int dfs(int s) {
	if(vs[s]) return 0;
	vs[s] = 1;
	int I = (s<n)?s:n * 2 - s - 2;
	int i;
	
	for(i=-I+n-1;i<=I+n-1;i+=2) {
		if(v[3][i] < 0) {
			if(db[i] < 0 || (!vs[db[i]] && dfs(db[i]))) {
				da[s] = i, db[i] = s;
				return 1;
			}
		}
	}
	return 0;
}

void diag() {
	int i, j;
	for(i=0;i<nn;i++) {
		da[i] = db[i] = -1;
	}
	for(i=0;i<nn;i++) {
		if(v[2][i] < 0 && da[i] < 0) {
			memset(vs, 0x00, sizeof(int) * nn);
			dfs(i);
		}
	}

	for(i=0;i<nn;i++) {
		j = da[i];
		if(j>=0 && db[j] == i) {
			int x = (j-i+n-1)/2, y = (i+j-n+1)/2;
			setCh(x, y, '+');
		}
	}
}

void foo(int C) {
	p = 0;
	int x, y;
	char ch;
	int i, j, k, l;

	scanf("%d %d", &n, &m);

	nn = 2 * n - 1;

	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			map[i][j]=res[i][j] = 0;
	for(i=0;i<2*n+1;i++)
		v[0][i]=v[1][i]=v[2][i]=v[3][i]=-1;
	
	for(i=0;i<m;i++) {
		char c;
		scanf(" %c %d %d", &c, &x, &y);
		x--, y--;
		setCh(x, y, c, 1);
	}

	/* Place + */

	diag();

	/* Place x */
	for(i=0;i<n;i++) {
		if(v[0][i] >= 0) continue;
		for(j=0;j<n;j++) {
			if(v[1][j] < 0) {
				setCh(i, j, 'x');
				break;
			}
		}
	}

	printf("Case #%d: ", C);
	{
		int c = 0;
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) {
				if(res[i][j]) c++;
			}
		}
		printf("%d %d\n", p, c);
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) {
				if(res[i][j]) {
					printf("%c %d %d\n", toCh(i, j), i + 1, j + 1);
				}
			}
		}
	}
	
}

int main() {
	scanf("%d", &T);
	for(int i=0;i<T;i++) {
		foo(i+1);
	}
	return 0;
}

