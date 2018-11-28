#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("sb.out","w",stdout);
	int T;
	cin>>T;
	for(int p=1;p<=T;p++)
	{
		int rem[2000];
		int need[2000];
		for(int i=0;i<2000;i++)rem[i]=0;
		int n,all;
		cin>>n>>all;
		int final;
		int min=-1;
		int max=-1;
		for(int i=0;i<all;i++)
		{
			
			 min=-1;
			 max=-1;
			for(int j=0;j<n;j++)
			{
				//printf("%d\n",rem[j]);
				if(rem[j])continue;
				int left=0;
				int right=0;
				for(int k=j-1;k>=0;k--)
				{
					if(rem[k])break;
					else left++;
				}
				for(int k=j+1;k<n;k++)
				{
					if(rem[k])break;
					else right++;
				}
				if(left>right)
				{
					int temp;
					temp=left;
					left=right;
					right=temp;
				}
				if(left>min)
				{
					final=j;
					min=left;
					max=right;
				}
				else if(left==min&&right>max)
				{
					final=j;
					min=left;
					max=right;
				}
				//cout<<left<<' '<<right<<"saf"<<endl;
			}
			//printf("asdf");
			rem[final]=1;
			//printf("%d %d %d\n",final,max,min);
			
		}
		printf("Case #%d: %d %d\n",p,max,min);
		
	}
 } 
