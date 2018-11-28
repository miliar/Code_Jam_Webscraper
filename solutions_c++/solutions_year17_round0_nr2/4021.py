#include<bits/stdc++.h>

using namespace std;

int main()
{
  	long long int testcase,n,f,i,j,k;
	char x;
  	cin>>testcase;
	for(long long int m=0;m<testcase;m++)
	{
		cin>>n;
		char s[100];
		sprintf(s,"%lld",n);
		int l = strlen(s);
		if(l==1)
		{
			printf("Case #%lld: %s\n",m+1,s);
			continue;
		}
		for(i=1;i<l;i++)
	      	{
			if(s[i]>=s[i-1])
			{	
				while(s[i]>=s[i-1])
				{
					i++;
				}
				if(i==l)
				{	
					if(s[0]=='0')
					{
						for(f=0;f<l-1;f++)
							s[f] = s[f+1];
						s[f] = '\0';
					}
					printf("Case #%lld: %s\n",m+1,s);
					break;
				}
				if(s[i-1]!=0)
				{
					for(k=i-1;k>0 && s[k]==s[k-1];k--);
					s[k] = s[k] - 1;
					k++;
					while(k!=l)
			    		{
						s[k] = '9';
						k++;
			    		}
					if(s[0]=='0')
					{
						for(f=0;f<l-1;f++)
							s[f] = s[f+1];
						s[f] = '\0';
					}
					printf("Case #%lld: %s\n",m+1,s);
					break;	
				}
			}
			else  /* For first char*/
			{
				s[i-1] = s[i-1] - 1;  /* Case of 0999 left */
				while(i!=l)
			    	{
					s[i] = '9';
					i++;
			    	}
				if(s[0]=='0')
				{
					for(f=0;f<l-1;f++)
						s[f] = s[f+1];
					s[f] = '\0';
				}
				printf("Case #%lld: %s\n",m+1,s);
				break; 
			}
		}
	}
	return 0;
}
 
 





