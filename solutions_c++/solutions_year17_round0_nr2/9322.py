#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t,tt;
	cin>>tt;
	for(t=1;t<=tt;t++)
	{
				
		long long int m,q,n=0;
		cin>>m;
		q=m;
		for(long int i=0;i<1000 && q>0;i++)
		{
			q=q/10;
			n++;
		}
		
		long int b[n]; 
		 
		
		for(long int i=n-1;i>=0;i--)
		{
			int temp;
			temp=m%10;
			b[i]=temp;
			m=m/10;
		}
		
		for(long int i=1;i<n;i++)
		{
			if(b[i-1]>b[i])
			{
				b[i-1]=b[i-1]-1;
				for(long int j=i;j<n;j++)
				{
					b[j]=9;
				}
				if(b[i-2]>b[i-1])
				{
					i=0;
				} 
				else i=n+1;
			}
		}
		
		// giving the output
		cout<<"Case #"<<t<<": ";
		if(b[0]==0)
		{
			for(long int i=1;i<n;i++)
			{
				cout<<b[i];
			}
		}
	    else
	    {
	    	for(long int i=0;i<n;i++)
	    	{
	    		cout<<b[i];
			}
		}
		cout<<endl;
		
	}
	return 0;
}
