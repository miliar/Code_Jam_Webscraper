#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

const char* impossible = "IMPOSSIBLE";

bool is_yellow(char c) { return c == 'Y' || c == 'O' || c == 'G'; }
bool is_red(char c) { return c == 'R' || c == 'O' || c == 'V'; }
bool is_blue(char c) { return c == 'B' || c == 'G' || c == 'V'; }

bool is_ok(string& s)
{
	const int n = s.size();
	for(int i = 0; i < n; ++i) {

		char c = s[i];
		char d = (i + 1 < n) ? s[i + 1] : s[0];

		if(is_yellow(c) && is_yellow(d))
			return false;
		if(is_red(c) && is_red(d))
			return false;
		if(is_blue(c) && is_blue(d))
			return false;
	}

	return true;
}

int main()
{
	int testcase;

	scanf("%d", &testcase);

	for(int casenum = 1; casenum <= testcase; ++casenum) {

		int n, r, o, y, g, b, v;

		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);

		assert(o + g + v == 0);

		if(r > n / 2 || y > n / 2 || b > n / 2) {
			printf("Case #%d: %s\n", casenum, impossible);
			continue;
		}

		vector<int> pos;
		pos.reserve(n);

		for(int i = 0; i < (n + 1) / 2; ++i)
			pos.push_back(i * 2);
		for(int i = 0; i < n / 2; ++i)
			pos.push_back(i * 2 + 1);

		string ans;
		ans.resize(n);

		vector<pair<int,char>> cs;

		cs.push_back({r, 'R'});
		cs.push_back({y, 'Y'});
		cs.push_back({b, 'B'});

		sort(cs.rbegin(), cs.rend());

		int it = 0;
		for(int i = 0; i < 3; ++i) {
			int x = cs[i].first;
			char c = cs[i].second;
			for(int i = 0; i < x; ++i)
				ans[pos[it++]] = c;
		}

		printf("Case #%d: %s\n", casenum, ans.c_str());
		assert(is_ok(ans));
	}

	return 0;
}
