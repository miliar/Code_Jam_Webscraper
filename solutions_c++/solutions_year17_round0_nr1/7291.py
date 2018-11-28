#include <iostream>
#include <string>

using namespace std;

inline void flipChar (string & str, int at) {
	str[at] = (str[at] == '+') ? '-' : '+';
}

inline bool goodLine (string const & str) {
	return (str.find('-') == string::npos);
}

int main () {
	int T;
	cin >> T;

	for (int rowNum =1; rowNum <= T; rowNum++) {
		string line;
		int flip, count = 0;
		cin >> line >> flip;

		for (int i=0, till=(line.size() - flip); i <= till; i++) {
			if (line[i] == '-') {
				// flip the next few
				for (int j=0; j<flip; j++)
					flipChar(line, i+j);

				count ++;
			}
		}

		cout << "Case #" << rowNum << ": ";
		if (goodLine(line)) 
			cout << count;
		else
			cout << "IMPOSSIBLE";

		cout << endl;
	}
}