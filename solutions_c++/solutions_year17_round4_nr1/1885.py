// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("a.in");
	ofstream out("a.out");

	int t;
	in >> t;
	for (int i = 0; i < t; i++)
	{
		int n,p;
		in >> n >> p;

		int leftovers[4] = {0,0,0,0};
		for (int j = 0; j < n; j++)
		{
			int g;
			in >> g;
			leftovers[g%p]++;
		}

		int cnt = leftovers[0];
		if (p == 2)
		{
			cnt += (leftovers[1]+1)/2;
		}
		else if (p == 3)
		{
			int cnt1 = min(leftovers[1],leftovers[2]);
			cnt += cnt1;

			int cnt2 = (leftovers[1] - cnt1)/3;
			cnt += cnt2;

			int cnt3 = (leftovers[2] - cnt1)/3;
			cnt += cnt3;

			if (cnt1*2 + cnt2*3 + cnt3*3 < leftovers[1] + leftovers[2])
				cnt++;
		}
		else if (p == 4)
		{
			cnt += leftovers[2]/2 + min(leftovers[1],leftovers[3]) + 1;
		}

		out << "Case #" << i+1 << ": " << cnt << endl;
	}

	in.close();
	out.close();

	return 0;
}

