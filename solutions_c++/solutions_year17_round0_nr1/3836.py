#define  _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:256000000")

#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <deque>
#include <queue>
#include <iomanip>
#include <fstream>
#include <string>

#define ll long long 
#define ld long double 
#define fi(n) for(int i = 0; i < (n); i++)
#define FOR(i, k, n) for(int i = (k); i < (n); i++)
#define all(a) (a.begin(), a.end())

const int INF = 2147483647;
const int mod = 1e9 + 7;
const long long lINF = 9223372036854775807;

using namespace std;

#define cin in
#define cout out

ifstream in;
ofstream out;

int main()
{
	in.open("A-large.in");
	out.open("aLarge.out");

	int T;
	cin >> T;
	FOR(tc, 1, T + 1)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		ll answ = 0;
		fi(s.length() - k + 1)
		{
			if (s[i] == '-')
			{
				answ++;
				FOR(j, i, i + k)
				{
					s[j] = ((s[j] == '+') ? '-' : '+');
				}
			}
		}
		bool pos = true;
		FOR(i, s.length() - k + 1, s.length())
			if (s[i] == '-')
				pos = false;
		cout << "Case #" << tc << ": ";
		if (pos)
			cout << answ << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}





