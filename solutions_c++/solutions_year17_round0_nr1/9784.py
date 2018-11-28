#include <iostream>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <stdio.h>
#include <queue>
#include <string>

using namespace std;

typedef long long LL;

map<string, bool> used;

bool check(string &s)
{
	int cnt = 0;
	for (int i = 0; i < s.size(); i++)
		cnt += (s[i] == '+');
	return (cnt == s.size());
}



int solve(string s, int x)
{
	queue<pair<string, int> > q;
	q.push(make_pair(s, 0));
	while (!q.empty())
	{
		pair<string, int> nw = q.front();
		//cout << nw.first << " " << nw.second << "\n";
		q.pop();
		if (check(nw.first))
			return nw.second;
		if (used[nw.first])
			continue;
		used[nw.first] = true;

		for (int st = 0; st + x <= s.size(); st++)
		{
			string sv = nw.first;
			for (int j = 0; j < x; j++)
			{
				if (nw.first[st + j] == '-')
					nw.first[st + j] = '+';
				else
					nw.first[st + j] = '-';
			}
			q.push(make_pair( nw.first, nw.second + 1 ));
			nw.first = sv;
		}
	}
	return -1;

}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		used.clear();
		string s;
		int x;
		cin >> s >> x;
		int sl = solve(s, x);
		cout << "Case #" << i << ": ";
		if (sl != -1)
			cout << sl;
		else
			cout << "IMPOSSIBLE";
		cout << "\n";
	}
	return 0;
}