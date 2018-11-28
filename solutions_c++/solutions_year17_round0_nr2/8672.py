#include <iostream>
#include <iterator>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <stack>

using namespace std;

bool isTidy(long long N)
{
	if (N < 10)
		return true;

	long long lastDig = 10;

	while (N && ((N % 10) <= lastDig))
	{
		lastDig = N % 10;
		N /= 10;
	}

	return !N;
}

long long getTidy(long long N)
{
	while (!isTidy(N)) --N;
	return N;
}

long long getTidy2(long long N)
{
	if (N < 10)
		return N;

	stack<int> digs;

	long long lastDig = 0;

	while (N)
	{
		digs.push(N % 10);
		N /= 10;
	}

	long long res = 0;

	while (!digs.empty() && (digs.top() >= lastDig))
	{
		res = 10 * res + digs.top();
		lastDig = digs.top();
		digs.pop();
	}

	if (!digs.empty())
	{
		--res;
		while (res && (res % 10) < ((res / 10) %10))
		{
			res /= 10;
			digs.push(0);
			--res;
		}

		while (!digs.empty())
		{
			res = 10 * res + 9;
			digs.pop();
		}
	}

	return res;
}

int main(int, char*[])
{   
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   
   istream_iterator<long long> it(cin);
   long long T = *it++;

   const long long c_T = T;

   while (--T >= 0)
   {
	   cout << "Case #" << c_T - T << ": " << getTidy2(*it++) << (T ? "\n" : "");
   }

   return 0;
}