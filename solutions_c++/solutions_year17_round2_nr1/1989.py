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

typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		double D, N;
		cin >> D >> N;
		cout << "Case #";
		cout << t << ": ";
		double max_v = 0;
		for (int j = 0; j < N; j++)
		{
			double K, S;
			cin >> K >> S;
			max_v = max(max_v, (D - K) / S);
		}
		printf("%.10f", D/max_v);
		cout << endl;
	}

}
