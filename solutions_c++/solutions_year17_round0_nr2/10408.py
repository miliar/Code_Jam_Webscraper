#include <stdio.h>


int main()
{
	FILE* fi = fopen("sample.in", "r");
	FILE* fo = fopen("output.txt", "w");
	int t;
	fscanf(fi,"%d", &t);

	for (int i = 0; i < t; i++)
	{
		int n;
		bool check = false;
		fscanf(fi,"%d", &n);

		while (check != true)
		{
			int tmp = n;
			int num = tmp % 10;
			while (tmp != 0)
			{
				int rest = tmp % 10;
				tmp = tmp / 10;
				if (num >= rest)
				{
					check = true;
					num = rest;
				}
				else
				{
					check = false;
					break;
				}
			}
			if (check == true)
				break;
			else
				n--;
		}
		fprintf(fo,"Case #%d: %d\n", i + 1, n);

	}

	return 0;
}