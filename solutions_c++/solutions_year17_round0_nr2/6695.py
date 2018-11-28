#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
FILE* out;
string Make_Max_Tidynum(string num);
void print_Tidy(string num);
int main()
{

	out = fopen("o.txt", "w");
	int _case;
	scanf("%d", &_case);
	for (int i = 1; i <= _case; i++)
	{
		string num;
		string Tidynum;
		cin >> num;
		//printf("Case #%d: ", i);
		fprintf(out,"Case #%d: ", i);
		Tidynum = Make_Max_Tidynum(num);
		print_Tidy(Tidynum);
	}
	fclose(out);
}
string Make_Max_Tidynum(string num)
{
	int fzero = 0;
	for (int i = 1; i < num.size(); i++)
	{

		for (int k = 0; k < num.size(); k++)
		{
			if (num[k] == '0')
				fzero = k + 1;
			else break;
		}

		if (num[i] >= num[i - 1])
			continue;
		else
		{
			num[i - 1] --;
			for (int j = i - 1; j >= fzero; j--)
			{
				if (j == fzero)
				{
					//num[j]--;
					for (int k = j+1; k <= num.size(); k++)
						num[k] = '9';
				}
				else if (num[j] < num[j - 1])
				{
					num[j - 1] --;
				}
				else
				{
					for (int k = j+1; k <= num.size(); k++)
					num[k] = '9';
					break;
				}
			}
			break;
		}
	}
	return num;
}
void print_Tidy(string num)
{
	bool Firstnum_exist = false;
	int size = num.size();
	for (int i = 0; i < size; i++)
	{
		if (!Firstnum_exist && num[i] == '0')
			continue;
		else
			//printf("%c", num[i]);
			fprintf(out,"%c", num[i]);
	}
	fprintf(out,"\n");
	return;
}