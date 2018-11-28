#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	int i,k,j,t,f,m1,m2,p,l,t1=0;
	char s[100005];
	FILE *f1=freopen("A-large.in","r",stdin);
	FILE *f2=freopen("OUTPUT_2.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		t1++;
		scanf("%s%d",s,&k);
		l=strlen(s);
		f=0;
		if(l<k)
		{
			
		}
		else
		{
			for(i=0;i<=l-k;i++)
			{
				if(s[i]=='-')
				{
					f++;
					for(j=i;j<i+k;j++)
					{
						if(s[j]=='-')
						{
							s[j]='+';
						}
						else
						{
							s[j]='-';
						}
					}
				}
		    }
		    m1=m2=0;
			for(p=i-1;p<l;p++)
			{
				if(s[p]=='-')
				{
					m1++;
				}
			}
			if(m1==0)
			{
				printf("Case #%d: %d\n",t1,f);
			}
			else
			{
				printf("Case #%d: IMPOSSIBLE\n",t1);
			}
	    }
	}
	
	fclose(f1);
	fclose(f2);
	return 0;	
}
