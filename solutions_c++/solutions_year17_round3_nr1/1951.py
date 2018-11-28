#include <iostream>
#include <iomanip>
#include <vector>
#include <utility>
#include <functional>
#include <algorithm>

using namespace std;

#define For(i,a,b)  for(int i=(a);i<(b);++i)
#define rep(i,n)    For(i,0,(n))

#define PI (long double(3.14159265358979323846264338327950288))

long double solve()
{
	int N, K;

	cin >> N >> K;

	vector<int> R(N);
	vector<int> H(N);
	rep(i, N)
		cin >> R[i] >> H[i];

	vector<pair<long long, long long>> pancake(N);
	rep(i, N)
		pancake[i] = make_pair(2 * long long(R[i]) * H[i], long long(R[i]) * R[i]);

	long long result = 0;
	long long rrmax = 0;
	rep(i, K) {
		long long tmp = 0;
		int index = 0;
		rep(i, N) {
			long long add = pancake[i].first + max(0LL, pancake[i].second - rrmax);
			if(tmp < add) {
				tmp = add;
				index = i;
			}
		}
		result += tmp;
		rrmax = max(rrmax, pancake[index].second);
		pancake[index] = make_pair(0LL, 0LL);
	}

	return PI * result;
}

int main()
{
	int T;
	cin >> T;

	rep(i, T) {
		cout << "Case #" << (i + 1) << ": " << fixed << setprecision(10) << solve() << endl;
	}
}
