// C.cpp 
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;

void getT(int& T)
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	ss >> T;
}

void getNK(long long& N, long long& K)
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	ss >> N >> K;
}

void solve(long long N, long long K, long long& max, long long& min)
{
	if (K == 1)
	{
		max = N/2;
		min = N/2;
		if (N % 2 == 0)
			--min;
		return;
	}

	if (K % 2 == 1 && N % 2 == 1)
	{
		solve(N/2, K/2, max, min);
		return;
	}
	if (K % 2 == 1 && N % 2 == 0)
	{
		solve(N/2 - 1, K/2, max, min);
		return;
	}
	if (K % 2 == 0 && N % 2 == 1)
	{
		solve(N/2, K/2, max, min);
		return;
	}
	if (N % 2 == 0 && K % 2 == 0)
	{
		solve(N/2, K/2, max, min);
		return;
	}
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	getT(T);

	for (int t = 1; t <= T; ++t)
	{
		long long N;
		long long K;
		getNK(N, K);

		long long max;
		long long min;
		solve(N, K, max, min);

		cout << "Case #" << t << ": " << max << " " << min << endl;
	}


    return 0;
}

