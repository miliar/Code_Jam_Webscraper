#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		if(n>=10)
		{
			bool flag=false;
			while(flag==false)
			{
				string s=to_string(n);
				for(int j=1;j<s.length();j++)
				{
					if(s[j]<s[j-1])
					{
						flag=false;
						break;
					}
					else
					{
						flag=true;
					}
				}
				n--;
			}
			cout<<"Case #"<<i+1<<": "<<n+1<<"\n";
		}
		else if(n>=1)
		{
			cout<<"Case #"<<i+1<<": "<<n<<"\n";
		}
	}
	return 0;
}