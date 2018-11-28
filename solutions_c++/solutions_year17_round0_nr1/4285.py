/*
 * 1.cpp
 *
 *  Created on: 08-Apr-2017
 *      Author: atulb
 */

#include <bits/stdc++.h>

using namespace std;

using LL = long long;
using ULL = unsigned long long;
#define vi vector<LL>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"


void solve(LL casenum)
{
	cout << "Case #" << casenum << ": ";

	string s;
	LL K;
	cin >> s >> K;
	LL flips = 0;

	LL N = s.size();

	for (LL i=0;i<N;++i)
	{
		if (s[i] == '+')
			continue;

		else if (i+K-1 >=N)
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}

		else
		{
			flips++;
			for (LL j=0; j <K;++j)
			{
				s[i+j] = s[i+j] == '-' ? '+' : '-';
			}
		}
	}

	cout << flips << endl;


}

int main()
{
   ios_base::sync_with_stdio(false);
   LL T;
   cin >> T;
   for (LL i=1;i<=T;++i)
   {
	   solve(i);
   }


   return 0;
}
