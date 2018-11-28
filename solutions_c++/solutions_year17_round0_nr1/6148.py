#include<iostream>

using namespace std;

int main()
{
	int i,tc;
	cin>>tc;
	for(i=1;i<=tc;i++)
	{
		int c=0,flag=0;
		string s;
		cin>>s;
		int z,ln;
		cin>>z;
		ln=s.length();
		cout<<"Case #"<<i<<": ";
		for(int j=0;j<ln;j++)
		{
			if(s[j]=='-')
			{
				if(j<ln+1-z)
				{
					c++;
					for(int k=j;k<j+z;k++)
					{
						if(s[k]=='-')
							s[k]='+';
						else
							s[k]='-';
					}
				}
				else{
					cout<<"IMPOSSIBLE"<<endl;
					flag=1;
					break;
				}
			}
		}
		if(flag==0)
		cout<<c<<endl;
		
	}
	return 0;
}
