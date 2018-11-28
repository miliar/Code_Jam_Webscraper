#include <bits/stdc++.h>

typedef unsigned long long ull;

using namespace std;

int main()
{
	int T;
	cin>>T;
	int t(T);
	while(t--)
	{
		string s;
		int k;
		cin>>s>>k;
		int flips(0);
		bool possible(true);
		cout<<"Case #"<<T-t<<": ";
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				if(s.length()-i<k)
				{
					possible=false;
					break;
				}				
				else
				{
					for(int j=i;j<i+k;j++)
					{
						s[j]=(s[j]=='+'? '-' : '+');
					}
					flips++;
				}
			}
		}
		if(possible)
		{
			cout<<flips<<'\n';
		}
		else
		{
			cout<<"IMPOSSIBLE\n";
		}
	}
}