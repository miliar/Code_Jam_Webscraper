#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

bool is(__int64 n)
{
	int last = 11;
	while (n > 0) 
	{
		int mod = n % 10;
		n /= 10;

		if (last < mod)
			return false;

		last = mod;
	}
	return true;
}

__int64 do_case(__int64 n)
{
	for (__int64 i = n; i > 0; --i) 
	{
		if (is(i))
			return i;
	}
	return 0;
}

int main() 
{
	int T;
	__int64 N;
	cin >> T;
	
	for (int i = 0; i < T; ++i) 
	{
		cin >> N;
		__int64 r = do_case(N);
		//printf("%s %d\n", S.c_str(), s);
			printf("Case #%d: %lld\n", i + 1, r);
	}

	return 0;
}