#include<bits/stdc++.h>
typedef long long int lli;
using namespace std;
int main()
{
	int t,k,a,b,c=1,count;
	string s;
	cin>>t;
	while(t--)
	{   count=0;
		cin>>s;
		cin>>k;
		a=0;
		b=s.length();
			for(int i=a;i<b;i++)
			{
						if(s[i]=='-')
						{
							a=i;
							break;
						}
						else
						{
							a=b+1;
						}
			}		
		while(a<b)
		{
					if(a+k-1>=b)
					{
						count=-1;
						break;
						//impossible
					}
					else
					{
					
					for(int j=a;j<a+k;j++)
					{
						if(s[j]=='-')
						{
							s[j]='+';
						}
						else
						{
							s[j]='-';
						}
						
					}
					for(int j=a;j<b;j++)
					{
						if(s[j]=='-')
						{
							a=j;
							break;
						}
						else
						{
							a=b+1;
						}
					}
					count++;
									
				}
			
		}
		cout<<"Case #"<<c<<": ";
		if(count>=0)
		{
			cout<<count<<"\n";
		}
		else
		{
			cout<<"IMPOSSIBLE\n";
		}
		c++;
	}
	return 0;
}
