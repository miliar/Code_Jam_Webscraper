#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t ,k;
	string s;
	cin>>t;
	for(int x = 0; x < t;++x)
	{
		cin>>s>>k;
		int sz = s.size();
		int  c = 0;
		for(int i = 0; i <= sz -k; ++i)
		{
			if(s[i] == '-')
			{
				++c;
				for(int j = 0; j<k; ++j)
				{
					if(s[i+j] == '-')
						s[i+j] = '+';
					else
						s[i+j] = '-';
				}
			}
		}
		cout<<"Case #"<<x+1<<": ";
		int flag = 0;
		for(int i = 0; i < sz; ++i)
		{
			if(s[i] == '-'){
				flag = 1;
				break;
			}
		}
		if(flag == 0)
			cout<<c<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}