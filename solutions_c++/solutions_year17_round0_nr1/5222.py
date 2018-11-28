#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
string solve(string S, int k);

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }


int main() {
	int T, K;
	string S, res; 

	cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
	//cout << "T:" << T <<"\n";
	for (int i = 1; i <= T; ++i) {
		cin >> S >> K;  // read n and then m.
		res = solve(S, K);
		cout << "Case #" << i << ": " << res << endl;
		//cout << "S: " << S << " " << "K:" << K << "\n";
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
	return 0;
}

string solve(string S, int k) {
	int len, i, j, count;
	int flag = 0;
	len = S.length();
	string res;

	count = 0;
	for (i = 0; i <= len - k;){
		if (i == len - k) {
			for (j = 0; j < k-1; j++) {
				if (S[i+j] != S[i+j+1]) {
					res = "IMPOSSIBLE";
					flag = 1;
					break;
				}
			}
			if (flag == 0) {
				if (S[i+j] == '-')
					count ++;
				res = NumberToString(count);
			}
			
		} else {
			if (S[i] == '-') {
				count++;
				for (j = 0; j < k; j++) {
					// flip it!
					if(S[i+j] == '-')
						S[i+j] = '+';
					else
						S[i+j] = '-';
				}
			}
		}

		i++;
	}

	return res;
}

