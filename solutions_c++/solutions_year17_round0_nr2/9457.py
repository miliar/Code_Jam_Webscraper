#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	long long i,t;
	
	cin>>t;
	for(i=0;i<t;i++)
	{
		long long f=0,n,j,k=0,c,a[100],x,b=0;
		cin>>n;
		c=n;
		while(c!=0)
		{
			a[k++]=c%10;
			c=c/10;	
		}
		c=0;
		for(j=k-1;j>0;j--)
		{
			c++;
			if(a[j]>a[j-1])
			{
				if(f!=1)
				{
					a[j]=a[j]-1;
					for(j=0;j<k-c;j++) a[j]=9;
					break;
				}
				else
				{
					for(x=0;x<=b;x++) 
						a[x]=9;
					a[x]=a[x]-1;

				}
			}
			else if(a[j]==a[j-1] )
			{
				b++;
				f=1;
			}

		}
		c=0;
		for(j=k-1;j>=0;j--)
		{
			c+=a[j]*pow(10,j);
		}
		cout << "Case #" << i+1 << ": "<<c<<endl;

	}
}