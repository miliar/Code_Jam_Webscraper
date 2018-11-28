//i am vengence i am the night i am Batman
//ios_base::sync_with_stdio(false);cin.tie(NULL);
#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long int i,j,k,l,m,n,r,t,x,y,z;
	
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		cin>>k;
		n=k;r=0;x=0;
		vector<int> a;
		while(n!=0)
		{
			m=n%10;
			a.push_back(m);
			n=n/10;
			r++;
		}
		
		if(r==1)
		cout<<"Case #"<<i<<": "<<k<<"\n";
		else
		{
		while(x!=r-1)
		{
		x=0;	
		for(j=r-1;j>0;j--)
		{
			if(a[j]>a[j-1])
			{
				a[j]=a[j]-1;
				
				for(l=0;l<j;l++)
				{
					a[l]=9;
				}
			}
			else
			{
				x++;
			}
		}
		}
		
		z=0;
		cout<<"Case #"<<i<<": ";
		for(j=r-1;j>=0;j--)
		{
			if(a[j]!=0)
			{
				cout<<a[j];
				z=1;
			}
			if(a[j]==0 && z==1)
			{
				cout<<a[j];
			}
		}

		cout<<"\n";
		}
		
	}
	
    return 0;
}
