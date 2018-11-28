#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("output_pan_large.out","w",stdout);
	int test;
	cin>>test;
	for(int m=0;m<test;m++)
	{
		int k,count=0;
		string s;
		cin>>s;
		cin>>k;      
		char c='y';
		int p=0;
		int size=s.size();
		for (int i = 0; i < size; ++i)
		{
			if (s[i] == '-')
			{
				count++;
				p=i+k;
				for (int j = i; j < p; ++j)
				{
					if(p > size)
						break;
					if (s[j] == '-')
					{
						s[j] = '+';
					}
					else
					{
						s[j] = '-';
					}
					
					//cout<<"hello"<<endl;
				}
				//cout<<"s : "<<s<<endl;		
			}
			
		}
		for (int i = 0; i < size; ++i)
		{
			if (s[i] == '-')
			{
				c='n';
				break;
			}
		}
		if (c=='n')
		{
			cout<<"Case #"<<m+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
			cout<<"Case #"<<m+1<<": "<<count<<endl;
	}
	return 0;
}