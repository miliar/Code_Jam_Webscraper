

#define _CRT_SECURE_NO_WARNINGS
#include <iostream> 
#include <vector>
#include <algorithm>
#include <map> 
#include <string>
#include <set> 
#include <iterator> 
#include <deque>
#include <iomanip>
#include <string> 
#include <math.h> 
#include <time.h>
#include <queue> 
#include <stdio.h>
#include <valarray>
#include <stack>
#include <stdio.h>
#include <cstdlib>
#include <cstring>


#define mp(x, y) make_pair(x, y)
#define all(x) x.begin(), x.end() 
#define det(a, b, c, d) a*d - b*c

typedef long long ll;

using namespace std;

const long double PI = 2*asin(1);

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int x;
	cin >> x;
	for (int t=1; t<=x; t++){
		int n, k;
		cin >> n >> k;
		vector<pair<double, double> > pancakes(n);
		for (int i = 0; i < n; i++) {
			cin >> pancakes[i].first >> pancakes[i].second;
		}
		sort(all(pancakes));
		reverse(all(pancakes));
		double ans = 0;
		for (int i = 0; i < (1 << n); i++) {
			int ones = 0;
			for (int digit = 0; digit < n; digit++) {
				if ((i&(1 << digit))) {
					ones++;
				}
			}
			if (ones == k) {
				double tmp = 0;
				for (int digit = 0; digit < n; digit++) {
					if ((i&(1 << digit))) {
						if (tmp > 0) {
							tmp -= PI*(pancakes[digit].first*pancakes[digit].first);
						}
						tmp += PI*(pancakes[digit].first*pancakes[digit].first + 2 * pancakes[digit].first*pancakes[digit].second);
						
					}
				}
				ans = max(ans, tmp);
			}
		}
		cout << fixed << setprecision(7) << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
