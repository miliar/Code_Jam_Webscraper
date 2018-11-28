#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <deque>
#include <string>

using namespace std;

#define pb push_back
#define mp make_pair
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define MAXS 1005

int T, casenum;
string sN;

int main()
{
	casenum = 1;
	cin >> T;
	while (T--)
	{
		string sSol;
		cin >> sN;
		if (sN.length() == 1)
			sSol = sN;
		else
		{
			int decPosition = 0, i = 0;
			while (i < sN.length() - 1 && sN[i] <= sN[i+1]) {
				if (i > 0 && sN[i] > sN[i - 1])
					decPosition = i;
				++i;
			}
			if (i > 0 && sN[i] > sN[i - 1])
				decPosition = i;

			if (i == sN.length() - 1)
				sSol = sN;
			else
			{
				if (!(decPosition == 0 && sN[0] == '1'))
				{
					for (int i = 0; i < decPosition; ++i)
						sSol.push_back(sN[i]);
					sSol.push_back(sN[decPosition] - 1);
					for (int i = decPosition + 1; i < sN.length(); ++i)
						sSol.push_back('9');
				}
				else
					for (int i = 0; i < sN.length() - 1; ++i)
						sSol.push_back('9');
			}
		}
		cout << "Case #" << casenum << ": " << sSol << endl;
		casenum++;
	}
	return 0;
}