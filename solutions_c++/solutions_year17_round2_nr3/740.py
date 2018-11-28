#include <bits/stdc++.h>
#define ii pair<int, int>
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define vii vector< pair<int, int> >
typedef long long ll;
using namespace std;
double D[105][105];
double v[105];
double mx[105];
int main()
{
    int tt;
    scanf("%d", &tt);
    for(int qq = 1; qq<= tt; qq++)
    {
        double clock_start = clock();
		int n, q;
		scanf("%d %d", &n, &q);
		for(int i = 1; i<= n; i++) scanf("%lf %lf", mx+i, v+i);
		for(int i = 1; i<= n; i++) for(int j = 1; j<= n; j++) scanf("%lf", D[i]+j);
		for(int i = 1; i<= n; i++) for(int j = 1; j<= n; j++)
		{
			if(i == j) D[i][j] = 0;
			if(abs(D[i][j]+1) < 1e-6) D[i][j] = 1e18;
		}
		for(int k = 1; k<= n; k++) for(int i = 1; i<= n; i++) for(int j = 1; j<= n; j++)
			D[i][j] = min(D[i][k]+D[k][j], D[i][j]);
		for(int i = 1; i<= n; i++)
		{
			for(int j = 1; j<= n; j++)
			{
				if(D[i][j]> mx[i]) D[i][j] = 1e18;
				else D[i][j] /= v[i];
			}
		}
		for(int k = 1; k<= n; k++) for(int i = 1; i<= n; i++) for(int j = 1; j<= n; j++)
			D[i][j] = min(D[i][k]+D[k][j], D[i][j]);
	    printf("Case #%d: ", qq);
		while(q--)
		{
			int u, v; scanf("%d %d", &u, &v);
			printf("%lf ", D[u][v]);
		}
		printf("\n");
        fprintf(stderr, "Test %d solved in %.2lf s.\n", qq, (clock()-clock_start)/CLOCKS_PER_SEC);
    }
	return 0;
}
