#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ios::sync_with_stdio(0);
	freopen("A-large.in","r",stdin);
	freopen("xra.out","w",stdout);
	int test,tases = 1; cin >> test;
	while(test--)
	{
		string g; cin >> g;
		int s; cin >> s;
		int p = s;
		int cnt = 0;
		int res = 1000;
		while(res--)
		{
			p = s;
			int w = g.find('-');
			if(w == -1)
			{
				cout <<"Case #" << tases++<<": "<< cnt << endl;
				break;
			}
			else
			{
				if(w+s > g.size())
				{
					cout <<"Case #"<<tases++<< ": IMPOSSIBLE" << endl;
					break;
				}
				for(int i = w;p--;i++)
				{

					if(g[i] == '+') g[i] = '-';
					else g[i] = '+';
				}
				cnt++;
			}
		}
	}
	return 0;
}
/*
 *
 * 		---+++-+
 */
