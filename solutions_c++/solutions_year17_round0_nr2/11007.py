#include<bits/stdc++.h>
using namespace std;
int main()
{   freopen("inp.txt","r",stdin);
    freopen("Paruout.txt","w",stdout);

	int t;
	cin>>t;
	  for(int i=1;i<=t;i++)
	{
		long long int p,yes=0,ans=0;
		cin>>p;
		while(yes==0)
		{
            long long int nn=p;
         	int ar[20];
	        int j=0;
	        while(nn!=0)
	        {
		        ar[j]=nn%10;
		        nn=nn/10;
		        j++;
	        }
	        int flag=0;
	        for(int x=0;x<j-1 && flag==0;x++)
	        {
		    if(!(ar[x]>=ar[x+1])) flag=1;
	        }
			if(flag==0)
			{
				ans=p;
				yes=1;
			}
			else p--;
		}
		printf("Case #%d: %lld\n",i,ans);
	}
}
