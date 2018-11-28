#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, z=0;
	cin >> t;
	while (t--)
	{
		string str;
		cin >> str;
		int k;
		cin >> k;
		int ans=0;
		for (int i=0; i<str.size()-k+1; i++)
		{
			if(str[i] == '-'){
				for (int j=i; j<i+k; j++)
				{
					if(str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				ans++;
			}
		}
		for (int i=0; i<str.size(); i++)
		{
			if(str[i] == '-'){
				ans = -1;
			}
		}
		cout << "Case #" << ++z << ": ";
		if(ans == -1) puts("IMPOSSIBLE");
		else cout << ans << endl;
	}	
}
