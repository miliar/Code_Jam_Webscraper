#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int it=1;it<=T;++it) {
		int d, n;
		cin >> d >> n;
		double maxtime = 0;
		while (n--){
 			int k, s;
			cin >> k >> s;
			double newtime = (double) (d-k)/s;
			maxtime = maxtime>newtime?maxtime:newtime;
		}
		cout << "Case #" << it << ": " << setprecision(20) << d/maxtime << endl;
	}
}