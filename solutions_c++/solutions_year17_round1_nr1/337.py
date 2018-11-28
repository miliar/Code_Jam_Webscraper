#include<bits/stdc++.h>
using namespace std;
char ch[100][100];
int n, m;
void dfs(int l, int r){
	//cout<<l<<"  --  "<<r<<endl;
	int lastx = -1;
	for(int i = l; i <= r; i++)
		for(int j = 0; j < m; j++)
			if(ch[i][j] != '?'){
				if(lastx != -1 && i != lastx){
					dfs(l, lastx);
					dfs(lastx + 1, r);
					return;
				}
				lastx = i;
			}
	int lasty = 0;
	char lastchar;
	for(int t = 0; t < m; t++)
		if(ch[lastx][t] != '?'){
			for(int i = l; i <= r; i++)
				for(int j = lasty; j <=  t; j++)
					ch[i][j] = ch[lastx][t];
			lasty = t + 1;
			lastchar = ch[lastx][t];
		}
	for(int i = l; i <= r; i++)
		for(int j = lasty; j < m; j++)
			ch[i][j] = lastchar;
}
int main(){
	freopen("A_large.in", "r", stdin);
	freopen("A_large.out", "w", stdout);
	int TT;
	cin >> TT;
	for(int ii = 1; ii <= TT; ii++){
		cin>>n>>m;
		for(int i = 0; i < n; i++){
			scanf("%s", ch[i]);
			//printf("%s\n", ch[i]);
		}
			
		dfs(0, n - 1);
		printf("Case #%d:\n", ii);
		for(int i = 0; i < n; i++)
			printf("%s\n", ch[i]);
	}
}
