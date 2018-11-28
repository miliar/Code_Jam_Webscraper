#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <limits>
#include <cmath>
#include <functional>
#include <list>
#include <numeric>
#include <string.h>

using namespace std;

#define ll	long long
#define ld	long double
#define vi	vector<int>
#define rep(i,a,b)	for(int i=a;i<b;i++)

ll pow2(ll a, ll b)
{
	if (b == 0)
		return 1;
	if (b == 1)
		return a;
	if (b % 2 == 1)
		return pow2(a, b / 2)*pow2(a, b / 2)*a;
	else
		return pow2(a, b / 2)*pow2(a, b / 2);
}

int CC(int x, int y) {
	ll ans = 1;
	vi ys(y - 1);
	iota(ys.begin(), ys.end(), 2);
	int y_ind = 0;
	//	for (int i = x + y; i > x; i--) {
	for (int i = x + 1; i < x + y + 1; i++) {
		ans *= i;
		if (y_ind < y - 1 && ans % ys[y_ind] == 0) {
			ans /= ys[y_ind++];
		}
		if (y_ind == y - 1 && ans >1000000007)
			ans %= 1000000007;
	}
	if (ans > 1000000007)
		ans %= 1000000007;

	return ans;
}


int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {

		string s;
		cin >> s;
		int K;
		cin >> K;
		int N = s.length();
		vector<char> v(N);
		int ans = 0;
		for (int n = 0; n < N; n++) {
			if (s[n] == '+')
				v[n] = 1;
			else
				v[n] = 0;
		}
		for (int n = 0; n < N - K + 1; n++) {
			if (v[n] == 0) {
				ans++;
				for (int j = 0; j < K; j++) {
					v[n + j] = !v[n + j];
				}
			}
		}
		for (int n = N - K; n < N; n++) {
			if (v[n] == 0) {
				ans = -1;
				break;
			}
		}
		if(ans < 0)
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << t + 1 << ": "<<ans<<endl;
	}
	return 0;
}