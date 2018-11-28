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
	freopen("AL.in", "r", stdin);
	freopen("aLoutput.txt", "w", stdout);
	int t;
	cin >> t;
	for (int qt = 0; qt < t; ++qt) {

		int n, d;
		cin >> d >> n;
		vector<pair<int, int>> hs(n);
		for (int i = 0; i < n; ++i) {
			cin >> hs[i].first >> hs[i].second;
		}

		sort(hs.begin(), hs.end());

		long long iterations = 0;

		double l = 0, r = 1e18, eps = 1e-6, result = 0, eps2 = 1e-9;
		while ((r - l) > eps) {
			iterations++;
			double mid = (l + r) / 2;
			double time = d / mid;
			double overflow = false;
			for (auto& el : hs) {
				if ((mid) < el.second) {
					continue;
				}

				double t1 = el.first * 1.0 / (mid - el.second);
				if (t1  < time) {
					overflow = true;
					break;
				}
			}

			if (!overflow) {
				result = mid;
				l = mid *( 1 + eps2);
			}
			else {
				r = mid * (1 - eps2) ;
			}

		}

		cout << "Case #" << qt + 1 << ": " << fixed << setprecision(6) << result << endl;
	}
	
}