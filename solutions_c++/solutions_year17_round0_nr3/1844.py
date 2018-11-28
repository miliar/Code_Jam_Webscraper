#include <iostream>
#include <utility>

using namespace std;

#define For(i,a,b)  for(int i=(a);i<(b);++i)
#define rep(i,n)    For(i,0,(n))

pair<long long, long long> solve()
{
	long long N, K;

	cin >> N >> K;

	long long div = 1;
	while(K > (div << 1) - 1)
		div <<= 1;

	long long mx = (N - (div - 1)) / div;
	mx += (N - (mx * div + div - 1) >= (K - (div - 1))) ? 1 : 0;

	return make_pair(mx / 2, (mx - 1) / 2);
}

int main()
{
	int T;
	cin >> T;

	rep(i, T) {
		pair<long long, long long> r = solve();
		cout << "Case #" << (i + 1) << ": " << r.first << " " << r.second << endl;
	}
}
