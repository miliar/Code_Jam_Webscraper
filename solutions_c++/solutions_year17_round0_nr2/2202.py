#include<iostream>
using namespace std;

int main()
{	
	
	freopen("B-large.in","r",stdin);
	freopen("output5.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 1; i<=t; ++i)
	{
		string a;
		string z = "";
		cin>>a;
		a.push_back('a');
		int n = a.length();
		cout<<"Case #"<<i<<": ";
		int count = 0;
		for(int j = 0; j<=n-2; j++)
		{
			if(a[j]<a[j+1])
			{	
				while(count)
				{
					z.push_back(a[j]);
					count--;
				}
				z.push_back(a[j]);
				count = 0;
			}
			else if(a[j]==a[j+1])
			{
				count++;
			}
			
			else if(a[j] > a[j+1] && a[j]!='1')
			{
				z.push_back(a[j] - 1);
				for(int x = j+1-count; x<=n-2; x++)
					z.push_back('9');
				break;
			}
			
			else if(a[j] > a[j+1] && a[j]=='1')
			{
				for(int x = j+1-count; x<=n-2; x++)
					z.push_back('9');
				break;
			}
		}
		
		cout<<z;
		
		
	    cout<<"\n";
	}
	
	return 0;
}
