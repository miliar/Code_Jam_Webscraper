#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> ii;
int tcs, r, c, dx[4] = {-1, 0, 1, 0}, dy[4] = {0, -1, 0, 1};
char b[27][27];
bool v[27][27];
void fill(int cx, int cy, char cf, int d){
	if(cx < 0 || cx >= r || cy < 0 || cy >= c) return;
	v[cx][cy] = 1;
	if(b[cx][cy] != cf && b[cx][cy] != '?') return ;
	b[cx][cy] = cf;
	fill(cx+dx[d], cy+dy[d], cf, d);
}
//start from innermost
int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		memset(v, 0, sizeof v);
		scanf("%i%i", &r, &c);
		for(int i=0;i<r;i++){
			scanf("%s", b[i]);
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				fill(i, j, b[i][j], 0);
				fill(i, j, b[i][j], 2);
			}
		}
		memset(v, 0, sizeof v);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				fill(i, j, b[i][j], 1);
				fill(i, j, b[i][j], 3);
			}
		}
		printf("Case #%i:\n", tc);
		for(int i=0;i<r;i++){
			printf("%s\n", b[i]);
		}
	}
}