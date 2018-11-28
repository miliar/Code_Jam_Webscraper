#include <bits/stdc++.h>
using namespace std;
bool check(char *str)
{
	int len=strlen(str);
	if(len==1) return true;
	char pre=str[0];
	for(int i=1;i<len;i++)
	{
		if(str[i]<pre)
		{
			return false;
		}
		else
		pre=str[i];
			
	}
	return true;

}
int main()
{
   long long int val;
   char str[20];
   int t;
   freopen("B-small-attempt1.in","r",stdin);
   freopen("GCJ-OP.txt","w",stdout);
   scanf("%d",&t);
   for(int T=1;T<=t;T++)
   {
   	scanf("%s",str);
   	if(check(str))
   	{
   	
   	//	Case #1: 129
   		printf("Case #%d: %s \n",T,str);
   	//	printf("%s \n",str);	
   	}
   	else
   	{
   		long long val=atoll(str);
   	
   		val--;
   		sprintf(str,"%lld",val);;
   		if(check(str))
   		{
   	//		printf("%s \n",str);
   				printf("Case #%d: %s \n",T,str);
   		}
   		else
   		{
   			char ans[20]={'\0'};
   			int len=strlen(str);
   			char pre=str[0];
   			ans[0]=pre;
   			bool flag=0;
   			for(int i=1;i<len;i++)
   			{
   				if(flag)
   				{
   					ans[i]='9';
   				}
   				else if(str[i]>=pre)
   				{
   					pre=str[i];
   					ans[i]=str[i];
   				}
   				else
   				{
   					flag=1;
   					bool flag2=1;
   					int j=i-1;
   					ans[i]='9';
   					while((j>=0) && flag2)
   					{
   						ans[j]=char(ans[j]-1);
   						if((j>0) && (ans[j]>=ans[j-1] ) )
   						{
   							flag2=0;	
   						}
   						else
   						{
   							if(j!=0)
   							ans[j]='9';
   							j--;
   							if(j>0)
   							ans[j]=char(ans[j]-1);
   						}
   						
   						
   						
   					
   					}
   				}
   				//cout<<ans[i]<<" "<<ans[i-1]<<endl;;	
   			}
   			val=atoll(ans);
   	//		printf("%lld\n",val);
   				printf("Case #%d: %lld \n",T,val);
   			
   		
   		}
   	
   	}
   	
   	
   	
   
   }
	   
	   
   
   
   	return 0;
}
