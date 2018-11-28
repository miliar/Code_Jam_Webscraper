#include<stdio.h>
#include<string.h>

int a[20];
char s[20];
int asize;
int ans[20];
int anssize;

bool istidy()
{
	bool tidy = true;
	for(int i = 0; i < anssize - 1; i++)
		if(ans[i] > ans[i+1])
		{
			tidy = false;
			break;
		}
	return tidy;
}

void findprev()
{
	int inv = -1;

	for(int i = 0; i < asize - 1; i++)
		if(a[i] > a[i + 1])
		{
			inv = i;
			break;
		}

	if(inv == -1)
	{
		anssize = asize;
		for(int i = 0; i < asize; i++) 
			ans[i] = a[i];
		return;
	}

	for(; inv >= 1; inv--)
		if(a[inv] != a[inv-1]) break;

	if(inv == 0 && a[inv] == 1)
	{
		anssize = asize - 1;
		for(int i = 0; i < asize; i++)
		{
			ans[i] = 9;
		}
	}
	else
	{
		for(int i = 0; i < asize; i++)
			ans[i] = a[i];

		ans[inv]--;
		anssize = asize;
		for(int i = inv + 1; i < asize; i++)
			ans[i] = 9;
	}
}



void decrement()
{
	for(int i = anssize - 1; i >= 0; i--)
	{
		if(ans[i] != 0)
		{
			ans[i]--;
			break;
		}
		else
		{
			ans[i] = 9;
		}
	}

	if(ans[0] == 0)
	{
		for(int i = 0; i < anssize - 1; i++)
			ans[i] = ans[i+1];

		anssize--;
	}
}

void findprev2()
{
	anssize = asize;
	for(int i = 0; i < asize; i++)
		ans[i] = a[i];

	while(!istidy())
		decrement();
}



int main()
{
	int t;
	scanf("%d", &t);
	for(int _t = 1; _t <= t; _t++)
	{
		scanf(" %s", s);
		asize = strlen(s);
		for(int i = 0; i < asize; i++) 
			a[i] = s[i] - '0';

		printf("Case #%d: ", _t);
		findprev();
		for(int i = 0; i < anssize; i++) 
			printf("%d", ans[i]);
		//test
		// findprev2();
		// printf("*");
		// for(int i = 0; i < anssize; i++) 
		// 	printf("%d", ans[i]);

		printf("\n");
	}
}