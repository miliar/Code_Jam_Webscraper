#include <cstdio>
#include <iostream>
#include <cstring>
#define db(x) cout<<#x<<"="<<(x)<<" "
#define el cout<<endl
using namespace std;

const int MXN = 1010;

int cas, tcas;

char str[MXN];
int N;

int A[MXN];

void init()
{
	scanf("%s\n", str + 1); N = strlen(str + 1);
}

namespace solve
{	
	void solve()
	{
		if (N == 1)
		{
			printf("%s\n", str + 1);
			return;
		}
		for(int i = 2; i <= N; ++i)
				if (str[i] < str[i-1])
				{
					for(int j = 1 ; j <= i-1; ++j)
						if (str[j] == str[i-1])
						{
							-- str[j];
							for(int k = j + 1; k <= N; ++k) str[k] = '9';
							break;
						}
					break;
				}
		for(int j = 1; j <= N; ++j)
			if (str[j] != '0')
			{
				printf("%s\n", str + j);
				return;
			}
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &cas);
	for(tcas = 0; tcas < cas; ++tcas)
	{
		init();
		printf("Case #%d: ", tcas + 1);
		solve::solve();
	}
	return 0;
}
