#include <iostream>
#include <iterator>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <stack>
#include <string>
#include <utility>
#include <queue>
#include <unordered_set>
#include <sstream>

using namespace std;

string getnexttry(const string& s, int offset, int K)
{
	string res(s);

	for (int i = 0; i < K; ++i)
	{
		res[offset + i] = (res[offset + i] == '+' ? '-' : '+');
	}

	return move(res);
}

bool need2try(const string& s, int offset, int K)
{
	return true; // for now!
	string res(s);

	for (int i = 0; i < K; ++i)
	{
		if ('-' == res[offset + i])
			return true;
	}

	return false;
}

int getswaps(string s, int K)
{
	string result(s.size(), '+');

	if (!s.compare(result))
	{
		return 0;
	}

	queue<pair<string, int>> q1;
	unordered_set<string> seen;

	seen.insert(s);
	q1.emplace(s, 0);

	while (!q1.empty())
	{
		auto cur = q1.front();
		q1.pop();

		for (int i = 0; i <= (s.size() - K); ++i)
		{
			if (need2try(cur.first, i, K))
			{
				string nextStep = getnexttry(cur.first, i, K);
				if (seen.count(nextStep))
					continue;

				if (!nextStep.compare(result))
				{
					return 1 + cur.second;
				}
				else
				{
					seen.insert(nextStep);
					q1.emplace(nextStep, 1 + cur.second);
				}
			}
		}
	}

	return -1;      
}

int main(int, char*[])
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	long long T = 0;

	string k_str;
	std::getline(cin, k_str);
	istringstream k_o(k_str);
	k_o >> T;

	const long long c_T = T;

	//char dummy = '0';
	//cin >> dummy;
	while (--T >= 0)
	{
		string s;
		int K = 0;

		std::getline(cin, k_str);
		istringstream k_o(k_str);
		getline(k_o, s, ' ');
		k_o >> K;

		//cin >> dummy;
		//std::getline(cin, s, ' ');
		//cin >> K;

		const int steps = getswaps(s, K);
		if (steps < 0)
		{
			cout << "Case #" << c_T - T << ": " << "IMPOSSIBLE" << (T ? "\n" : "");
		}
		else
			cout << "Case #" << c_T - T << ": " << steps << (T ? "\n" : "");
	}

	return 0;
}