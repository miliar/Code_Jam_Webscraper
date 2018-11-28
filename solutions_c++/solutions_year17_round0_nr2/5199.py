#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
#include <stdint.h>
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
uint64_t solve(uint64_t N);
vector<int> decomposeInt(uint64_t N);

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }


int main() {
	int T;
	uint64_t N;
	uint64_t res; 

	cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
	//cout << "T:" << T <<"\n";
	for (int i = 1; i <= T; ++i) {
		cin >> N;  // read n and then m.
		decomposeInt(N);
		res = solve(N);
		cout << "Case #" << i << ": " << res << endl;
		//cout << "S: " << S << " " << "K:" << K << "\n";
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
	return 0;
}

uint64_t solve(uint64_t N) {
	vector<int> carr;
	int len, i, j;
	uint64_t res;
	carr = decomposeInt(N);
	len = carr.size();

	for(i = 0; i < len - 1;) {
		if (carr[i] < carr[i+1]) {
			for (j = 0; j < i+1; j++) {
				carr[j] = 9;
			}
			carr[i+1] = carr[i+1] - 1;
		}
		i++;
	}

	res = 0;
	for (vector<int>::reverse_iterator rit = carr.rbegin(), rie = carr.rend();
						rit != rie; ++rit) {
		res = res * 10 + (*rit);
	}

	return res;
}

vector<int> decomposeInt(uint64_t N) {
	uint64_t t;
	char c;
	vector<int> carr;

	t = N;
	while (t > 0) {
		c = (t%10);
		t = t/10;
		carr.push_back(c);
	}

	//cout << "carr:" ;
	//for (vector<int>::iterator it = carr.begin(), ie = carr.end();
	//					it != ie; ++it) {
	//	cout << *it << ",";
	//}
	//cout << "\n";

	return carr;
}

