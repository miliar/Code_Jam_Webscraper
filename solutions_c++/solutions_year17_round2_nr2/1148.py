#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

string solve()
{
}

int main()
{
	int T;
	cin >> T;

	string colors = "ROYGBV";
	
	for (int t = 1; t <= T; t++)
	{
		int N;
		cin >> N;
		vector<pair<int, char> > horses;
		for (int i = 0; i < 6; i++)
		{
			int h;
			cin >> h;
			horses.push_back(make_pair(h, colors[i]));
		}
		sort(horses.rbegin(), horses.rend());
		
		string result;
		int lastColor = -1;
		
		for (int j = 0; j < N; j++)
		{
			int maxColor = -1;

			for (int i = 0; i < 6; i++)
				if (i != lastColor && horses[i].first > 0 && (maxColor < 0 || horses[i].first > horses[maxColor].first))
					maxColor = i;
			
//			cerr << maxColor << "\n";
			
			if (maxColor < 0)
			{
				result = "IMPOSSIBLE";
				break;
			}
			
			result.push_back(horses[maxColor].second);
			horses[maxColor].first--;
			lastColor = maxColor;
		}
		
		if (result[0] == result.back())
			result = "IMPOSSIBLE";

		cout << "Case #" << t << ": " << result << "\n";
	}
	
	return 0;
}

