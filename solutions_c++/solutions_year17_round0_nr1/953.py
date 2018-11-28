#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++)
	{
		string a;
		int k;
		cin>>a>>k;
		int ans = 0;
		for (int i = 0; i+k-1 < a.size(); i++)
			if (a[i] == '-')
			{
				ans++;
				for (int j = i; j <= i+k-1; j++)
					a[j] ^= '+' ^ '-';
			}
		for (int i = 0; i < a.size(); i++)
			if (a[i] == '-')
				ans = -1;
		if (ans == -1)
			cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<t<<": "<<ans<<endl;	
	}
	return 0;
}