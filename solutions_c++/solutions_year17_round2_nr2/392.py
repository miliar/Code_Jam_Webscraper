#pragma comment(linker, "/STACK:10000000000")
#include <map>
#include <unordered_map>
#include <set>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <time.h>
#include <iostream>
#include <stdio.h>
#include <queue>
#include <bitset>
#include <random>
#include <iterator>
#include <cassert>
#include <cstdint>
#include <string>
#include <numeric>

using namespace std;

#define LLD "%lld"

void print_str(const char* s)
{
	while (*s != 0)
	{
		putchar(*s);
		s++;
	}
}

template<typename T> void scan(T &t)
{
	cin >> t;
}

template<> void scan<int>(int &t)
{
	scanf("%d", &t);
}

template<> void scan<long long>(long long &t)
{
	scanf(LLD, &t);
}

template<> void scan<string>(string &t)
{
	cin >> t;
}

template<> void scan<char*>(char* &t)
{
	scanf("%s", t);
}

template<> void scan<char>(char &t)
{
	t = getchar();
	while (t <= 32)
		t = getchar();
}

template<> void scan<double>(double &t)
{
	scanf("%lf", t);
}

template<typename T> void scan(vector<T> &t)
{
	for (int i = 0; i < t.size(); i++)
	{
		scan(t[i]);
	}
}


template<typename T, typename... Ts> void scan(T& t, Ts&... ts)
{
	scan(t);
	scan(ts...);
}

template<typename T> void print(T t)
{
	cout << t;
}

template<> void print<string>(string s)
{
	print_str(s.c_str());
}

template<> void print<int>(int t)
{
	printf("%d", t);
}

template<> void print<long long>(long long t)
{
	printf(LLD, t);
}

template<> void print<char>(char t)
{
	putchar(t);
}

template<> void print<const char*>(const char* t)
{
	print_str(t);
}

template<> void print<double>(double t)
{
	printf("%lf", t);
}

template<typename T, typename V> void print(pair<T, V> t)
{
	printf("(");
	print(t.first);
	printf(", ");
	print(t.second);
	printf(")");
}

template<typename T, typename... Ts> void print(T t, Ts... ts)
{
	print(t);
	print(ts...);
}

#define TASK "hats"
#define X first
#define Y second

const int INF = 1e9;
const long long LINF = 3e18;
const int maxN = 110;
const int maxM = 5000 + 100;
const int K = 3000;
const int SIZE = (1 << 19);
const int mb = 30;
const long long MOD = 100000000000000003;
const long long P = 1009;
const double EPS = 1e-8;

mt19937_64 random_generator;

long long random(long long l, long long r)
{
	uniform_int_distribution<long long> dist(l, r);
	long long res = dist(random_generator);
	return res;
}

int r, o, y, g, b, v;

string solve(int n)
{
	vector<pair<int, char> > t;
	t.push_back(make_pair(r, 'R'));
	t.push_back(make_pair(y, 'Y'));
	t.push_back(make_pair(b, 'B'));
	sort(t.rbegin(), t.rend());
	string ans = "";
	for (int i = 0; i < t[0].first; i++)
	{
		ans.push_back(t[0].second);
	}
	if (t[1].first + t[2].first < t[0].first)
	{
		return ans = "IMPOSSIBLE";
	}
	int cnt = 0;
	for (int j = 0; j < t[1].first; j++)
	{
		bool found = false;
		for (int i = 0; i < (int)ans.size() - 1; i++)
		{
			if (ans[i] == t[0].second && ans[i + 1] == t[0].second)
			{
				ans.insert(ans.begin() + i + 1, t[1].second);
				cnt++;
				found = true;
				break;
			}
		}
		if (!found && ans.back() == t[0].second)
		{
			ans.push_back(t[1].second);
			cnt++;
		}
	}
	t[1].first -= cnt;
	cnt = 0;
	for (int j = 0; j < t[2].first; j++)
	{
		if (ans.back() == t[0].second)
		{
			cnt++;
			ans.push_back(t[2].second);
			continue;
		}
		for (int i = (int)ans.size() - 1; i > 0; i--)
		{
			if (ans[i] == t[0].second && ans[i - 1] == t[0].second)
			{
				ans.insert(ans.begin() + i, t[2].second);
				cnt++;
				break;
			}
		}
	}
	t[2].first -= cnt;
	for (int j = 0; j < t[1].first; j++)
	{
		if (ans.back() != t[1].second && ans[0] != t[1].second)
		{
			ans.push_back(t[1].second);
			continue;
		}
		for (int i = 0; i < (int)ans.size() - 1; i++)
		{
			if (ans[i] != t[1].second && ans[i + 1] != t[1].second)
			{
				ans.insert(ans.begin() + i + 1, t[1].second);
				break;
			}
		}
	}
	for (int j = 0; j < t[2].first; j++)
	{
		if (ans.back() != t[2].second && ans[0] != t[2].second)
		{
			ans.push_back(t[2].second);
			continue;
		}
		for (int i = 0; i < (int)ans.size() - 1; i++)
		{
			if (ans[i] != t[2].second && ans[i + 1] != t[2].second)
			{
				ans.insert(ans.begin() + i + 1, t[2].second);
				break;
			}
		}
	}
	if (ans.size() != n)
		return ans = "IMPOSSIBLE";
	for (int i = 0; i < (int)ans.size() - 1; i++)
	{
		if(ans[i] == ans[i + 1])
			return ans = "IMPOSSIBLE";
	}
	if (ans.back() == ans[0])
		return ans = "IMPOSSIBLE";
	return ans;
}



int main()
{
#ifdef _DEBUG
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#else
	//freopen(TASK".in", "r", stdin);
	//freopen(TASK".out", "w", stdout);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	scan(t);
	for (int test = 1; test <= t; test++)
	{
		int n;
		cin >> n;
		cin >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << test << ": ";
		string ans = solve(n);
		cout << ans << "\n";
	}
	return 0;
}