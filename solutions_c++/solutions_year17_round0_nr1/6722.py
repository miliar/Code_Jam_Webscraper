#include<iostream>
#include<vector>
#include<string>
#include<cstdio>

using namespace std;

int Count_Flipping_Pancake(string state, int flipsize, int cakenum);

int main()
{
	FILE *out;
	out = fopen("output.txt", "w");
	int n;
	int cake, fliper;
	int count;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		string state;
		cin >> state;
		cake = state.size();
		cin >> fliper;
		count = Count_Flipping_Pancake(state, fliper, cake);
		//fprintf(out, "Case #%d: ", i);
		fprintf(out,"Case #%d: ", i);
		if (count == -1)
			fprintf(out, "IMPOSSIBLE\n");
			//printf("IMPOSSIBLE");
		else
			fprintf(out, "%d\n", count);
			//printf("%d", count);
	}
}
int Count_Flipping_Pancake(string state, int flipsize, int cakenum)
{
	int count = 0;
	for (int i = 0; i < cakenum; i++)
	{
		if (state[i] == '-')
		{
			if (i + flipsize - 1 < cakenum)
			{
				for (int j=i; j < i + flipsize; j++)
				{
					if (state[j] == '-')
						state[j] = '+';
					else
						state[j] = '-';
				}
				count++;
			}
			else
				return -1;
		}
	}
	return count;
}