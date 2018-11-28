#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cstring>
#include <cmath>
#include <stack>
#define int long long
#define uint unsigned long long
#define CONTAINS(v,n) (find((v).begin(), (v).end(), (n)) != (v).end())
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define ARY_SORT(a, size) sort((a), (a)+(size))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
using namespace std;

int func(int n)
{
	int a = n;
	int min = 9;
	while (true)
	{
		int m = a % 10;
		if (m == 0)
		{
			return false;
		}
		if (m > min)
		{
			return false;
		}
		min = MIN(m, min);
		if (a < 10)
		{
			return true;
		}
		a /= 10;
	}
}

signed main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int a = 0;
		cin >> a;
		for (int k = a; k >= 1; k--)
		{
			if (func(k))
			{
				cout << "Case #" << (i + 1) << ": " << k << endl;
				break;
			}
		}
	}
}
