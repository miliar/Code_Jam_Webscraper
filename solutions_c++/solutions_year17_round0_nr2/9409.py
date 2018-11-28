#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,n,i,count,m,o,check;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    long long int a[20];
    for(i=0;i<20;i++)
    	a[i]=-1;
    long long int counter=1;
	while(t--)
	{
		cout<<"Case #"<<counter<<": ";
		counter++;
		count=0;
		cin>>n;
		m=n;
		o=n;
		while(m!=0)
		{
		    count++;
		    m=m/10;
		}
		long long int a[count];
        for(i=0;i<count;i++)
		{
		    a[i]=o%10;
		    o=o/10;
		}
		check=1;
		if(count>1)
		{
		for(i=0;i<count-1;i++)
			check=check*10;
			if(check==n)
				cout<<n-1<<endl;
		
			else
			{	
			
				for(i=0;i<count-1;i++)
				{
					if(a[i]<a[i+1])
					{
						a[i]=9;
						a[i+1]=a[i+1]-1;
						for(int j=i-1;j>=0;j--)
							a[j]=9;
						
					}
				}
				for(i=0;i<count;i++)
				{
					if(i==0)
					{
						if(a[count-1]!=0)
							cout<<a[count-1];
					}
					else
					cout<<a[count-1-i];
				}
				cout<<endl;
		
			}	
			
			
		}	
	
			else cout<<n<<endl;
		
		
	}
		
}