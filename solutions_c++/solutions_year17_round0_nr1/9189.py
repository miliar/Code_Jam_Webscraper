#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

main()
{
	int t;
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for(int cases = 1; cases <= t; cases++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int n = s.size();
		int ret = 0;
		for(int i = 0; i <= n - k; i++)
		{
			if(s[i] != '+')
			{
				ret++;
				for(int j = i; j < i + k; j++)
					s[j] = (s[j] == '+') ? ('-') : ('+');
			}
		}
		bool invalid = false;
		for(int i = n - k; i < n; i++)
			if(s[i] != '+')
			{
				invalid = true;
				break;
			}
		
		if(invalid)
			cout<<"Case #" << cases << ": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #" << cases << ": "<< ret<<endl;
	}
}
