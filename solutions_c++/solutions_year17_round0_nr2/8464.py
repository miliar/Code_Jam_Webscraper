#include<bits/stdc++.h>
using namespace std;
int main()
{
	
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-output1.out","w",stdout);
	
	int t,n;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		
		
		int a,c=0;
		for(int l=0;;l++)
		{
			a=n;
			for(int j=0;;j++)
			{
				a=a/10;
				c++;
				if(a==0)
					break;
			}
			int b=n,d;
			int a[c];
			for(int k=0;k<c;k++)
			{
				a[k]=b%10;
				b=b/10;
					
			}
			int cou=0;
			for(int k=0;k<c-1;k++)
			{
				if(a[k]-a[k+1]<0)
				{
					n=n-1;
					cou++;
					break;		
				}
			}
				if(cou==0)
				{
				
				cout<<"Case #"<<i<<": "<<n;
					goto a;
				}
		}
		a:
		
		cout<<endl;
	}
	
}
