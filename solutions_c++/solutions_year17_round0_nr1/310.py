// A.cpp
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

void getSK(string& S, int& K)
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	ss >> S >> K;
}

void putCounter(string& s,  int counter)
{
	stringstream ss;
	ss << counter;
	s = ss.str();
}

void flip(string& S, int i, int K)
{
	for (int k = 0; k < K; ++k)
	{
		if (S[i + k] == '-')
			S[i + k] = '+';
		else
			S[i + k] = '-';
	}
}

string solve(string S, int K)
{
	string result;
	int counter = 0;

	int i;
	for (i = 0; i + K <= S.length(); ++i)
	{
		if (S[i] == '-')
		{
			flip(S, i, K);
			++counter;
		}
	}
	putCounter(result, counter);
	for (; i < S.length(); ++i)
	{
		if (S[i] == '-')
		{
			result = "IMPOSSIBLE";
			break;
		}
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
		string S;
		int K;
		getSK(S,K);
		cout << "Case #" << t << ": " << solve(S, K) << endl;
	}

    return 0;
}

