#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	int k;
	string s;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	for(int i=0; i<T; i++)
	{
		cin>>s>>k;
		int st = 0;
		int flag = 1;
		int step = 0;
		while(1)
		{
			while(st < s.length() && s[st] == '+')
				st ++;
			if(st + k > s.length())
			{
				if(st < s.length())
					flag = 0;
				break; 
			}
			step ++;
			for(int j=st; j<st+k; j++)
			{
				if(s[j] == '-')
					s[j] = '+';
				else s[j] = '-';
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(flag)
			cout<<step;
		else cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}