#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <functional>
#include <random>
#include <ctime>
#include <cassert>
#include <unordered_map>

using namespace std;

#define N 100000
#define M 1850
mt19937 gen;
#define forn(i, n) for (int i = 0; i < n; i++)
#define piii pair<int, pair<int, int>>
#define pii pair<int, int>
#define forlrv(i, l, r) for (int i = r; i >= l; i--)
#define y(p) p.second
#define mp make_pair
#define mpp(a, b, c) mp(a, mp(b, c))
typedef long long ll;
#define forlr(i, l, r) for (int i = l; i <= r; i++)
#define p p2

ll solve(string s)
{
	forn(i, s.length())
	{
		int k = -1;
		for (int j = 1; j < s.length(); j++)
			if (s[j] < s[j - 1])
			{
				k = j;
				break;
			}

		if (k == -1) break;
		s[k - 1] = char(s[k - 1] - 1);
		forlr(j, k, s.length() - 1)
			s[j] = '9';
	}

	return stoll(s);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	string s;
	forn(i, t)
	{
		cin >> s;
		printf("Case #%d: %lld\n", i + 1, solve(s));
	}
}