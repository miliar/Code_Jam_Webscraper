#include<iostream>

using namespace std;

char N[20];
char result[20];

int solve(int pos, int length)
{

	//������ ���� Ʈ��.
	if (pos == length)
	{
		//strcpy(result, N);
		return 1;
	}
	//ó�� �����ϴ� ��츸.
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
			//������ �����ϴ� ���. �ڸ� ���� 9�� ä��.
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
	//�� ���� ���.
	else
	{
		//�� ���ں��� ũ�ų� ����.
		if (N[pos - 1] <= N[pos])
		{
			if (solve(pos + 1, length))
			{
				return 1;
			}
			else
			{
				//�ڿ��ִ� �Ѱ��� ���ڰ� �� �۾Ƽ� �ǵ��ƿ�.
				N[pos] -= 1;
				if ( N[pos - 1] <= N[pos] &&
					N[pos] >= '0')
				{
					//������ �����ϴ� ���. �ڸ� ���� 9�� ä��.
					for (int i = pos+1; i < length; i++)
					{
						N[i] = '9';
					}

					strcpy(result, N);

					return 1;
				}
				else
				{
					//�����Ѱ�� ������ ���ư� ���� ��ġ�� 9�� ä��� �۾����� ���ư�.
					return 0;
				}
			}
		}
		//�� ���ں��� ����.
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