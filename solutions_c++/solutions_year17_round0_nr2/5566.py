// B.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

#include "bigInt.h"
// BigInt::Rossi n1 ("314159265358979323846264338327950288419716939937510", BigInt::DEC_DIGIT);
// int stoi (const string& str, size_t* idx = 0, int base = 10);
// string to_string (val);

#define FOR(i,n) for (int (i) = 0; (i) < (n); i++)
using namespace std;
typedef unsigned __int64 ulint;
typedef __int64 lint;

bool isValid(ulint n)
{
	ulint t = 9;
	while (n > 0)
	{
		if (n%10 > t)
			return false;
		else
		{
			t = n%10;
			n = n/10;
		}
	}

	return true;
}

ulint simple_resolve(ulint n)
{
	for (ulint i = n; i > 0; i--)
	{
		if (isValid(i))
			return i;
	}

	return 0;
}

bool valid(std::vector<ulint> &digits)
{
	for (int i = digits.size()-1; i > 0; i--)
	{
		if (digits[i] > digits[i-1])
			return false;
	}

	return true;
}

ulint getNumber(std::vector<ulint> &digits)
{
	ulint res = 0;
	ulint weight = 1;
	for (int i = 0; i < digits.size(); i++)
	{
		res = res + digits[i]*weight;
		weight *= 10;
	}

	return res;
}

ulint resolve(ulint n)
{
	std::vector<ulint> digits;
	ulint tmp = n;
	while (tmp > 0)
	{
		digits.push_back(tmp%10);
		tmp = tmp/10;
	}

	while (!valid(digits))
	{
		int i = 0;
		while (i < digits.size()-1 && digits[i] >= digits[i+1])
			i++;

		std::vector<ulint> tmpd(digits);
		tmpd[i] = 9;
		if (getNumber(tmpd) > n)
			digits[i+1] = digits[i+1] - 1;
		
		digits[i] = 9;
	}
	
	return getNumber(digits);
}

int main(void)
{
    //freopen("E:\\CodeJam\\B\\x64\\Debug\\in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	//ios::sync_with_stdio(false);

    int t = 0;
    std::cin >> t;
    
    FOR(i,t)
    {
		ulint n;

		std::cin >> n;

		//ulint res = simple_resolve(n);
		ulint tmpres = resolve(n);

		//if (res != tmpres)
			//std::cout << "fuck:" << n << '\t' << res << '\t' << tmpres << '\n';

		std::cout << "Case #" << i+1 << ": " << tmpres << endl;
    }

	return 0;
}


