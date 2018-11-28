#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <cassert>

using namespace std;

#define sqr(x) ((x)*(x))

int pos[1450];
int arr[1000];
priority_queue <int> q;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	long double PI = 3.141592653589;
	for (int T = 0; T < t; T++)
	{
		cout << "case #" << T + 1 << ": ";
		int N, K;
		cin >> N >> K;
		double U;
		cin >> U;
		int UU = U * 1000000;
		for (int i = 0; i < N; i++)
		{
			double a;
			cin >> a;
			arr[i] = a * 1000000;
			q.push(-arr[i]);
		}
		while (UU > 0)
		{
			int V = -q.top();
			q.pop();
			if (V < 1000000)
			{
				V++;
			}
			UU--;
			q.push(-V);
		}
		double ans = 1;
		while (!q.empty())
		{
			ans *= ((-q.top() + 0.0) / 1000000);
			q.pop();
		}
		printf("%.10f", ans);
		cout << endl;
	}
}