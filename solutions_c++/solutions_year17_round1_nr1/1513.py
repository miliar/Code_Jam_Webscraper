#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;
char S[30][30];
int vis[50];
int n,m,Case;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&Case);
	for (int CASE=1; CASE<=Case; CASE++){
		scanf("%d%d",&n,&m);
		for (int i=0; i<n; i++){
			scanf("%s", S[i]);
		//	for (int j=0; j<m; j++)
		//	if (S[i][j] != '?')
		//		exist[S[i][j]-'A'] = CASE;
		}
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
			if (S[i][j] != '?' && vis[S[i][j]-'A'] != CASE){
				vis[S[i][j]-'A'] = CASE;
				char c = S[i][j];
				int k1=j, k2=j;
				while (k1 >= 0 && (S[i][k1] == c || S[i][k1] == '?'))
					S[i][k1--] = c;
				while (k2 < m && (S[i][k2] == c || S[i][k2] == '?'))
					S[i][k2++] = c;
				k1++; k2--;
				for (int k=i-1; k>=0; k--){
					int flag = true;
					for (int l=k1; l<=k2; l++)
						if (S[k][l] != c && S[k][l] != '?')
							flag = false;
					if (!flag) break;
					for (int l=k1; l<=k2; l++)
						S[k][l] = c;
				}
				for (int k=i+1; k<n; k++){
					int flag = true;
					for (int l=k1; l<=k2; l++)
						if (S[k][l] != c && S[k][l] != '?')
							flag = false;
					if (!flag) break;
					for (int l=k1; l<=k2; l++)
						S[k][l] = c;
				}
			}
		printf("Case #%d:\n", CASE);
		for (int i=0; i<n; i++)
			printf("%s\n", S[i]);
	}
	return 0;
}

