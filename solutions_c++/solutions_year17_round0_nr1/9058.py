#include <bits/stdc++.h>
using namespace std;
char rev(char inp)
{
	if (inp == '-')
		return '+';
	else
		return '-';
}
int main()
{
	int t;
	while (cin>>t)
		for (int cnt = 1; cnt <= t; cnt++)
		{
			bool b = true;
			string s;
			int k;
			cin>> s>> k;
			int res = 0;
			for (int i = 0; i < s.size(); i++)
				if (s[i] == '-')
				{
					if (i+k > s.size())
					{
						b = false;
						break;
					}
					res++;
					for (int j = i; j < i+k; j++)
						s[j] = rev(s[j]);
				}
			if (b)
				cout<<"Case #"<<cnt<<": "<<res<<endl;
			else
				cout<<"Case #"<<cnt<<": IMPOSSIBLE\n";
		}
}
