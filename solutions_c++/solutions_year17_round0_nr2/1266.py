#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n;
string s;

int nt(string s)
{
	int g = 0;
	for(int i = 0; i < s.length(); i++)
		g = (g * 10) + (s[i] - '0');
	return g;
}

string str(int x)
{
	if (!x) return "0";
	string s = "";
	while (x)
	{
		s += ('0' + (x % 10));
		x /= 10;
	}
	reverse(s.begin(), s.end());
	return s;
}

bool ok(int x)
{
	string s = str(x);
	for(int i = 0; i < s.length() - 1; i++)
	{
		if (s[i] > s[i + 1]) return false;
	}
	return true;
}

int main()
{
//	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out");

	in >> n;
	for(int i = 1; i <= n; i++)
	{
		in >> s;
//		int x = nt(s);
//		while (!ok(x))
//			x--;
//		out << "input #" << i << ": " << s << endl;
		int p = 0;
		while (p < s.length() - 1 && s[p] <= s[p + 1])
			p++;
//		out << "# " << p << endl;
		if (p == s.length() - 1)
		{
			out << "Case #" << i << ": " << s << endl;
			continue;
		}
		if (s[p] == '1')
		{
			out << "Case #" << i << ": ";
			string ans = "";
			for(int j = 0; j < s.length() - 1; j++)
				ans += "9";
			out << ans;
			out << endl;
			continue;
		}
//		for(int j = p + 1; j < s.length(); j++)
//			s[j] = '9';
		char tmp = s[p];
		while (p >= 0 && s[p] == tmp)
			p--;
		p++;
		s[p]--;
		for(int j = p + 1; j < s.length(); j++)
			s[j] = '9';
		out << "Case #" << i << ": " << s << endl;
	}
	return 0;
}
