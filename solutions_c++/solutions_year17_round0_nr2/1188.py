#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int LMAX = 30;

char N[LMAX];

int main()
{
	/*freopen("qr17bL.in", "r", stdin);
	freopen("qr17bL.out", "w", stdout);*/
	int T, i, len;
	cin >> T;
	for (int cs = 1; cs <= T; cs++)
	{
		scanf("%s", N + 1);
		N[0] = '0';
		len = strlen(N);
		
		for (i = 1; i < len; i++)
			if (N[i - 1] > N[i])
				break;
		
		if (i < len)
		{
			int j = i - 1;
			while (N[j - 1] == N[j])
				j--;
			N[j]--;
			while (++j < len)
				N[j] = '9';
		}
		
		i = 0;
		while (N[i] == '0')
			i++;
		printf("Case #%d: ", cs);
		for (; i < len; i++)
			printf("%c", N[i]);
		printf("\n");
	}
	return 0;
}


