#include <bits/stdc++.h>

using namespace std;

int cnt[10];
string mx;

void print(string s)
{
	if (s.length() == 1)
		cout << s;
	else
	{
		int i = 0;
		while (i < s.length() && s[i] == '0')
			i++;
		for (; i < s.length(); i++)
			cout << s[i];
	}
	cout << endl;
}

void bt(const string &up, int idx, int sum)
{
	if (idx > 9)
		return;
	if (idx == 9)
	{
		cnt[9] = up.size() - sum;
		string s;
		for (int i = 0; i <= 9; i++)
			s = s + string(cnt[i], i + '0');
		if (s <= up)
			mx = max(mx, s);
		return;
	}
	for (int i = 0; sum + i <= up.size(); i++)
	{
		cnt[idx] = i;
		bt(up, idx + 1, sum + i);
	}
}

int t;

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		string s;
		cin >> s;
		mx = string(s.length() - 1, '0' - 1);
		bt(s, 0, 0);
		cout << "Case #" << tt << ": ";
		print(mx);
	}
	return 0;
}