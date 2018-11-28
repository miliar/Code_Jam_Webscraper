#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:160777216")
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <stack>
#include <queue>
#define PI acos(-1.0)
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define INF 10000
#define eps 1e-12
#define ll long long
#define f0(i , n) for (int i = 0; i < n; i++)
#define NMAX 5000

using namespace std;

int test, i, j, k , t;

ll n;

int good(ll n)
{
	
	int last = 10;
	while (n)
	{
		if (n % 10 > last)
			return 0;

		last = n % 10;
		n /= 10;
	}

	return 1;
}

ll getnew(ll n)
{
	VI v;
	while (n)
	{
		v.push_back(n % 10);
		n /= 10;
	}

	reverse(v.begin(), v.end());

	for (i = 0; i < v.size() - 1; i++)
	{
		if (v[i] > v[i + 1])
		{
			break;
		}
	}

	for (j = i + 1; j < v.size(); j++)
		v[j] = 0;

	ll tmp = 0;
	for (i = 0; i < v.size(); i++)
		tmp = tmp * 10 + v[i];

	return tmp - 1;

}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> test;
	for (t = 1; t <= test; t++)
	{
		cin >> n;
		while (!good(n))
		{
			n = getnew(n);
		}
		
		cout << "Case #" << t << ": " << n << endl;
	}
	return 0;
}