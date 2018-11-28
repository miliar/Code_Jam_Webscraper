#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fp;
	int count;
	int casecount=1;
	int i;
	char str[20];
	int num;
	int a,b;
	int result=0;
	int check=0;
	
	fp = fopen("A-small-attempt3.in","a+");
	
	fscanf(fp,"%d\n",&count);
	
	for(i=0;i<100;i++)
	{
		fscanf(fp,"%s %dn",str,&num);
		for(a=0;a<=strlen(str)-num;a++)
		{
			if(str[a]=='-')
			{
				for(b=a;b<a+num;b++)
				{
					if(b>strlen(str))
					{
						result--;
						break;
					}
					else if(str[b]=='-')
					{
						str[b] = '+';
					}
					else if(str[b]=='+')
					{
						str[b] = '-';
					}
				}
				result++;	
			}
		}
		for(a=0;a<strlen(str);a++)
		{
			if(str[a]=='-')
			{
				printf("Case #%d: IMPOSSIBLE\n",i+1);
				check=1;
				break;
			}
		}
		if(check==0)
		{
			printf("Case #%d: %d\n",i+1,result);
		}
		result = 0;
		check=0;
	}
	
	return 0;
}
