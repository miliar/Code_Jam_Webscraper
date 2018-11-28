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
		cout<<"Case #"<<T-t<<": ";
		string s;
		cin>>s;
		if(s.length()>1)
		{
			for(int i=0;i<s.length()-1;i++)
			{
				if(s[i]>s[i+1])
				{
					if(i)
					{
						if(s[i]!=s[i-1])
						{
							s[i]--;
							for(int j=i+1;j<s.length();j++)
							{
								s[j]='9';
							}
						}
						else
						{
							int j(i-1);
							while(s[i]==s[j] && j>0)
								j--;
							if(j)
							{
								s[j+1]--;
								for(int k=j+2;k<s.length();k++)
								{
									s[k]='9';
								}
							}
							else
							{
								if(s[j]==s[i])
								{
									s[j]--;
									for(int k=j+1;k<s.length();k++)
									{
										s[k]='9';
									}
								}
								else
								{
									s[j+1]--;
									for(int k=j+2;k<s.length();k++)
									{
										s[k]='9';
									}
								}
							}
						}
					}
					else
					{
						s[i]--;
						for(int j=i+1;j<s.length();j++)
						{
							s[j]='9';
						}
					}
				}
			}
			while(s[0]=='0')
				s.erase(s.begin());
		}
		cout<<s<<'\n';
	}
}