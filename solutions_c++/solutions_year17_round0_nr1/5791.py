#include <bits/stdc++.h>

#define FOR(i, n) for(int i=0; i < n; i++)
#define FOR1(i, n) for(int i=1; i <= n; i++)

using namespace std;

constexpr int INF = 1000000000;

typedef long long ll;            // 19 digits
typedef unsigned long long llu;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> graph;

void print(const char* msg, ...);

int N, L, sol;

void getFlips(string s)
{
	//print("\nAnalyzing string '%s' with #flips = %d", s.c_str(), sol);
	if (s.size() <= L)
	{
		if (s.front() == '-')
			sol += 1;
		for(unsigned i=1; i < s.size(); i++)
		{
			if (s[i] != s.front())
				sol = INF;
		}
		return;
	}

	if (s.front() == '+')
		getFlips(s.substr(1));
	else
	{
		sol += 1;
		for(unsigned i=0; i < L; i++)
			s[i] = (s[i] == '+')? '-' : '+';
		getFlips(s.substr(1));
	}

}

int main()
{
	cin >> N;
	for(int TC=1; TC <= N; TC++)
	{
		//print("\nTEST %d - - - - - - -", TC);
		string s;
		cin >> s >> L;
		sol = 0;
		getFlips(s);

		if (sol == INF)
			printf("Case #%d: IMPOSSIBLE\n", TC);
		else
			printf("Case #%d: %d\n", TC, sol);
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