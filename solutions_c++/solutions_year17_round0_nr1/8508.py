#include <iostream>
using namespace std;
int main()
{
	int t,k;
	string s;
	cin>>t;
	int t1=0;
	while(t1<t)
	{
		int count=0;
		cin>>s>>k;
		for(int i=0;i<=s.length()-k;i++)
		{
			if(s[i]=='-')
			{
				for(int j=0;j<k;j++)
				{
					if(s[i+j]=='-')
					s[i+j]='+';
					else
					s[i+j]='-';
				}
				count++;
			}
		}
		cout<<"Case #"<<t1+1<<": ";
		int flag=0;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
		{
			cout<<count<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		t1++;
	}
	return 0;
}

