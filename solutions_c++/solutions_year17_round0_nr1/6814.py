#include <iostream>
using namespace std;

#define ll long long

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		string s = "";
		int k;
		cin>>s>>k;
		string ss = s;
		int count1 = 0;
		int count2 = 0;
		int count = 0;

		int flag = 0;
		int flag2= 0;

		for (int i = 0; i < s.size()-k+1; ++i)
		{
			if(s[i] == '-')
			{
				count1++;
				for (int j = i; j < i+k; ++j)
				{
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		for (int i = 0; i < s.size(); ++i)
		{
			if(s[i] == '-')
				flag = 1;
		}
		if(flag == 0)
			count = count1;
		

		s = ss;
		for (int i = s.size()-1; i >= k; i--)
		{
			if(s[i] == '-')
			{
				count2++;
				for (int j = i; j > i-k; j--)
				{
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		for (int i = 0; i < s.size(); ++i)
		{
			if(s[i] == '-')
				flag2 = 1;
		}
		if(flag2 == 0)
		{
			if(flag == 0)
			{
				count = min(count1,count2);
			}
			else
				count = count2;
		}
		
		if(flag == 0 || flag2 == 0)
			cout<<"Case #"<<x<<": "<<count<<"\n";
		else
			cout<<"Case #"<<x<<": IMPOSSIBLE"<<"\n";
	}
	
	return 0;
}