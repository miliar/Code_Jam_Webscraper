#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;scanf("%d",&t);
		
	for(int x=1;x<=t;x++)
	{
		string a;cin>>a;int n=a.size(),k;cin>>k;int res=0;
			
		for(int i=n-1;i>=k-1;i--)
		{
			if(a[i]=='-')
			{
				res++;
					
				for(int j=i;j>i-k;j--)
				{
					a[j] = (a[j] == '+' ? '-' : '+');
				}
			}
		}
			
		bool ans=true;
			
		for(int i=0;i<n;i++)
		{
			if(a[i]!='+')
			{
				ans=false;break;
			}
		}
			
		if(ans)
		{
			cout << "Case #" << x <<": "<< res << endl;
		}
		else
		{
			cout << "Case #" << x <<": "<< "IMPOSSIBLE" << endl;
		}
	}	
}	

