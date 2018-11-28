#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>      // std::setprecision

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define endl '\n'

using dvojice = pair<long long int, long long int>;




int main() {
	std::ios::sync_with_stdio(false);


	int t,n;
	double d, k, m;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> d >> n;
		double time = 0;

		for (int j = 1; j <= n; j++)
		{
			cin >> k >> m;
			double akttime = (d - k) / m;
			if (time < akttime)
				time = akttime;

		}

		cout << "Case #" << setprecision(7) << fixed << i << ": " << d/time << endl;
	}

}