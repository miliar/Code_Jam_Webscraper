#include <iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		int length = s.length();
		for(int j=1;j<length;j++)
		{
			if(s[j]<s[j-1])
			{
				s[j-1]=s[j-1]-1;
				for(int k=j;k<length;k++)
				{
					s[k]='9';
				}
				for(int k=j-2;k>=0;k--)
				{
					if(s[k]>s[k+1])
					{
						s[k+1]='9';
						s[k]=s[k]-1;
					}
				}
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		int index=0;
		while(s[index]=='0')
		{
			index++;
		}
		while(index<length)
		{
			cout<<s[index];
			index++;
		}
		cout<<endl;
	}
}

