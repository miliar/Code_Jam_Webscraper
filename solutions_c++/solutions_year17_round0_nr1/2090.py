#include<iostream>
using namespace std;

int main()
{
	FILE * fp, *fp1;
	fp = fopen("A-large.in", "r");
	fp1 = fopen("A-large.out", "w");
	int t;
	fscanf(fp,"%d", &t);
	for (int a = 1; a <= t; a++)
	{
		char c;
		char word[1001] = { 0 };
		int arr[1001] = { 0 };
		int k = 0;
		fscanf(fp,"%s", word);
		fscanf(fp,"%d", &k);
		int size = strlen(word);
		int index = 0;
		int sum = 0;
		for (int i = 0; i < size; i++)
		{
			if (word[i] == '+')
			{
				arr[i] = 1;
			}
		}
		int count = 0;
		bool confirm = 0;
		for (int i = index; index < size;)
		{
			i = index;
			if (!arr[i])
			{
				bool check = 0;
				int sum = 0;
				if (index + k > size)
				{
					confirm = 1;
					break;
				}
				for (int j = 0; j < k; j++)
				{
					arr[i + j] = 1 - arr[i + j];
					if (!arr[i + j])
					{
						check = 1;
					}
					if (!check)
					{
						index = i + j+1;
					}
					
				}
				count++;
			}
			else
				index++;
		}
		if(confirm)
			fprintf(fp1,"Case #%d: IMPOSSIBLE\n",a);
		else
			fprintf(fp1,"Case #%d: %d\n",a, count);
	}
}