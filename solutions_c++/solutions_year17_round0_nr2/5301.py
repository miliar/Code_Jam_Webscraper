#include<stdio.h>
#include<string.h>

FILE* INP;
FILE* OUP;

void test(int num);
bool BT(char *arr, int maxlen, long long int cur);
char* MAX(char *a, char *b)
{
	int alen = strlen(a), blen = strlen(b);
	if (alen == blen)
	{
		if (strcmp(a, b) > 0) return a;
		else return b;
	}
	else if (alen > blen) return a;
	else return b;
}

char val[20] = { 0 };
char max[20] = { 0 };

int main()
{
	INP = fopen("C:\\inpoup\\inp.txt", "rt");
	OUP = fopen("C:\\inpoup\\oup.txt", "wt");
	int n;
	fscanf(INP, "%d", &n);
	for (int i = 0; i < n; i++)
	{
		test(i);
		printf("Case#%d done\n", i + 1);
	}
	return 0;
}

void test(int num)
{
	val[0] = '\0';
	int len = 0;
	char map[20] = { 0 };
	fscanf(INP, "%s", max);
	len = strlen(max);
	for (int i = 1;i<10;i++)
	{
		map[0] = i + '0';
		BT(map, len, 1);
	}
	fprintf(OUP,"Case #%d: %s\n", num + 1, val);
}

bool BT(char *arr, int maxlen, long long int cur)
{
	bool pst = true;
	if (cur == maxlen)
	{
		arr[cur] = '\0';
		if (MAX(arr, max) == max)
		{
			strcpy(val, MAX(arr, val));
			return true;
		}
		return false;
	}
	arr[cur] = '\0';
	strcpy(val, MAX(arr, val));
	for (int i = arr[cur - 1] - '0'; i < 10; i++)
	{
		arr[cur] = i + '0';
		arr[cur + 1] = '\0';
		if(cur != maxlen - 1 || pst)pst = BT(arr, maxlen, cur + 1);
	}
	return true;
}