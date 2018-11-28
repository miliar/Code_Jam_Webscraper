#include<stdio.h>
#include<string.h>

FILE* INP;
FILE* OUP;

void test(int num);
void flip(char* arr, int num); 
bool check(char *arr);

int main()
{
	INP = fopen("C:\\inpoup\\inp.txt", "rt");
	OUP = fopen("C:\\inpoup\\oup.txt", "wt");
	int n;
	fscanf(INP, "%d", &n);
	for (int i = 0; i < n; i++)
	{
		test(i);
	}
	return 0;
}

void test(int num)
{
	int n, len;
	int tm = 0;
	char map[1010];
	fscanf(INP,"%s%d", map, &n);
	len = strlen(map);
	for (int i = 0; i <= len - n + 1; i++)
	{
		if (check(map))
		{
			fprintf(OUP, "Case #%d: %d\n", num + 1, tm);
			return;
		}
		else if(map[i] == '-')
		{
			flip(map + i, n);
			tm++;
		}
	}
	fprintf(OUP, "Case #%d: IMPOSSIBLE\n", num + 1);
}

bool check(char *arr)
{
	int i = 0;
	while (arr[i] != '\0')
	{
		if (arr[i] == '-') return false;
		i++;
	}
	return true;
}

void flip(char* arr, int num)
{
	for (int i = 0; i < num;i++)
	{
		if (arr[i] == '+') arr[i] = '-';
		else arr[i] = '+';
	}
}