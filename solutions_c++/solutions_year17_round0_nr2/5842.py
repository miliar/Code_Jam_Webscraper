#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)


// ---------------------------------------------------
// ---------------------------------------------------

bool ifTidy(long long N)
{
	stringstream strstream;
	strstream << N;

	string nstr;
	strstream >> nstr;

	for (int i = 1; i < nstr.size(); ++i) 
		if (nstr[i] < nstr[i-1])
		{
			return false;
		}

	return true;
}

long long minTidy(long long N)
{
	stringstream strstream;
	strstream << N;

	string nstr;
	strstream >> nstr;

	bool make9 = false;
	for (int i = 0; i < nstr.size()-1; ++i) 
	{
		if (nstr[i] > nstr[i+1] && !make9)
		{
			nstr[i] = nstr[i] -1; 
			make9 = true;
			continue;
		}

		if (make9) nstr[i] = '9';
	}

	if (make9) nstr[nstr.size()-1] = '9';

	// printf("nstr %s\n", nstr.c_str());

	return stoll(nstr);
}

int main()
 {
	if (1)
	{
		// freopen("B-small-attempt0.in", "r", stdin);
		// freopen("B-small-attempt0.out", "w", stdout);
		
		freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);

		int tt, tn; 
		cin >> tn;

		F1(tt,tn) 
		{
			long long N; 
			cin >> N;

			while (!ifTidy(N))
			{
				N = minTidy(N);
			}

			printf("Case #%d: %lld\n", tt, N);

		}
	}
	else
	{
		long long N = 1000;

		while (!ifTidy(N))
		{
			N = minTidy(N);
		}

		printf("%lld\n", N);
	}

	return 0;
}