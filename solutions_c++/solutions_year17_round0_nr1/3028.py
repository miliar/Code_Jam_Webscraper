
//https://open.kattis.com/users/joseph-scott


#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <sstream>
#include <cstdint>
#include <cmath>
#include <vector>

using namespace std;


int main()
{
#if 1
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int ncase; cin >> ncase;
	for (int icase = 1; icase <= ncase; icase++)
	{
		string board; int k;
		cin >> board >> k;
		vector<bool> b(board.size());
		for (int i = 0; i < board.size(); i++)
		{
			b[i] = board[i] == '+' ? 1 : 0;
		}
		int ans = 0;
		for (int i = 0; i + k <= b.size() ; i++)
		{
			if (!b[i])
			{
				for (int j = i; j <i+ k; j++)
				{
					b[j] = !b[j];
				}
				ans++;
			}
		}
		bool imp = false;
		for (int i = 0; i < b.size(); i++)
		{
			if (!b[i])
			{
				imp = true;
				break;
			}
		}
		if (imp)
		{
			cout << "Case #" << icase << ": IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << icase << ": "<< ans << endl;
		}
	}
}
