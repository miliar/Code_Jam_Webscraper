#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;
struct comparer
{
public:
	bool operator ()(pair<string, __int64> p1, pair<string, __int64>p2)
	{
		return p1.second > p2.second;
	}
};
int main()
{
	int T;
	cin >> T;
	cin.get();
	for (int N = 1; N <= T; N++)
	{
		string s;
		int k;
		__int64 cnt = -1;
		getline(cin, s, ' ');
		cin >> k;
		cin.get();
		int n = count(s.begin(), s.end(), '+');

		set<string> visited;
		priority_queue < pair<string, __int64>, deque<pair<string, __int64> >, comparer > q;
		q.push(pair<string, __int64>(s, 0));
		while (!q.empty())
		{
			pair<string, __int64> p = q.top();
			visited.insert(p.first);
			q.pop();
			if (count(p.first.begin(), p.first.end(), '+') == s.size())
			{
				cnt = p.second;
				break;
			}
			for (int i = 0; i <= p.first.size() - k; i++)
			{
				string ss = p.first;
				for (int j = i; j < i + k; j++)
				{
					ss[j] = (ss[j] == '+') ? '-' : '+';
				}
				if (visited.find(ss) == visited.end())
				{
					q.push(pair<string, _int64>(ss, p.second + 1));
				}
			}
		}
		cout << "Case #" << N << ": ";
		if (cnt == -1)
			cout << "IMPOSSIBLE";
		else
			cout << cnt;
		cout << endl;
	}
	return 0;
}