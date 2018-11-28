#pragma region Header
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <queue>
#include <complex>
#include <bitset>
#include <random>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define print_var(x) cerr << #x << " = " << x << endl
#define print_array(arr, len) {cerr << #arr << " = "; for(int i = 0; i < len; ++i) cerr << arr[i] << ' '; cerr << endl;}
#define print_iterable(it) {cerr << #it << " = "; for(const auto& e : it) cerr << e << ' '; cerr << endl << endl;}
#define print_2d_array(arr, len1, len2) {cerr << #arr << ':' << endl;\
for(int i = 0; i < len1; ++i, cerr << endl) \
for(int j = 0; j < len2; ++j)\
cerr << arr[i][j] << ' '; \
cerr << endl; }
#define print_endl() cerr << endl
#else
#define eprintf(...) (void)0
#define print_var(x) (void)0
#define print_array(arr, len) (void)0;
#define print_iterable(it) (void)0;
#define print_2d_array(arr, len1, len2) (void)0;
#define print_endl() (void)0
#endif

#pragma endregion

typedef long long ll;
typedef pair<int, int> pii;

const int N = 105;
const int MASK = 1050;

string board0[N];
string board[N];
bool dp[N][MASK];
string how[N][MASK];
int p[N][MASK];
int r, c;

char sym[4] = { '.', '#', '-', '|' };

string from_mask(int mask)
{
	string res;
	for (int i = 0; i < c; i++)
	{
		res.push_back(sym[mask % 4]);
		mask /= 4;
	}
	return res;
}
int to_mask(string v)
{
	int res = 0;

	for (int i = v.size() - 1; i >= 0; i--)
	{
		int val;
		if (v[i] == '.')
			val = 0;
		if (v[i] == '#')
			val = 1;
		if (v[i] == '-')
			val = 2;
		if (v[i] == '|')
			val = 3;
		res = res * 4 + val;
	}
	return res;
}

char go(char was, char cur, bool shooted, bool &ok)
{
	if (was == '.')
	{
		if (cur == '.')
		{
			return '.';
		}
		if (cur == '#' || cur == '-')
		{
			ok = false;
			return '?';
		}
		if (cur == '|')
		{
			return '|';
		}
	}
	if (was == '#')
	{
		if (cur == '.' && shooted)
			cur = '#';
		return cur;
	}
	if (was == '|')
	{
		if (cur == '#')
		{
			return '#';
		}
		if (cur == '.')
		{
			return '|';
		}
		if (cur == '|' || cur == '-')
		{
			ok = false;
			return '?';
		}
	}
	if (was == '-')
	{
		if (cur == '.')
		{
			ok &= shooted;
			return was;
		}
		if (cur == '#' || cur == '-')
		{
			return cur;
		}
		if (cur == '|')
		{
			ok = false;
			return '?';
		}
	}
}

bool used[N][N];

bool check_all()
{
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			used[i][j] = false;

	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			if (board0[i][j] == '-')
			{
				for (int k = j - 1; k >= 0 && board0[i][k] != '#'; k--)
				{
					if (board0[i][k] != '.')
						return false;
					used[i][k] = true;
				}
				for (int k = j + 1; k < c && board0[i][k] != '#'; k++)
				{
					if (board0[i][k] != '.')
						return false;
					used[i][k] = true;
				}
			}

			if (board0[i][j] == '|')
			{
				for (int k = i - 1; k >= 0 && board0[k][j] != '#'; k--)
				{
					if (board0[k][j] != '.')
						return false;
					used[k][j] = true;
				}
				for (int k = i + 1; k < r && board0[k][j] != '#'; k++)
				{
					if (board0[k][j] != '.')
						return false;
					used[k][j] = true;
				}
			}
		}

	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			if (!used[i][j] && board0[i][j] == '.')
				return false;

	return true;
}

void solve()
{
	for (int i = 0; i < N; i++)
		for (int j = 0; j < MASK; j++)
		{
			dp[i][j] = false;
			how[i][j] = "";
			p[i][j] = -1;
		}

	scanf("%d%d", &r, &c);
	for (int i = 0; i < r; i++)
		cin >> board0[i];
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			if (board0[i][j] == '|' || board0[i][j] == '-')
				board0[i][j] = '*';
	swap(r, c);
	for (int i = 0; i < r; i++)
	{
		board[i].resize(c);
		for (int j = 0; j < c; j++)
			board[i][j] = board0[j][i];
	}

	int all = 1;
	string st = "";
	for (int i = 0; i < c; i++)
	{
		all *= 4;
		st.push_back('#');
	}

	dp[0][to_mask(st)] = true;
	for (int i = 0; i < r; i++)
	{
		print_var(i);
		for (int bmask = 0; bmask < all; bmask++)
		{
			if (!dp[i][bmask])
				continue;

			for (int shoot = 0; shoot < (1 << c); shoot++)
			{
				auto was = from_mask(bmask);

				string str = board[i];
				for (int j = 0; j < c; j++)
					if (str[j] == '*')
						if (shoot & (1 << j))
							str[j] = '|';
						else
							str[j] = '-';
				string str0 = str;

				bool shooted[10] = {};
				for (int j = 0; j < c; j++)
				{
					if (str[j] != '-')
						continue;
					for (int k = j - 1; k >= 0 && str[k] != '#'; k--)
						shooted[k] = true;
					for (int k = j + 1; k < c && str[k] != '#'; k++)
						shooted[k] = true;
				}

				bool ok = true;
				for (int j = 0; j < c; j++)
					if (shooted[j] && str[j] != '.')
						ok = false;

				for (int j = 0; j < c; j++)
				{
					str[j] = go(was[j], str[j], shooted[j], ok);
				}
				if (!ok)
					continue;

				int to = to_mask(str);
				dp[i + 1][to] = true;
				p[i + 1][to] = bmask;
				how[i + 1][to] = str0;
			}
		}
	}

	for (int bmask = 0; bmask < all; bmask++)
	{
		if (!dp[r][bmask])
			continue;
		string t = from_mask(bmask);
		bool ok = true;
		for (int i = 0; i < c; i++)
			ok &= t[i] != '.';
		if (!ok)
			continue;

		puts("POSSIBLE");

		vector<string> ans;
		for (int i = r; i > 0; i--)
		{
			ans.push_back(how[i][bmask]);
			bmask = p[i][bmask];
		}

		reverse(ans.begin(), ans.end());

		for (int i = 0; i < c; i++)
		{
			for (int j = 0; j < r; j++)
			{
				char c = ans[j][i];
				if (c == '|')
					c = '-';
				else if (c == '-')
					c = '|';
				board0[i][j] = c;
			}
		}

		for (int i = 0; i < c; i++)
			cout << board0[i] << endl;

		swap(r, c);
		/*if (!check_all())
			throw;*/

		return;
	}

	puts("IMPOSSIBLE");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		cout << "Case #" << test << ": ";
		solve();

		eprintf("DONE %d/%d in %.2lf\n", test, tests, (double)clock() / CLOCKS_PER_SEC);

	}

	eprintf("\n\ntime: %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
	return 0;
}