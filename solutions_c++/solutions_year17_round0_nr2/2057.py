#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <map>
using namespace std;
#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 

VI digits(long long n)
{
	VI result;

	while (n)
	{
		result.push_back(n % 10);
		n /= 10;
	}
	reverse(ALL(result));

	return result;
}



bool good(long long n)
{
	VI d = digits(n);

	REP(i, d.size() - 1)
	{
		if (!(d[i + 1] >= d[i]))
			return false;
	}

	return true;
}

long long bf(int n)
{
	long long r = 0;
	REP(i, n)
	{
		if (good(i + 1))
			r = i + 1;
	}

	return r;
}




// BEGIN CUT HERE
int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);


	int T;
	cin >> T;

	REP(t, T)
	{
		long long n;
		cin >> n;

		VI d = digits(n);

		int i = 1;
		while (i < d.size() && d[i] >= d[i - 1])
		{
			++i;
		}

		if (i != d.size())
		{
			int p = d[i - 1];

			int j = i, k = i - 1;
			while (i < d.size())
			{
				d[i] = 9;
				++i;
			}
			
			while (k >= 0 && d[k] == p)
			{
				d[k] = p - 1;
				--k;
			}

			k += 2;
			while (k < d.size())
			{
				d[k++] = 9;
			}
		}

		string r = "";

		bool first = true;
		for (int i = 0; i < d.size(); ++i)
		{
			if (d[i] == 0 && first)
				continue;

			r += '0' + d[i];
			first = false;
		}

		if (r.size() < d.size())
			r = string(d.size() - 1, '9');


		//int rb = bf(n);
		//string e="";
		//for (int i = 0; i < digits(rb).size(); ++i)
		//{
		//	e += '0' + digits(rb)[i];
		//}

		//if (e != r)
		//	cout << "!";

		cout << "Case #" << (t + 1) << ": " << r << endl;

	}


}
// END CUT HERE
