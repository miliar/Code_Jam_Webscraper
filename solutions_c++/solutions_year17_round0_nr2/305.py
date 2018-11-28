// B.cpp
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;

void getT(int& T)
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	ss >> T;
}

void getN(string& N)
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	ss >> N;
}

void tidy(string& s, int i)
{
	--s[i];
	for (++i; i < s.length(); ++i)
	{
		s[i] = '9';
	}  
}

void ltrim0(string &s) {
	while (s[0] == '0')
	  s.erase(0, 1);
}

string solve(string N)
{
	string result = N;

	if (result.length() > 1)
	{
		for (int i = result.length() - 2; i >= 0; --i)
		{
			if (result[i] > result[i+1])
			  tidy(result, i);
		}
		ltrim0(result);
	}

	return result;
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	getT(T);

	for (int t = 1; t <= T; ++t)
	{
		string N;
		getN(N);
		cout << "Case #" << t << ": " << solve(N) << endl;
	}

    return 0;
}

