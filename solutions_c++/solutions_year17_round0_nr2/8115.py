#include <bits/stdc++.h>

using namespace std;

#define debug(x) cout << "-----" << x << "-----" << endl
#define debugS(S, x) cout << "-" << S << "-" << "-----" << x << "-----" << endl
#define print(x) cout << x << endl
#define NMAX 111

typedef long long int lli;
typedef unsigned long long int llu;
typedef pair < lli, lli > par;
typedef vector < vector < par > > grafo;

char S[NMAX];

int main()
{

	int T;
	scanf("%d", &T);

	int con = 1;
	while(con <= T)
	{
		scanf("%s", S);
		int tam = strlen(S);
		for(int i = tam - 1; i > 0; i--)
		{
			if(S[i] < S[i - 1])
			{
				for(int j = i; j < tam; j++)
					S[j] = '9';
				S[i - 1]--;
			}
		}



		printf("Case #%d: ", con);
		for(int i = 0; i < tam; i++)
		{
			if(i == 0 && S[i] == '0')
				continue;
			else if(S[0] == '0')
				printf("9");
			else
				printf("%c", S[i]);
		}
		printf("\n");

		con++;
	}

	return 0;
}