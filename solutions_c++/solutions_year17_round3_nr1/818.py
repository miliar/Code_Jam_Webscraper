#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <functional>
#include <math.h>
#include <iomanip>
#include <fstream>
using namespace std;

#define rep0(i, n) for(int i = 0; i < (n); ++i)
#define ll long long
#define pll pair<ll, ll>
#define vll vector<ll>
#define vpll vector<pll>
#define vvll vector<vll>

#define vb vector<bool>
#define has(a, n) (a.find(n) != a.end())

int prefix_function(string s, int m) {
	int n = (int)s.length();
	vector<int> pi(n);
	for (int i = 1; i < n; ++i) {
		int j = pi[i - 1];
		while (j > 0 && s[i] != s[j])
			j = pi[j - 1];
		if (s[i] == s[j])  ++j;
		pi[i] = j;
		if (pi[i] == m) {
			return i;
		}
	}

	return -1;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	freopen("Al.in", "r", stdin);
	double  M_PI = 3.141592653589793238462643383279502884;
	freopen("atestoutput2.txt", "w", stdout);
	int t;
	cin >> t;
	for (int qt = 0; qt < t; ++qt) {
		int n, k;
		cin >> n >> k;
		vector<pair<ll,ll>> in(n);
		for (int i = 0; i < n; ++i) {
			cin >> in[i].second >> in[i].first;
			in[i].first *= in[i].second;
		}

		sort(in.rbegin(), in.rend());
		ll currSum = 0;
		double surf = 0;
		for (int st = 0; st <n; ++st) {
			int counter = 1;
			ll sum = in[st].first;
			for (int j = 0; j < n && counter < k; ++j) {
				if (j == st)
					continue;
				if (in[st].second >= in[j].second) {
					sum += in[j].first;
					counter++;
				}
			}

			if (counter == k) {
				surf = max(surf, M_PI * 2 * sum + M_PI * in[st].second * in[st].second);
			}
			
		}
		


		cout << "Case #" << qt + 1 << ": " << fixed << setprecision(6) << surf  << endl;
	}

}