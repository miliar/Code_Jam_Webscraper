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
	in.open("B-large.in");
	out.open("B-large.out");

	int T;
	cin >> T;
	FOR(tc, 1, T + 1)
	{
		string s;
		cin >> s;
		bool nine = false;
		int k = 0;
		FOR(i, 1, s.length())
		{
			if (!nine && s[i - 1] > s[i])
			{
				s[k]--;
				i = k + 1;
				nine = true;
			}
			if (s[i] != s[k])
				k = i;
			if (nine)
				s[i] = '9';
		}
		reverse all(s);
		while (s.back() == '0')
			s.pop_back();
		reverse all(s);
		cout << "Case #" << tc << ": " << s << endl;
	}
	return 0;
}





