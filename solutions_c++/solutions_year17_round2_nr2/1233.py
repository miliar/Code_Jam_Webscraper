#include <fstream>
#include <string>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

struct color
{
	color(char c, int count)
		: c(c), count(count)
	{ }

	char c;
	int count;
};

void print(ofstream& of, int tcase, const string& str)
{
	of << "Case #" << tcase << ": " << str << endl;
}

bool check(const string& str)
{
	for (auto i = 1; i < str.size() - 1; i++)
	{
		if (str[i - 1] == str[i] || str[i] == str[i + 1])
			return false;
	}
	return str[0] != str[str.size() - 1];
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int t;
	in >> t;

	for (auto tcase = 1; tcase <= t; tcase++)
	{
		int n;
		const int colorCount = 6;

		vector<color> colors = {
			color('R', 0),
			color('O', 0),
			color('Y', 0),
			color('G', 0),
			color('B', 0),
			color('V', 0)
		};

		in >> n;

		for (auto i = 0; i < colorCount; i++)
		{
			in >> colors[i].count;
		}

		string str;

		auto impossible = false;
		
		sort(colors.rbegin(), colors.rend(), [](auto a, auto b)
		{
			return a.count < b.count || a.count == b.count && a.c < b.c;
		});

		auto poss = colors[0].count <= colors[1].count + colors[2].count;

		while (true)
		{
			sort(colors.rbegin(), colors.rend(), [](auto a, auto b)
			{
				return a.count < b.count || a.count == b.count && a.c < b.c;
			});


			if (colors[0].count == 0)
				break;
			if (str.size() != 0 && colors[0].c == str[str.size() - 1])
			{
				if (colors[1].count > 0)
				{
					str += colors[1].c;
					colors[1].count--;
				}
				else
				{
					impossible = true;
					break;
				}
			}
			else
			{
				str += colors[0].c;
				colors[0].count--;
			}
		}

		const auto last = str.size() - 1;


		if (str.size() > 1 && str[0] == str[last])
		{
			auto c = str[last];
			str[last] = str[last - 1];
			str[last - 1] = c;
		}

		if (impossible || str[0] == str[last] || (str.size() > 1 && str[last - 1] == str[last - 2]))
		{
			assert(!poss);
			print(out, tcase, "IMPOSSIBLE");
		}
		else
		{
			assert(poss);
			assert(check(str));
			print(out, tcase, str);
		}
	}
}