#include <cstdio>
#include <iostream>
#include <cstring>
#define db(x) cout<<#x<<"="<<(x)<<" "
#define el cout<<endl
using namespace std;

const int MXN = 1010;

int cas, tcas;

char str[MXN];
int N, K;

int A[MXN];

void init()
{
	str[0] = '+';
	scanf("%s %d\n", str + 1, &K); N = strlen(str + 1);
	str[N + 1] = '+';
	for(int i = 0; i <= N; ++i) A[i+1] = str[i] != str[i+1];
}

namespace solve
{	
	void solve()
	{
		int cnt = 0;
		for(int i = 1; i <= N + 1; ++i)
			if (A[i])
			{
				//db(i),el;
				A[i] ^= 1;
				if (i + K > N + 1)
				{
					printf("IMPOSSIBLE\n");
					return;
				}
				A[i + K] ^= 1;
				++ cnt;
			}
		printf("%d\n", cnt);
	}
}

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	scanf("%d", &cas);
	for(tcas = 0; tcas < cas; ++tcas)
	{
		init();
		printf("Case #%d: ", tcas + 1);
		solve::solve();
	}
	return 0;
}
