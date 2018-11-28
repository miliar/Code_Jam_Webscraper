#include <stdio.h>

int SOL;
int NUM;

int itoa(int n, char s[])
{

	int i, sign;
	if((sign = n) <0)
	n = -n;
	i=0;

	do {
		s[i++] = n%10 +'0';

	} while((n/=10)>0);

	if(sign<0)
	s[i++]='-';
	s[i]='\0';
	//reverse(s);
	return i;
}


int solve(int number)
{
	char ns[20];
	int i = 0;
	int n;
	int size=0;

	n = number;

	while (n >= 0)
	{
		size=itoa(n, ns);

		for (i = size-1; i >= 1; i--)
		{
			if (ns[i] > ns[i-1]) {
				n--;
				break;
			}
		}

		if (i == 0)
			return n;
	}
	return 0;
}

int main()
{
	int T=0;
	FILE *out;
	//out = fopen("B-small-attempt2.out", "w");
	//freopen("B-small-attempt2.in","r",stdin);

	scanf("%d",&T);
	for (int testcase = 1; testcase <= T; testcase++)
	{
		scanf("%d",&NUM);
		SOL = solve(NUM);
		printf("Case #%d: %d\n", testcase, SOL);
		//fprintf(out,"Case #%d: %d\n",testcase,SOL);
	}
	fclose(out);
	return 0;
}