#include <bits/stdc++.h>

using namespace std;

#define debug(x) cout << "-----" << x << "-----" << endl
#define debugS(S, x) cout << "-" << S << "-" << "-----" << x << "-----" << endl
#define print(x) cout << x << endl
#define NMAX 1222

typedef long long int lli;
typedef unsigned long long int llu;
typedef pair < lli, lli > par;
typedef vector < vector < par > > grafo;

char S[NMAX];

int main()
{
	int T, K;

	scanf("%d", &T);

	int con = 1;
	while(con <= T)
	{
		scanf("%s %d\n", S, &K);

		int res = 0;
		int tam = strlen(S);
		for(int i = 0; i <= tam - K; i++)
		{
			if(S[i] == '-')
			{
				res++;
				for(int j = i; j < i + K; j++)
				{
					if(S[j] == '-')
						S[j] = '+';
					else
						S[j] = '-';
				}
			}
		}

		for(int i = tam - K; i < tam; i++)
		{
			if(S[i] == '-')
			{
				res = -1;
				break;
			}
		}

		if(res >= 0)
			printf("Case #%d: %d\n", con, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", con);

		con++;
	}

	return 0;
}