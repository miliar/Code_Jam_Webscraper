#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "B-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		int N, R, Ory, Y, Gyb, B, Vbr;
		cin >> N >> R >> Ory >> Y >> Gyb >> B >> Vbr;
		int r = R - Gyb;
		int y = Y - Vbr;
		int b = B - Ory;

		//cerr << Case << ": " << r << ' ' << y << ' ' << b <<endl;

		string res;
		if(r < 0 || b < 0 || y < 0)
			res = "IMPOSSIBLE";
		else if(R == Gyb && R > 0)
		{
			if(Ory + Y + B + Vbr > 0)
				res = "IMPOSSIBLE";
			else
			{
				res.assign(N, ' ');
				for(int i = 0; i < N; i += 2)
				{
					res[i] = 'R';
					res[i+1] = 'G';
				}
			}
		}
		else if(Y == Vbr && Y > 0)
		{
			if(R + Ory + Gyb + B > 0)
				res = "IMPOSSIBLE";
			else
			{
				res.assign(N, ' ');
				for(int i = 0; i < N; i += 2)
				{
					res[i] = 'Y';
					res[i+1] = 'V';
				}
			}
		}
		else if(B == Ory && B > 0)
		{
			if(R + Y + Gyb + Vbr > 0)
				res = "IMPOSSIBLE";
			else
			{
				res.assign(N, ' ');
				for(int i = 0; i < N; i += 2)
				{
					res[i] = 'B';
					res[i+1] = 'O';
				}
			}
		}
		else
		{
			std::vector<pair<int, char>> c = {{r, 'R'}, {y, 'Y'}, {b, 'B'}};
			sort(c.begin(), c.end());
			if(c[0].first + c[1].first < c[2].first)
				res = "IMPOSSIBLE";
			else
			{
				res.assign(r+b+y, ' ');
				int i = 0;
				while(c[0].first > 0 || c[1].first > 0 || c[2].first > 0)
				{
					//cerr << c[0].first << ' ' << c[1].first << ' ' << c[2].first << endl;
					res[i] = c[2].second;
					--c[2].first;
					++i;
					if(c[1].first > 0)
					{
						res[i] = c[1].second;
						--c[1].first;
						++i;
					}
					if(c[2].first + 1 == c[0].first)
					{
						res[i] = c[0].second;
						--c[0].first;
						++i;
					}
				}
				string res1;
				res1.assign(N, ' ');
				int j = 0;
				map<char, pair<char, int>> mp;
				mp['R'] = {'G', Gyb};
				mp['Y'] = {'V', Vbr};
				mp['B'] = {'O', Ory};
				for(int i = 0; i < res.size(); ++i)
				{
					res1[j] = res[i];
					++j;
					while(mp[res[i]].second > 0)
					{
						--mp[res[i]].second;
						res1[j] = mp[res[i]].first;
						++j;
						res1[j] = res[i];
						++j;
					}
				}
				res = res1;
			}
		}

		cout << "Case #" << Case << ": ";
		cout << res << endl;
	}

	return 0;
}
