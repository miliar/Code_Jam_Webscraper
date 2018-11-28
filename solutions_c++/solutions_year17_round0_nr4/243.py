#include <bits/stdc++.h>
using namespace std;
char grid[205][205];
bitset<205> pls[205], times[205];
bitset<205> ldi, rdi;
bitset<205> rows, cols;
bitset<205> done;
int match[205], mt[205];
int n,m;

bool Aug(int l) {
	if (done[l]) return false;
	done[l]=true;
	int lb,ub;
	if (l<n) lb=n-1-l, ub=n-1+l;
	else lb=l+1-n, ub=2*n-3-(l-n);
	for (int i=lb; i<=ub; i+=2) {
		if (!rdi[i]) {
			//printf("%d %d %d\n", l, i, match[i]);
			if (match[i]==-1) {
				match[i]=l;
				return true;
			}
			else if (Aug(match[i])) {
				match[i]=l;
				return true;}
		}
	}
	return false;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int p=1; p<=tc; p++) {
		memset(match,-1,sizeof(match));
		rows.reset();
		cols.reset();
		ldi.reset();
		rdi.reset();
		scanf("%d%d", &n, &m);
		for (int j=0; j<n; j++) {
			for (int k=0; k<n; k++) {
				grid[j][k]='.';
				times[j][k]=false;
				pls[j][k]=false;
			}
		}
		for (int j=0; j<m; j++) {
			char c;
			scanf("  %c", &c);
			int x,y;
			scanf("%d%d", &x, &y);
			x--, y--;
			grid[x][y]=c;
			if (c=='o'||c=='x') {
				times[x][y]=true;
				rows[x]=true;
				cols[y]=true;
			}
			if (c=='o'||c=='+') {
				pls[x][y]=true;
				ldi[x+y]=true;
				rdi[n-x-1+y]=true;
			}
		}
		
		int add=0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (!rows[i] && !cols[j]) {
					rows[i]=true;
					cols[j]=true;
					times[i][j]=true;
				}
			}
		}
		
		int ans=n;
		for (int i=0; i<2*n-1; i++) {
			if (!ldi[i]) {
				done.reset();
				int z=Aug(i);
				ans+=z;
			}
			else ans++;
			//printf("%d %d\n", i, ans);
			//for (int j=0; j<2*n-1; j++) printf("%d ", match[j]);
			//printf("\n");
		}
		memset(mt,-1,sizeof(mt));
		for (int i=0; i<2*n-1; i++) {
			if (match[i]!=-1) mt[match[i]]=i;
		}
		for (int i=0; i<2*n-1; i++) {
			if (!ldi[i] && mt[i]!=-1) {
				//printf("%d %d\n", i, mt[i]);
				int tgt=i+mt[i]-(n-1);
				tgt/=2;
				pls[i-tgt][tgt]=true;
			}
		}
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (pls[i][j] && times[i][j]) {
					if (grid[i][j]!='o') add++;
				}
				else if (pls[i][j] && grid[i][j]!='+') {
					add++;
				}
				else if (times[i][j] && grid[i][j]!='x') {
					add++;
				}
			}
		}
		
		printf("Case #%d: %d %d\n", p, ans, add); 
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (pls[i][j] && times[i][j]) {
					if (grid[i][j]!='o') printf("o %d %d\n", i+1, j+1);
				}
				else if (pls[i][j] && grid[i][j]!='+') {
					printf("+ %d %d\n", i+1, j+1);
				}
				else if (times[i][j] && grid[i][j]!='x') {
					printf("x %d %d\n", i+1, j+1);
				}
			}
		}
	}
}
