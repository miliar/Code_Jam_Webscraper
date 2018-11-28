#include <bits/stdc++.h>

#define FOR(i, n) for(int i=0; i < n; i++)
#define FOR1(i, n) for(int i=1; i <= n; i++)

using namespace std;

constexpr int INF = 1000000000;

typedef long long ll;            // 19 digits
typedef unsigned long long llu;

void print(const char* msg, ...);

bool isTidy(string s)
{
	char c = '\0';
	for(unsigned i=0; i < s.size(); i++)
	{
		if (s[i] > c)
			c = s[i];
		else if (s[i] < c)
			return false;
	}
	return true;
}

int main()
{
	int TC;

	cin >> TC;
	for(int tc=1; tc <= TC; tc++)
	{
		unsigned long long N;
		cin >> N;

		string cstr = to_string(N);
		while(isTidy(cstr) == false)
		{
			for(unsigned i=0; i < cstr.size()-1; i++)
			{
				if (cstr[i] > cstr[i+1])
				{
					cstr[i] -= 1;
					for(unsigned j=i+1; j < cstr.size(); j++)
						cstr[j] = '9';
					break;
				}
			}
		}

		printf("Case #%d: %llu\n", tc, stoull(cstr));
	}

	return EXIT_SUCCESS;
}

void print(const char* msg, ...)
{
	#ifndef ONLINE_JUDGE
		va_list argptr;
		va_start(argptr, msg);
		vfprintf(stderr, msg, argptr);
		va_end(argptr);
	#endif
}