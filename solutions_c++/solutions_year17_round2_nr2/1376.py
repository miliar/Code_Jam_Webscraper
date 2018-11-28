#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int _case = 0; _case < cases; _case++)
	{
		int n, r, o, y, g, b, v;
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);

		r += o + v;
		y += o + g;
		b += g + v;

		string out_string = "";

		int upper_limit = n / 2;
		if (r > upper_limit || y > upper_limit || b > upper_limit)
			out_string = "IMPOSSIBLE";
		else
		{
			vector<int> indices;
			for (int i = 0; i < n; i++)
				if (i % 2 == 0)
					indices.push_back(i);
			for (int i = 0; i < n; i++)
				if (i % 2 == 1)
					indices.push_back(i);

			vector<pair<int, char>> colors;
			colors.push_back(make_pair(-r, 'R'));
			colors.push_back(make_pair(-y, 'Y'));
			colors.push_back(make_pair(-b, 'B'));
			sort(colors.begin(), colors.end());

			vector<char> str(n);
			for (int i = 0; i < n; i++)
				if (i < -colors[0].first)
					str[indices[i]] = colors[0].second;
				else if (i < -colors[0].first - colors[1].first)
					str[indices[i]] = colors[1].second;
				else
					str[indices[i]] = colors[2].second;

			for (int i = 0; i < n; i++)
				out_string += str[i];
		}

		cout << "Case #" << _case + 1 << ": " << out_string << endl;
	}

	return 0;
}