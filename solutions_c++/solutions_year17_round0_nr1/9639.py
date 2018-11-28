#include<stdio.h>
#include<string.h>
int main()
{
	char A[1000];
	int t,n,len,i,out,h,check;
	scanf("%d",&t);
	for(int o=1;o<=t;o++)
	{
		out=0;
		scanf("%s %d",A,&n);	
		 i=0;
		len=strlen(A);
		while(A[i]!='\0')
		{
			if(out<len)
			{						
			if(A[i]=='-')
			{
				out++;
				check=i+n;
				if(len>=check)
				{				
				for(h=1;h<=n;h++)
				{				
					if(A[i]=='-' && A[i]!='\0')
					{
						A[i]='+';
						i++;
					}
					else if(A[i]=='+' && A[i]!='\0')
					{
						A[i]='-';
						i++;
					}
				}
			}
				i=0;
			}
		
		else if(A[i]=='+')
		{
		
			i++;
		}
	}
	else
	{
		break;
	}
		}
		
		if(out<len)
		{
			printf("case #%d: %d\n",o,out);
		}
		else
		{
			printf("case #%d: IMPOSSIBLE\n",o);
		}
	}
}
