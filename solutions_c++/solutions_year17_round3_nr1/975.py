#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

#define EPS 1e-9

using namespace std;

typedef pair<int, int> ii;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef pair<ll, ll> llll;
typedef vector<llll> vllll;

const double pi = atan(1.0) * 4.0;

int main() {
	
	int t; cin >> t;
	int cas = 1;
	while (t--) {
		cout << "Case #" << cas << ": ";
		cas++;


		int n, k; cin >> n >> k;


		vllll pancakes = vllll();
		for (int i = 0; i < n; i++)
		{
			ll r, h; cin >> r >> h;
			pancakes.push_back(llll(r, r * h));
		}

		sort(pancakes.begin(), pancakes.end());
		double max_area = 0.0;
		for (int i = n - 1; i >= k - 1; i--) {
			//cout << "trying pancake " << i << endl;
			// assume this is the pancake with the largest radius
			ll max_r = pancakes[i].first;
			ll total_height = pancakes[i].second;

			//cout << max_r << ", " << total_height << endl;

			// of the remaining, take the (k - 1) largest sleeves
			vllll remaining = vllll(pancakes.begin(), pancakes.begin() + i);
			sort(remaining.begin(), remaining.end(), [](llll &left, llll &right) {return left.second > right.second; });
			//cout << "sorted remaining" << endl;
			for (auto p : remaining) {
				//cout << p.first << " " << p.second << endl;
			}
			for (int j = 0; j < k - 1; j++) {
				total_height += remaining[j].second;
				//cout << "added height of " << j << " to obtain " << total_height << endl;
			}

			double sa = pi * max_r * max_r + 2 * pi * total_height;
			//cout << "found area of " << sa << endl;
			if (sa > max_area) {
				//cout << "max area found with " << max_r << " " << total_height << endl << endl;
				max_area = sa;
			}
		}
		
		cout << fixed << setprecision(10) << max_area << endl;
	}
	return 0;
}