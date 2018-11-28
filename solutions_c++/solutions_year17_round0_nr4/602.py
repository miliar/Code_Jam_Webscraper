
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;

//Solution D for small and large
int main(void)
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		int n, m;
		cin >> n >> m;
		vector<int>b, r, c;
		set<pair<int, int>>han;
		vector<vector<int>>board(n, vector<int>(n));//斜め判定用
		int score = 0;
		for (int i = 0; i < m; ++i)
		{
			char bb; int rr, cc;
			cin >> bb >> rr >> cc;
			b.push_back((bb != '+') + (bb != 'x') * 2);
			r.push_back(rr - 1);
			c.push_back(cc - 1);
			board[rr - 1][cc - 1] = (bb != 'x');
			han.insert(make_pair(rr - 1, cc - 1));
			score += ((bb == 'o') ? 2 : 1);
		}
		map<pair<int, int>, int>ans;
		//縦横の判定
		{
			set<int>rs, cs;
			for (int i = 0; i < n; ++i)
			{
				rs.insert(i);
				cs.insert(i);
			}
			for (int i = 0; i < m; ++i)
			{
				if (b[i] & 1)
				{
					rs.erase(r[i]);
					cs.erase(c[i]);
				}
			}
			while (!rs.empty())
			{
				int nr = *rs.begin();
				int nc = *cs.begin();
				ans[make_pair(nr, nc)]++;
				++score;
				rs.erase(nr);
				cs.erase(nc);
			}
		}
		//斜めの判定
		{
			auto brd = [&](int p, int q)
			{
				if (p < 0 || p >= n || q < 0 || q >= n)return 0;
				return board[p][q];
			};
			auto insert = [&](int p, int q)
			{
				for (int i = 0; i < n; ++i)
				{
					if (brd(p + i, q + i) || brd(p + i, q - i) || brd(p - i, q + i) || brd(p - i, q - i))
						return;
				}
				board[p][q] = 1;
				ans[make_pair(p, q)] += 2;
				++score;
			};
			for (int cc = 0; cc < n; ++cc)
			{
				//(0,cc)に入れる
				insert(0, cc);
			}
			for (int cc = 1; cc < n - 1; ++cc)
			{
				//(n - 1,cc)に入れる
				insert(n - 1, cc);
			}
		}
		//ansから答えを抽出
		cout << "Case #" << test + 1 << ": ";
		cout << score << " " << ans.size() << endl;
		for (auto p : ans)
		{
			char outc = '_';
			switch (p.second)
			{
			case 1:outc = 'x'; break;
			case 2:outc = '+'; break;
			case 3:outc = 'o'; break;
			}
			if (outc != 'o')
			{
				if (han.find(make_pair(p.first.first, p.first.second)) != han.end())
				{
					outc = 'o';
				}
			}
			cout << outc << " " << p.first.first + 1 << " " << p.first.second + 1 << endl;
		}
	}
	return 0;
}
