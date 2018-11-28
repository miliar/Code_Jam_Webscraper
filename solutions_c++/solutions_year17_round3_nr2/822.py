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
	freopen("Bs.in", "r", stdin);
	double  M_PI = 3.141592653589793238462643383279502884;
	freopen("atestoutput2.txt", "w", stdout);
	int t;
	int interval = 12 * 60;
	cin >> t;
	for (int qt = 0; qt < t; ++qt) {
		int a1, a2;
		cin >> a1 >> a2;
		vector<pair<int, int>> h1(a1), h2(a2);
		for (int i = 0; i < a1; ++i) {
			cin >> h1[i].first >> h1[i].second;
		}
		sort(h1.begin(), h1.end());
		for (int i = 0; i < a2; ++i) {
			cin >> h2[i].first >> h2[i].second;
		}
		sort(h2.begin(), h2.end());
		if (a1 + a2 <= 1 || (a1 == 1 && a2 == 1)){
			cout << "Case #" << qt + 1 << ": " << 2 << endl;
			continue;
		}
		else {
			if (a1 == 2) {
				int firstDiff = h1[1].second - h1[0].first;
				if (firstDiff <= 0) {
					firstDiff += 720*2;
				}
				int secondDif = h1[0].second - h1[1].first;
				if (secondDif <= 0) {
					secondDif += 720*2;
				}

				if (min(firstDiff, secondDif) <= interval) {
					cout << "Case #" << qt + 1 << ": " << 2 << endl;
					continue;
				}
				else {
					cout << "Case #" << qt + 1 << ": " << 4 << endl;
				}
			}
			else {
				int firstDiff = h2[1].second - h2[0].first;
				if (firstDiff <= 0) {
					firstDiff += 720*2;
				}
				int secondDif = h2[0].second - h2[1].first;
				if (secondDif <= 0) {
					secondDif += 720*2;
				}

				if (min(firstDiff, secondDif) <= interval) {
					cout << "Case #" << qt + 1 << ": " << 2 << endl;
					continue;
				}
				else {
					cout << "Case #" << qt + 1 << ": " << 4 << endl;
				}
			}
		}

		
	}

}