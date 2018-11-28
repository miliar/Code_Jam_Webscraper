#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
#define REP(i, a, b) for(int i = int(a); i <= int(b); i++)
#define LOOP(i, v) for(int i = 0; i < v.size(); i++)
#define EPS 1e-9
#define INF 1e12
#define debug(x) cerr << "DEBUG : " << (#x) << " => " << (x) << endl

int main()
{
	int T;
	int M, N;
	char c[30][30];
	int line[30];
	int col[30];
	
	scanf("%d\n", &T);

	REP(t, 1, T)
	{
		fprintf(stderr, "Cas %d\n", t);
		printf("Case #%d:\n", t);
		
		scanf("%d %d\n", &M, &N);
		
		REP(i, 0, M-1)
		{
			line[i] = -1;
			REP(j, 0, N-1)
			{
				scanf("%c", &c[i][j]);
				if(c[i][j] != '?') line[i] = i;
			}
			if(line[i] == -1 && i > 0) line[i] = line[i-1];
			scanf("\n");
		}
		
		for(int i = M-1; i >= 0; i--)
		{
			if(line[i] == -1) line[i] = line[i+1];
		}
		
		REP(i, 0, M-1)
		{
			//fprintf(stderr, "Line %d\n", i);
			REP(j, 0, N-1)
			{
				col[j] = -1;
				c[i][j] = c[line[i]][j];
				if(c[i][j] != '?') col[j] = j;
				if(col[j] == -1 && j > 0) col[j] = col[j-1];
			}
			for(int j = N-1; j >= 0; j--)
			{
				if(col[j] == -1) col[j] = col[j+1];
				c[i][j] = c[i][col[j]];
				//fprintf(stderr, "Col %d = %d\n", j, col[j]);
			}
		}
		
		REP(i, 0, M-1)
		{
			REP(j, 0, N-1)
			{
				printf("%c", c[i][j]);
			}
			printf("\n");
		}
	}
	
	return 0;
}
