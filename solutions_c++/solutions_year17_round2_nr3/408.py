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

long long d[maxN][maxN];
double nd[maxN][maxN];
double e[maxN], s[maxN];
int u[maxN], v[maxN];

vector<double> solve(int n, int q)
{
	for (int k = 0; k < n; k++)
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (d[i][j] <= e[i])
				nd[i][j] = (double)d[i][j] / s[i];
			else
				nd[i][j] = 1e18;
		}
	}
	for (int k = 0; k < n; k++)
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				nd[i][j] = min(nd[i][j], nd[i][k] + nd[k][j]);

	vector<double> ans;
	for (int i = 0; i < q; i++)
	{
		ans.push_back(nd[u[i]][v[i]]);
	}
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
		int n, q;
		cin >> n >> q;
		for (int i = 0; i < n; i++)
		{
			cin >> e[i] >> s[i];
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> d[i][j];
				if (d[i][j] == -1)
					d[i][j] = 1e18;
			}
		}
		for (int i = 0; i < q; i++)
		{
			cin >> u[i] >> v[i];
			u[i]--;
			v[i]--;
		}
		
		cout.precision(10);
		cout << fixed << "Case #" << test << ": ";
		vector<double> tmp = solve(n, q);
		for (int i = 0; i < q; i++)
		{
			cout << fixed << tmp[i] << " ";
		}
		cout << "\n";
	}
	return 0;
}