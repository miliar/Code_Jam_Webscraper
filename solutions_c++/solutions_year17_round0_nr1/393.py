#include<bits/stdc++.h>
using namespace std;
char s[1010];
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int t;
	int k=0;
	cin>>t;
	int cas=0;
	while(t--)
	{
	
		cas++;
		int flag=0;
		scanf("%s%d",s,&k);
		int sign=0;
		int  times=0;
		int n=strlen(s);
		for(int j=0;j<=n-k;j++){
			if(s[j]=='-'){
				times++;
				sign++;
				for(int i=0;i<k;i++)
				{
					if(s[i+j]=='-'){
						s[i+j]='+';
					}
					else
					{
						s[i+j]='-';
					}
					
				}
				
			}
			if(j==n-k){
				for(int i=0;i<k;i++)
				{
					if(s[i+j]=='-')
					{
						sign++;
						flag=1;
					}
				}
			}
			
		}
		if(sign==0)
		{
			printf("Case #%d: %d\n",cas,0);
		}
		else if(flag==1)
		{
			printf("Case #%d: IMPOSSIBLE\n",cas);
		}
		else 
		printf("Case #%d: %d\n",cas,times);
	}
	return 0;
}