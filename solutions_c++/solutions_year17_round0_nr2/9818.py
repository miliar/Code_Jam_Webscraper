#include<stdio.h>
#include<string.h>
char at[20],ent[20],tam;


void tidy(int p)
{
	if (tam-1>p)
	{
		if (at[p]<=at[p+1])
		{
			tidy(p+1);
		}
		else
		{
			at[p]=at[p]-1;
			for (int i=p+1;i<tam;i++)
				at[i]=9;
			tidy(p-1);
		}
	}
}


int main()
{
	int t;
	scanf ("%d",&t);
	for (int k=0;k<t;k++)
	{
		printf ("Case #%d: ",k+1);
		scanf (" %s", ent);
		//transformando caracter ascci em inteiro
		tam=strlen(ent);
		for (int i=0;i<tam;i++)
		{
			at[i]=ent[i]-'0';
		}
		tidy(0);
		for (int i=0;i<tam;i++)
		{	
			if (at[i]!=0)
				printf("%d",at[i]);
		}
		printf("\n");
	}
	return 0;
}
