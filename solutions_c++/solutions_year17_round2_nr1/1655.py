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
	LL D,N;
	cin >> D >> N;
    double t = 0;
	for (LL i = 0; i < N; ++i)
	{
		LL K,S;
		cin >> K >> S;
		double curr = double(D - K) / S;
		t = max(t, curr);
	}
	cout << std::fixed << std::setprecision(18) << double(D) / t << endl;
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
