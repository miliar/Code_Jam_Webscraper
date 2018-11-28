// 1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <queue>
#include <sstream>
#include <string>
#include <algorithm>
#include <iomanip>



using namespace std;

typedef unsigned long long ull;

int main()
{
	freopen("2.in", "r", stdin);
	freopen("2_out.txt", "w", stdout);

	int T; cin >> T;
	for (int tt = 1; tt <= T; ++tt)
	{
		ull tav;
		cin >> tav;
		int n;
		cin >> n;
		vector<long long> kezdo(n);
		vector<long long> speed(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> kezdo[i] >> speed[i];
		}
		long double maxido = 0;
		for (int i = 0; i < n; ++i)
		{
			ull tavolsag = tav - kezdo[i];
			long double ido = (long double)tavolsag / (long double)speed[i];
			if (ido > maxido) maxido = ido;

		}

		


		cout << "Case #" << tt << ": "<< setprecision(6)<<fixed<<((long double)tav/maxido)<< endl;
	}


    return 0;
}

