#include <cstdio>
#include <cstring>
#define CODE "B-large"
typedef long long lld;
const int MAXD = 55;
char buff[MAXD]{ };
int digit[MAXD]{ };
int H, L, P, S, T; // Head, Length, Pivot, Suffix

int main()
{
	freopen(CODE ".in", "r", stdin);
	freopen(CODE ".out", "w", stdout);
	scanf("%d", &T);
	for(int _ = 1; _ <= T; ++_)
	{
		scanf(" %s", buff);
		H =  0;
		P = -1;
		L = strlen(buff);
		S =  L;
		for(int i = 1; i < L; ++i)
			if(buff[i-1] > buff[i])
			{	// Inversion
				P = i-1;
				break;
			}
		if(P == -1)
		{	// Tidy Number
			printf("Case #%d: %s\n", _, buff);
			continue;
		}
		for(int i = P; i >= 0; --i)
		{
			--buff[i];
			if((i == 0) || (buff[i-1] <= buff[i]))
			{
				if(!i && (buff[i] == '0')) H = 1;
				S = i+1;
				break;
			}
		}
		for(int i = S; i < L; ++i)
			buff[i] = '9'; // Nine-Fill
		printf("Case #%d: %s\n", _, buff+H);
	}
	return 0;
}