#include <bits/stdc++.h>
using namespace std;

char mapa[30][30];
char copyM[30][30];

int main (){

	freopen("A-large.in", "r", stdin);
	freopen("solLarge.out", "w", stdout);
	int t;
	scanf ("%d", &t);
	for (int caso = 1; caso <= t; caso++){
		int n, m;
		scanf ("%d %d", &n, &m);
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= m; j++){
				scanf (" %c", &mapa[i][j]);
				copyM[i][j] = mapa[i][j];
			}
		}
		int ff = n;
		int fact = n;
		while (fact >= 1){
			int cont = 0;
			while (fact >= 1 && cont == 0){
				for (int j = 1; j <= m; j++)
					if (mapa[fact][j] != '?')
						cont++;
				if (cont == 0)
					fact--;
			}
			if (fact >= 1){
				int cact = m;
				int cf = m;
				while (cact >= 1){
					while (cact >= 1 && mapa[fact][cact] == '?')
						cact--;
					if (cact >= 1){
						for (int i = fact; i <= ff; i++)
							for (int j = cact; j <= cf; j++)
								copyM[i][j] = mapa[fact][cact];
						cact--;
						cf = cact;
					}else{
						for (int i = fact; i <= ff; i++)
							for (int j = 1; j <= cf; j++)
								copyM[i][j] = copyM[fact][cf + 1];
					}
				}
				fact--;
				ff = fact;
			}else{
				for (int j = 1; j <= m; j++)
					for (int i = 1; i <= ff; i++)
						copyM[i][j] = copyM[ff + 1][j];
			}
		}
		printf ("Case #%d:\n", caso);
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= m; j++)
				printf ("%c", copyM[i][j]);
			printf ("\n");
		}
	}
	return 0;
}