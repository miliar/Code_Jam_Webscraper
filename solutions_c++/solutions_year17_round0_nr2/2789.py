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
		cin>>s;
		long long int i,j,ans=0;
		long long int n=s.length(); 
		long long int a[n];
		for(i=0;i<n;i++)
		{
			a[i]=s[i]-'0';
		}
		for(i=n-1;i>=1;i--)
		{
			if(a[i]<a[i-1])
			{
				for(j=i;j<n;j++)
					a[j]=9;

				a[i-1]-=1;
			}

		}
		for(i=0;i<n;i++)
		{
			ans*=10;
			ans+=a[i];
		}

		
		cout << "Case #" << it << ": "<< ans << endl;
		
		it++;
		

	}
	
 
 
 
	return 0;
} 