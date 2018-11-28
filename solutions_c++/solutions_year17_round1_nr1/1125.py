#include <bits/stdc++.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair

int n,m;
char mat[30][30];

int main(){
	int t;
	scanf("%d",&t);
	for(int caso = 1; caso <= t; caso++){
		scanf("%d %d",&n,&m);
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++)
				scanf(" %c",&mat[i][j]);
		}
		for(int i = 0; i < n; i++){
			char a = '?';
			for(int j = 0; j < m; j++){
				//printf("%c - %c\n",a,mat[i][j] );
				if(mat[i][j] == '?')
					mat[i][j] = a;
				else a = mat[i][j];
			}
		}

		for(int i = 0; i < n; i++){
			char a = '?';
			for(int j = m-1; j >= 0; j--){
				if(mat[i][j] == '?')
					mat[i][j] = a;
				else a = mat[i][j];
			}
		}
		for(int j = 0; j < m; j++){
			char a = '?';
			for(int i = 0; i < n; i++){
				if(mat[i][j] == '?')
					mat[i][j] = a;
				else a = mat[i][j];
			}
		}

		for(int j = 0; j < m; j++){
			char a = '?';
			for(int i = n-1; i >= 0; i--){
				if(mat[i][j] == '?')
					mat[i][j] = a;
				else a = mat[i][j];
			}
		}
		printf("Case #%d:\n",caso );
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				printf("%c",mat[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}