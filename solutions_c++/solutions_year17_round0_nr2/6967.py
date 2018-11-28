#include <bits/stdc++.h>
using namespace std;

int main()
{
	int cs=1,t;
	string str;
	cin>>t;
	while(t--)
	{
		cin>>str;
		cout<<"Case #"<<cs++<<": ";
		int len = str.length();
		if(len==1)cout<<str<<endl;
		else
		{
			for(int i=len-2;i>=0;i--)
			{
				if(str[i]>str[i+1])
				{
					str[i]--;
					for(int j=i+1;j<len;j++)str[j]='9';
				}
			}

			int it = 0;
			while(str[it]=='0' and it<len-1)it++;
			str = str.substr(it);
			cout<<str<<endl;
		}
	}
}