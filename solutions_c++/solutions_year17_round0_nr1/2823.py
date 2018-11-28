#include <iostream>
#include <string>
using namespace std;
 
int main()
{
	int t,it=1;
	cin>>t;
	while(it<=t)
	{
		string s;
		int k,i,n,j,b=1;
		cin>>s>>k;
		n=s.length(); 
		int a[n];
		for(i=0;i<n;i++)
		{
			if(s[i]=='+')
			{
				a[i]=1;
			}
			else
			{
				a[i]=0;
			}
		}

		int c=0;
		for(i=0;i<=n-k;i++)
		{
			if(a[i]==0)
			{
				c++;
				
				for(j=i;j<=i+k-1;j++)
				{
					a[j]=1-a[j];
				}
				

			}

		}
		for(i=0;i<n;i++)
		{
			if(a[i]==0)
			{
				b=0;
			}
		}
		if(b==1)
		{
			cout << "Case #" << it << ": " << c << endl;
		}
		else
		{
			cout << "Case #" << it << ": IMPOSSIBLE" << endl;
		}

		it++;
		

	}
	
 
 
 
	return 0;
} 