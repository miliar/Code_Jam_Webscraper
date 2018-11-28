#include <iostream>
#include <string>

int main()
{
	int T;
	scanf("%d", &T);

	for (int Case = 0; Case < T; Case++)
	{
		char S[1001];
		int K;

		scanf("%s", S);
		scanf("%d", &K);

		int cnt = 0;
		for (int i = 0; i <= strlen(S) - K; i++)
		{
			if (S[i] == '-')
			{
				cnt++;
				for (int j = 0; j < K; j++)
				{
					if (S[i + j] == '-')
						S[i + j] = '+';
					else
						S[i + j] = '-';
				}
			}
		}

		bool chk = 1;
		for (int i = strlen(S) - K; i < strlen(S); i++)
		{
			if (S[i] == '-')
			{
				chk = 0;
				break;
			}
		}

		if (chk)printf("Case #%d: %d\n",Case + 1, cnt);
		else printf("Case #%d: IMPOSSIBLE\n",Case + 1);
	}

	return 0;
}