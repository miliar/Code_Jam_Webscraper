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
#include <queue>

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
	int T;	cin >> T;
	for (int t = 0; t < T; t++) {
		string s;	cin >> s;
		int N = s.length();
		queue<char> ans;
		int n = 0;
		int cut = n;
		for (n = 0; n < N - 1; n++) {
			if (s[n] < s[n + 1]) {
				cut = n + 1;
			}
			else if (s[n]>s[n + 1]) {
				break;
			}
		}
		if (n == N - 1) {
			cout << "Case #" << t + 1 << ": "<<s<<endl;
			continue;
		}
		else {
			for (int i = 0; i < cut; i++) {
				ans.push(s[i]);
			}
			ans.push(s[cut] - 1);
			for (int i = cut + 1; i < N; i++) {
				ans.push('9');
			}
			for (int i = 0; i < N; i++) {
				if (ans.front() == '0')
					ans.pop();
				else
					break;
			}

			cout << "Case #" << t + 1 << ": ";
			int size = ans.size();
			for (int i = 0; i < size; i++) {
				cout << ans.front();
				ans.pop();
			}
			cout << endl;
		}
	}
	return 0;
}