#include <stdio.h>
#include <string.h>
#include <algorithm>

#define TEST_NUM "bb"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

char arr[100];
char res[100];

void process()
{
	bool u;
	int l, i, j;
	scanf("%s", arr);

	l = strlen(arr);

	for(i = 0; i<l; i++)
	{
		u = 1;
		for(j = i+1; j<l; j++)
		{
			if(arr[j] > arr[i])
				break;
			if(arr[j] < arr[i])
			{
				u = 0;
				break;
			}
		}

		if(u)
			res[i] = arr[i];
		else
		{
			res[i] = arr[i]-1;
			for(j = i+1; j<l; j++)
				res[j] = '9';
			break;
		}
	}

	res[l] = '\0';

	if(res[0] == '0')
		printf("%s", res+1);
	else
		printf("%s", res);
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
#ifdef _DEBUG
	fprintf(stderr, "\nYou are using DEBUG MODE!!!\n\n");
#endif
	char inname[100];
	char outname[100];
	sprintf(inname, "%s.in", TEST_NUM);
	sprintf(outname, "%s.out", TEST_NUM);
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
#endif
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for(ti = 1; ti<=tn; ti++)
	{
		fprintf(stderr, "Case %d/%d\n", ti, tn);
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}