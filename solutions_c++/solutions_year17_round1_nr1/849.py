//============================================================================
// Name        : Test2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int T, R, C;

char G[30][30];
bool V[30];

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d %d", &R, &C);

		int lastR = -1;
		for(int i = 0; i < R; i++){
			scanf("%s", G[i]);

			V[i] = false;

			int last = -1;
			for(int j = 0; j < C; j++)if(G[i][j] != '?'){
				V[i] = true;
				last = j;
				lastR = i;

				for(int k = j - 1; k >= 0; k--){
					if(G[i][k] != '?')break;
					G[i][k] = G[i][j];
				}
			}

			if(last != -1){
				for(int k = last + 1; k < C; k++)
					G[i][k] = G[i][last];
			}

			if(V[i]){
				for(int j = i - 1; j >= 0; j--){
					if(V[j])break;
					memcpy(G[j], G[i], sizeof G[i]);
				}
			}
		}

		for(int i = lastR + 1; i < R; i++)
			memcpy(G[i], G[lastR], sizeof G[lastR]);

		printf("Case #%d:\n", t);
		for(int i = 0; i < R; i++)
			printf("%s\n", G[i]);
	}
	return 0;
}
