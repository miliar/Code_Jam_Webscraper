#include<bits/stdc++.h>
/*
*/

using namespace std;
typedef  pair<pair<int, int>, pair<int, int>> area;
long long int R, C;
vector<string>calc(vector<string>input) {
	map<char, area>ans;
	map<char, pair<int, int>>point;

	for (size_t i = 0; i < R; i++)
	{
		for (size_t j = 0; j < C; j++)
		{
			if (input[i][j] != '?')
			{
				point[input[i][j]] = make_pair(i, j);
				if (ans.size() == 0)
				{
					ans[input[i][j]] = make_pair(make_pair(0, 0), make_pair(R - 1, C - 1));
				}
				else {
					for (auto now : ans) {
						if (now.second.first.first <= i&&i <= now.second.second.first&&now.second.first.second <= j&&j <= now.second.second.second)
						{
							if (point[now.first].first < i)
							{
								ans[input[i][j]] = ans[now.first];
								ans[now.first].second.first = point[now.first].first;
								ans[input[i][j]].first.first = point[now.first].first + 1;
							}
							else if (point[now.first].first > i) {
								ans[input[i][j]] = ans[now.first];
								ans[now.first].first.first = point[now.first].first;
								ans[input[i][j]].second.first = point[now.first].first - 1;
							}
							else {
								if (point[now.first].second < j)
								{
									ans[input[i][j]] = ans[now.first];
									ans[now.first].second.second = point[now.first].second;
									ans[input[i][j]].first.second = point[now.first].second + 1;
								}
								else {
									ans[input[i][j]] = ans[now.first];
									ans[now.first].first.second = point[now.first].second;
									ans[input[i][j]].second.second = point[now.first].second - 1;
								}
							}
							break;
						}
					}
				}
			}
		}
	}
	vector<string>ret(R, string(C, ' '));
	for (auto now : ans) {
		//cout << now.first << " " << now.second.first.first << " " << now.second.first.second << " " << now.second.second.first << " " << now.second.second.second << endl;
		for (size_t i = now.second.first.first; i <= now.second.second.first; i++)
		{
			for (size_t j = now.second.first.second; j <= now.second.second.second; j++)
			{
				ret[i][j] = now.first;
			}
		}
	}
	return ret;
}

int main() {
	long long int casenum;
	cin >> casenum;
	for (size_t index = 0; index < casenum; index++)
	{
		cin >> R >> C;
		vector<string>D(R);
		for (size_t i = 0; i < R; i++)
		{
			cin >> D[i];
		}
		auto ans = calc(D);
		cout << "Case #" << index + 1 << ":" << endl;
		for (size_t i = 0; i < R; i++)
		{
			cout << ans[i] << endl;
		}
	}
}
