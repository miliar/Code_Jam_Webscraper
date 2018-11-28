#include <algorithm>
#include <cassert>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <unordered_map>

typedef unsigned uint;
typedef unsigned long long ulong;
using namespace std;
static const char nl = '\n';

ulong go(const string& s);

ulong fixup(ulong r)
{
	if(r == 0) return 0;
	ostringstream oss;
	oss << r;
	return go(oss.str());
}

ulong addDigit(ulong r,char d)
{
	r *= 10;
	r += d - '0';
	return r;
}

ulong go(const string& s)
{
	ulong retVal = 0;
	int index = -1;
	if(s.length() == 0) throw exception();
	retVal = addDigit(retVal,s[0]);
	bool hasCarried = false;
	for(uint i = 1;i < s.length();++i)
	{
		if(hasCarried) 
		{
			retVal = addDigit(retVal,'9');
		}
		else
		{
			if(s[i] >= s[i-1])
			{
				retVal = addDigit(retVal,s[i]);
			}
			else
			{
				retVal -= 1;
				retVal = fixup(retVal);
				retVal = addDigit(retVal,'9');
				hasCarried = true;
			}
		}
	}
	return retVal;
}

bool isTidy(ulong l)
{
	uint lastDigit = 9;
	while(l > 0)
	{
		uint currentDigit = l % 10;
		if(currentDigit > lastDigit) return false;
		l /= 10;
		lastDigit = currentDigit;
	}
	return true;
}

ulong go2(const string& s)
{
	ulong l;
	istringstream iss(s);
	iss >> l;
	while(l > 0)
	{
		if(isTidy(l)) return l;
		--l;
	}
	throw exception();
}

int main(int argc,char* argv[])
{
	#if 0
	ios_base::sync_with_stdio(false);
	string s("1000000000000000000");
	for(uint i = 1;i <= 100000;++i)
	{
		int index = i % s.length();
		char digit;
		if(index == 0)
		{
			digit = (rand() % 9) + '1'; 
		}
		else
		{
			digit = (rand() % 10) + '0';
		}
		s[index] = digit;
		ulong r = go(s);
		cout << s << ',' << r << nl;
		istringstream iss(s);
		ulong l;
		iss >> l;
		assert(r <= l);
		assert(isTidy(r));
	}
	#else
	ios_base::sync_with_stdio(false);
	uint T;
	cin >> T;
	string s;
	for(uint i = 0;i < T;++i)
	{
		cin >> s;
		cout << "Case #" << (i+1) << ": " << go(s) << nl;
	}
	#endif
	return 0;
}