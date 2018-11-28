#include<bits/stdc++.h>
using namespace std;

int main()
{
	
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int t;
	int x = 1;
	cin>>t;
	while(t--)
	{
		int ans = 1;
		int count = 0;
		string str;
		cin>>str;
		int k;
		cin>>k;
		int l = str.length();
		for(int i=0;i<l;i++)
		{
			if(str[i]=='+')
			continue;
			if(str[i]=='-')
			{
				if(l-i<k)
				{
					ans = 0;
					break;
				}
				else
				{
					count++;
					for(int j=i;j<i+k;j++)
					{
						if(str[j]=='+')
						str[j]='-';
						else if(str[j]=='-')
						str[j]='+';
					}
				}
			}
		}
		if(ans)
		cout<<"Case #"<<x<<": "<<count<<endl;
		else
		cout<<"Case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
		x++;
	}
}
