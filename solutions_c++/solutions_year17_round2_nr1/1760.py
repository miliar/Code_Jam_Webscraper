#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <iomanip>

using namespace std;

typedef long long int ll;

const int MAXSIZE = 100*1000;
const int INF = 2000*1000*1000;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie();

	int T;
	cin >> T;
	for(int t=1; t<=T; ++t) {
		int d, n;
		cin >> d >> n;
		int pos, s;
		double tm = -1;
		for (int i=0; i<n; ++i) {
			cin >> pos >> s;
			double tmp = (d - pos + .0) / s;
			if (tmp > tm) tm = tmp;
		}
	
		cout << fixed;
		cout << "Case #" << t << ": " << setprecision(9) << d / tm << endl;
	}

	return 0;
}