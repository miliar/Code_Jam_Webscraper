#include <bits/stdc++.h>

using namespace std;

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small.out", "w", stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("B-test.in", "r", stdin);
	//freopen("B-brute-optimized.out", "w", stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc = 1; tc <= t; tc++)
	{
		char str[20];
		scanf("%s",str); 
		//Numbers in non decreasing are good, 123, 111 are good
		//Find the last good number <= str1
		//3, 1, 2 ->
		int N = strlen(str);

		for(int i = N - 1; i > 0; i--)
		{
			int j ;
			for( j = i ; j > 0; j-- )
			{
				if(str[j - 1] <= str[j]) continue;
				else break;
			}

			if(j == 0) break;
			str[j - 1] = (str[j - 1] == '0') ? '9' : str[j - 1] - 1;

			for(int k = j ; k <= i ; k++)
				str[k] = '9';
			i = j;
		}

		printf("Case #%d: ",tc);
		int i = 0;
		for(; i < N; i++)
			if(str[i] != '0') break;
		for( ; i < N; i++)
			printf("%c",str[i]);

		printf("\n");

	}
	return 0;
}