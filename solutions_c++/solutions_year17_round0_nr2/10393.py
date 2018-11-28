#include<iostream>
#include<cstdio>
using namespace std;

int isTidy(int num)
{
	if (num<10) return 1;
	int number=num;
	int digit=0;
	while (number>=1)
	{
		number=number/10;
		digit++;
	}
	int bil[digit];
	number=num;
	for (int i=digit-1;i>=0;i--) 
	{
	    bil[i]=number%10;
	    number/=10;
	}
	for (int i=0;i<digit-1;i++) 
	{
		if (bil[i]>bil[i+1])
		return 0;
	}
	return 1;
}

int main()
{
	int T;
	scanf("%d",&T);
	//printf("T=%d\n",T);
	int N[T];
	for (int i=0;i<T;i++)
	scanf("%d",&N[i]);
	
	for (int i=0;i<T;i++)
	{
		if (isTidy(N[i])==1)
		{
			printf("Case #%d: %d\n",i+1,N[i]);
		}
		else
		{
			while (isTidy(N[i])==0)
			{
				N[i]--;
			}
			printf("Case #%d: %d\n",i+1,N[i]);
		}
	}
	
}
