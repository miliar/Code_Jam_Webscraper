#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <algorithm>
#include <ctype.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;

const int inf = 1000000001;
const double eps = 10e-9;

stringstream out;

struct cmp
{
	bool operator() (const int& a, const int& b) const {
		return a < b;
	}
};
//----------------------------------

void func()
{
	string S;
	int K;
	cin >> S >> K;
	queue<int> limits;
	int c = 0;

	for (int i = 0; i < S.size(); ++i)
	{
		int s = limits.size();
		if ((S[i] == '-' && s % 2 == 0) || (S[i] == '+' && s % 2 == 1))
		{
			limits.push(i + K - 1);
			c++;
		}

		if (!limits.empty() && limits.front() == i)
			limits.pop();
	}
	if (limits.empty())
		out << c << endl;
	else
		out << "IMPOSSIBLE\n";
}

//----------------------------------

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		out << "Case #" << i << ": ";
		func();
	}
	cout << out.str();
	return 0;
}