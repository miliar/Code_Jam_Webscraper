#include<iostream>

using namespace std;

char N[20];
char result[20];

int solve(int pos, int length)
{

	//만약을 위한 트랩.
	if (pos == length)
	{
		//strcpy(result, N);
		return 1;
	}
	//처음 시작하는 경우만.
	else if (pos == 0)
	{
		if (solve(pos + 1, length))
		{
			char *p;
			for (p = N; *p == '0'; p++);

			strcpy(result, p);

			return 1;
		}
		else
		{
			N[pos] -= 1;
			//조건을 만족하는 경우. 뒤를 전부 9로 채움.
			for (int i = pos + 1; i < length; i++)
			{
				N[i] = '9';
			}

			char *p;
			for (p = N; *p == '0'; p++);

			strcpy(result, p);

			return 1;
		}
	}
	//그 외의 경우.
	else
	{
		//전 숫자보다 크거나 같음.
		if (N[pos - 1] <= N[pos])
		{
			if (solve(pos + 1, length))
			{
				return 1;
			}
			else
			{
				//뒤에있는 한가지 숫자가 더 작아서 되돌아옴.
				N[pos] -= 1;
				if ( N[pos - 1] <= N[pos] &&
					N[pos] >= '0')
				{
					//조건을 만족하는 경우. 뒤를 전부 9로 채움.
					for (int i = pos+1; i < length; i++)
					{
						N[i] = '9';
					}

					strcpy(result, N);

					return 1;
				}
				else
				{
					//실패한경우 앞으로 돌아가 현재 위치도 9로 채우는 작업으로 돌아감.
					return 0;
				}
			}
		}
		//전 숫자보다 작음.
		else
		{
			return 0;
		}

	}
}


int main()
{
	//ifstream fin();
	//ofstream fout();

	//FILE *fin = fopen("input2.txt", "r");
	FILE *fin = fopen("B-large.in", "r");

	//FILE *fout = fopen("output2.txt", "w+");
	FILE *fout = fopen("B-large.out", "w+");

	int T;
	
	
	int length;
	

	fscanf(fin, "%d", &T);

	for (int i = 1; i <= T; i++)
	{

		fscanf(fin, "%s", &N);
		length = strlen(N);

		solve(0, length);

		fprintf(fout, "Case #%d: %s\n", i, result);
	}



	return 0;
}