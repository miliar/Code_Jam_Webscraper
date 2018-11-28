#include <bits/stdc++.h>
using namespace std;
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)

void dfs(string s, string t)
{
	if(s > t)
		return;
	if(s.length() == t.length())
		throw s;
	char tc = s.empty() ? '1' : *--s.end();
	h(c, '9', tc)
		dfs(s + (char) c, t);
}

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		string s; cin >> s;
		string t = "";
		while(t.length() < s.length())
			t += '1';
		if(s < t)
		{
			printf("Case #%d: ", _);
			g(__, 1, s.length())
				putchar('9');
			putchar('\n');
			continue;
		}
		try
		{
			dfs("", s);
			cerr << "WTF?" << endl;
		}
		catch(string u)
		{
			printf("Case #%d: %s\n", _, u.c_str());
		}
	}
	return 0;
}
