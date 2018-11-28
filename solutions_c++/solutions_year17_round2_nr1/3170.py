#include <iostream>
#include <math.h>
#include <algorithm>
#include <array>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stdio.h>

using namespace std;

void solve(int t)
{
	long long hD;
	long long  hS;
	long long D, N;
	double maxT = 0;
	cin >> D >> N;
	//cout << D << " " << N << endl;
	for (int i = 0; i < N; i++)
	{
		cin >> hD >> hS;
		//cout << hD << " " << hS << endl;
		double t = (double)(D - hD) / (double)hS;
		if (t > maxT)
		{
			maxT = t;

		}
	}

	printf("Case #%d: %lf\n", t, (double)D / (double)maxT);
}


int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}

