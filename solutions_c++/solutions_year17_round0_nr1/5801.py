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
		string s;
		cin >> s;
		int k;
		cin >> k;
		int res = 0;
		bool ok = true;
		for (int i = 0; i < sz(s) - k + 1; i++)
		{
			if (s[i] == '-')
			{
				for (int j = i; j < i + k; j++)
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				res++;
			}
		}

		cout << "Case #" << t + 1 << ": ";
		// TODO: Answer here
		if (s.find('-') != string::npos)
			cout << "IMPOSSIBLE";
		else
			cout << res;
		cout << endl;
	}

	return 0;
}