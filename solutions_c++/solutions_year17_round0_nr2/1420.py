#include <cstdio>
#include <cstring>

int main(int argc, char* argv)
{
	int T, t;

	char S[32];
	int S_Len;
	
	scanf("%d", &T);

	for (t = 1; t <= T; t++)
	{
		scanf("%s", S);
		S_Len = strlen(S);

		while (1)
		{
			int i;

			for (i = 0; i < S_Len - 1; i++)
			{
				if (S[i] > S[i + 1])
				{
					break;
				}
			}

			if (i == S_Len - 1)
			{
				break;
			}

			for (int j = i + 1; j < S_Len; j++)
			{
				S[j] = '9';
			}

			for (int j = i; j >= 0; j--)
			{
				if (S[j] > '0')
				{
					S[j]--;
					break;
				}
				else
				{
					S[j] = '9';
				}
			}
		}

		char *S_Start = S;

		while (*S_Start == '0' && *S_Start != '\0')
		{
			S_Start++;
		}

		printf("Case #%d: %s\n", t, S_Start);
	}

	return 0;
}