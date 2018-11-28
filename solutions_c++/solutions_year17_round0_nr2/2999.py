#include <iostream>
#include <vector>
#include <deque>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>
#include <string>

using namespace std;

int T;
long long N;


long long solve()
{
	long long M = 1000000000000000000;
	long long res = 0;
	bool ready = false, start=false;
	int prev = N / M, count=0,n;
	N %= M;
	M /= 10;

	while(M)
	{
		n = ready ? 9 : (N / M); N %= M;  M /= 10;
		if (start || n || prev) start = true; else continue;
		if(n==prev && ++count) continue;
		if(n<prev)
		{
			res = res * 10 + (--prev ? prev : 9);
			count = count - (prev == 0 ? 1 : 0);
			prev = n = 9;
			ready = true;
		}
		while (count-->0) res = res * 10 + prev;
		count = (prev==9)?0:1;
		prev = n;
	}

	while (count--) res = res * 10 + prev;

	return res;
}

int main()
{
	cin >> T;

	for(int i = 0; i < T; ++i)
	{
		cin >> N;
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}
}