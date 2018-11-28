#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

using namespace std;

int ok[200] = {};

int main() {
	// your code goes here
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);

	for (int i = 1; i<=t; i++)
	{
		long long int n;
		scanf("%lld", &n);
		
		int index = 0;

		for (long long int j = n; j >= 1; j--)
		{
			index = 0;
			long long int mok = j;
			int rem = mok % 10;
			int flag = 0;

			while (mok != 0)
			{
				ok[index++] = rem;
				mok /= 10;
				rem = mok % 10;
			}
			for (int k = 0; k<index - 1; k++)
			{
				
				if (ok[k] < ok[k + 1])
				{
					flag = 1;
					break;
				}
			}

			if (flag == 0)
			{
				printf("Case #%d: %lld\n", i, j);
				break;
			}
			
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}