#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
using namespace std;

int main()
{
	FILE * fp, *fp2;
	fp=fopen("B-large.in", "r");
	fp2 = fopen("B-large.out", "w");
	int t;
	fscanf(fp,"%d\n", &t);
	//scanf("%d\n", &t);
	for (int a = 0; a<t; a++)
	{
		char arr[20];
		int size = -1;
		long long number, temp;
		char c;
		do
		{
			fscanf(fp, "%c", &c);
			//scanf("%c", &c);
			arr[size + 1] = c;
			size++;
		} while (c != '\n');
		arr[size] = NULL;
		int count = 1;
		bool confirm = 0;
		size = strlen(arr);
		int increase = 0;
		for (int i = 0; i < size - 1; i++)
		{
			if (arr[i] > arr[i + 1])//정렬 되었다면
			{
				confirm = 1;
				break;
			}
			else if (arr[i] < arr[i + 1])
			{
				increase = i + 1;
			}
		}
		if (confirm)
		{
			if (arr[increase] > '0')
				arr[increase]--;
			for (int i = increase + 1; i < size; i++)
			{
				arr[i] = '9';
			}
		}
		if (arr[0] == '0')
		{
			for (int i = 1; i <=size; i++)
				arr[i - 1] = arr[i];
		}
		fprintf(fp2,"Case #%d: %s\n",a+1,arr);
		//printf("Case #%d: %s\n", a + 1, arr);
	}
}