#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#pragma comment(linker, "/STACK:16777216")

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <stack>
#include <set>
#include <queue>
#include <numeric>
#include <algorithm>
#include <utility>
#include <bitset>
#include <cmath>
#include <sstream>
#include <functional>

#define all(a) (a).begin(),(a).end()
#define sz(a) (int)(a).size()

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector<double> vd;
typedef vector< vd > vvd;
typedef vector< string > vs;
typedef pair< int, int > pii;
typedef vector< pii > vpii;



int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int T = 0;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		long long n;
		cin >> n;
		long long res = 0;
		long long curn = n;
		while (true)
		{
			stringstream ss;
			ss << curn;
			string s = ss.str();
			bool ok = true;
			int i = 0;
			for (i = 0; i < sz(s) - 1; i++)
				if (s[i] > s[i + 1])
				{
					ok = false;
					break;
				}

			if (ok)
			{
				res = curn;
				break;
			}

			for (int j = i + 1; j < sz(s); j++)
				s[j] = '0';
			curn = stoll(s);
			curn -= 1;
		}
		
		cout << "Case #" << t + 1 << ": ";
		// TODO: Answer here
		cout << res << endl;
	}

	return 0;
}