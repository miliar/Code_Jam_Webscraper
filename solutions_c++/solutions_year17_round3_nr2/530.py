#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int solve()
{
	int AC, AJ;
	cin >> AC >> AJ;
	int N = AC + AJ;

	vector<pair<pair<int, int>, int> > A;
	
	for (int i = 0; i < AC; i++)
	{
		int c, d;
		cin >> c >> d;
		A.push_back(make_pair(make_pair(c, d), 1));
	}
	int needed = 720;
	for (int i = 0; i < AJ; i++)
	{
		int c, d;
		cin >> c >> d;
		A.push_back(make_pair(make_pair(c, d), 2));
		needed -= d - c;
	}
	
	cerr << "needed: " << needed << "\n";
	
	sort(A.begin(), A.end());
	
	vector<int> inc, dec;
	int neutral = 0;
	int switches = AJ;
	int prev = N - 1;
	int prevEnd = A[prev].first.second - 1440;
	for (int i = 0; i < N; i++)
	{
		int length = A[i].first.first - prevEnd;
		if (A[prev].second != A[i].second)
			neutral += length;
		else if (A[i].second == 1)
			inc.push_back(length);
		else
			dec.push_back(length);
		prev = i;
		prevEnd = A[prev].first.second;
	}
	
	sort(dec.begin(), dec.end());
	sort(inc.rbegin(), inc.rend());

	cerr << "dec\n";
	for (int d: dec)
	{
		if (needed < d)
			return switches;
		needed -= d;
		switches--;
		cerr << "needed: " << needed << "\n";
	}
	
	if (needed <= neutral)
		return switches;
	needed -= neutral;
	
	cerr << "inc\n";
	for (int i: inc)
	{
		switches++;
		if (needed <= i)
			return switches;
		needed -= i;
	}
	return switches;
}


int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": " << 2 * solve() << "\n";
	}
	
	return 0;
}

