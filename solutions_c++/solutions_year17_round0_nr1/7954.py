#include <iostream>
#include <string>
#include <vector>
#include <queue> 
#include <algorithm>
using namespace std;

#define FOR(i,n) for(int i=0; i<n; i++)

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc; cin >> tc;
	FOR(k, tc)
	{
		cout << "Case #" << k+1 << ": ";
		string s; cin >> s; int n,ans=0; cin >> n;
		bool ok = 1;
		FOR(i, s.length())
		{
			if (s[i] == '-')
			{
				if (i + n -1< s.length())
				{
					ans++;
					for (int j = i; j < i + n; j++)
						if (s[j] == '+') s[j] = '-'; else s[j] = '+';
				}
				else
				{
					ok = 0; break;
				}
			}
		}
		if (ok) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
