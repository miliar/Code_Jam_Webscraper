#include<iostream>



using namespace std;


int main()
{
	//ifstream fin();
	//ofstream fout();

	//FILE *fin = fopen("input.txt", "r");
	FILE *fin = fopen("A-large.in", "r");
	
	//FILE *fout = fopen("output.txt", "w+");
	FILE *fout = fopen("A-large.out", "w+");

	int T;
	int K;
	char S[1001];

	fscanf(fin, "%d", &T);

	for (int i = 1; i <= T; i++)
	{
		fscanf(fin, "%s", S);
		fscanf(fin, "%d", &K);

		int left = 0;
		int right = strlen(S);
		int result = 0;

		for (left = 0; left <= right - K; left++)
		{
			if (S[left] == '-')
			{
				result++;
				for (int k = left; k < left + K; k++)
				{
					S[k] = S[k] == '-' ? '+' : '-';
				}
			}
		}
		for (; left < right; left++)
		{
			if (S[left] == '-')
				result = -1;
		}
		
		if(result == -1)
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", i);
		else
			fprintf(fout, "Case #%d: %d\n", i, result);
	}



	return 0;
}