#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cmath>
using namespace std;

int solve(int myH, int myA, int opH, int opA, int b, int d, int dt, int it)
{
	int res = 0;
	int cnt = 0;
	int myCurH = myH, opCurH = opH;
	while (cnt < dt)
	{
		if (myCurH <= opA - d)
			myCurH = myH;
		else
			opA = max(0, opA - d);
		cnt++;
		myCurH -= opA;
		if (myCurH <= 0)
			return -1;
		res++;
	}
	cnt = 0;
	while (cnt < it)
	{
		if (myCurH <= opA)
			myCurH = myH;
		else
			myA += b;
		cnt++;
		myCurH -= opA;
		if (myCurH <= 0)
			return -1;
		res++;
	}
	while (opH > 0)
	{
		res++;
		if (opH <= myA)
			return res;
		if (myCurH <= opA)
		{
			myCurH = myH;
			if (myH <= opA * 2)
				return -1;
		}
		else
			opH -= myA;
		myCurH -= opA;
		if (myCurH <= 0)
			return -1;
	}
	return res;
}

int main()
{
	int tt;
	
	cin >> tt;
	
	for (int t = 1; t <= tt; ++t)
	{
		int res = -1, hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		
		for (int i = 0; i < 400; ++i)
			for (int j = 0; j < 400; ++j)
			{
				int temp = solve(hd, ad, hk, ak, b, d, i, j);
				if (res == -1)
					res = temp;
				else if (temp != -1)
					res = min(res, temp);
			}
		
		cout << "Case #" << t << ": ";
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}

    return 0;
}
