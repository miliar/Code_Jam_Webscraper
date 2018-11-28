#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
#include <stdint.h>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <stdio.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }



int main() {
	int i, j, T;
	uint64_t D, N, K, S;
	double tp, tc, t;

	cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
	//cout << "T:" << T <<"\n";
	cout << std::fixed;
    	cout << std::setprecision(6);
	for (i = 1; i <= T; ++i) {
		cin >> D >> N;  // read n and then m.
		tp = 0.0;
		for (j = 1; j <= N; j++) {
			cin >> K >> S;  // read n and then m.
			tc = (D - K)*1.0/(S*1.0);
			if (tc < tp)
				tc = tp;
			tp = tc;
		}

		t = D*1.0/tc;

		cout << "Case #" << i << ": " << t << endl;
		//printf("Case #%d: %.6f\n", i, t);
	}
	return 0;
}
