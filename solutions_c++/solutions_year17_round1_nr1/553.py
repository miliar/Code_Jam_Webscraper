#include <bits/stdc++.h>
using namespace std;

int t;
int r, c;
char g[42][42];

int main()
{
	scanf("%d\n", &t);
for(int x=1; x<=t; x++) {
	scanf("%d %d\n", &r, &c);
	for(int i=0; i<r; i++) scanf("%s\n", g[i]);
	for(int i=0; i<r; i++) {
		for(int j=0; j<c; j++) {
			if(g[i][j]!='?') {
				for(int ii=0; ii<=i; ii++) {
					for(int jj=0; jj<=j; jj++) {
						if(g[ii][jj]=='?') g[ii][jj]=g[i][j];
					}
					for(int jj=j+1; jj<c; jj++) {
						if(g[i][jj]=='?' && g[ii][jj]=='?') g[ii][jj]=g[i][j];
						else break;
					}
				}
			}
		}
	}
	for(int i=r-1; i>=0; i--) {
		for(int j=0; j<c; j++) {
			if(g[i][j]=='?') {
				for(int ii=i-1; ii>=0; ii--) {
					if(g[ii][j]!='?') {
						g[i][j]=g[ii][j];
						break;
					}
				}
			}
		}
	}
	printf("Case #%d:\n", x);
	for(int i=0; i<r; i++) {
		printf("%s\n", g[i]);
	}
}

	return 0;
}
