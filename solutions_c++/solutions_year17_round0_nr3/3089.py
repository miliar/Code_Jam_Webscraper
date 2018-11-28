#include <iostream>
#include <vector>
#include <deque>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>
#include <string>

using namespace std;

long long T,K,N;

tuple<long long , long long> solve()
{
	long long m = 0, n = 1, p = 1;
	bool r=false;

	while (true)
	{
		r = N % 2; N /= 2;

		if(K<=n+m) 
			return K <= n ? make_tuple(N, N-!r) : make_tuple(N-!r, N-1);
		K -= (n + m);
		r ? n = 2 * n + m : m = 2 * m + n;
	}
}

int main()
{
	cin >> T;

	for(int i = 0; i < T; ++i)
	{
		cin >> N >> K;
		tuple<long long, long long> r = solve();
		cout << "Case #" << i + 1 << ": " << get<0>(r) << " " << get<1>(r) << endl;
	}
}