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

int div1(int x, int V)
{
	int K;
	double k = (double)x/(1.1*(double)V);
	K = (int)floor(k);
	while(true)
	{
		if((long long int)11*K*V >= (long long int)10*x) return K;
		K++;
	}
}

int main()
{
	int T;
	int N, P;
	int v[51];
	vi ing[51], x;
	int pos[51];
	
	scanf("%d\n", &T);

	REP(t, 1, T)
	{
		fprintf(stderr, "Cas %d\n", t);
		printf("Case #%d: ", t);
		
		scanf("%d %d", &N, &P);
		
		REP(i, 0, N-1)
		{
			scanf("%d", &v[i]);
		}
		
		REP(i, 0, N-1)
		{
			ing[i].resize(P);
			REP(j, 0, P-1)
			{
				scanf("%d", &ing[i][j]);
			}
			sort(ing[i].begin(), ing[i].end());
			pos[i] = 0;
		}
		int tot = 0;
		bool stop = false;
		while(!stop)
		{
			int possibleN = 0;
			REP(i, 0, N-1)
			{
				int poss = div1(ing[i][pos[i]], v[i]);
				possibleN = max(poss, possibleN);
			}
			bool ok = true;
			REP(i, 0, N-1)
			{
				if((long long int)10*ing[i][pos[i]] < (long long int)9*possibleN*v[i])
				{
					ok = false;
					pos[i]++;
				}
			}
			if(ok)
			{
				tot++;
				REP(i, 0, N-1) pos[i]++;
				cerr << possibleN << endl;
			}
			REP(i, 0, N-1)
			{
				if(pos[i] >= P) stop = true;
			}
		}
		printf("%d\n", tot);
	}
	
	return 0;
}
