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
	int digits[25];
	ll N;
	cin >> N;
	int size = 0;
	while (N)
	{
		digits[size++] = N % 10;
		N /= 10;
	}
	digits[size] = 0;
	bool allNines = false;

	for (int i = 0; i < size; i++)
	{
		if (digits[i] < digits[i + 1])
		{
			digits[i + 1]--;
			for (int j = i; j >= 0; j--)
				digits[j] = 9;
		}
	}
	int p = size;
	while (digits[p] == 0) p--;
	for (int i = p; i >= 0; i--)
	{
		out << (allNines == false ? digits[i] : 9);
	}
	out << endl;
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