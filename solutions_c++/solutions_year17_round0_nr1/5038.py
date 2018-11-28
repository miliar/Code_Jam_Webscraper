#include <iostream>
#include <vector>
#include <iterator>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <map>
#include <unordered_map>

using namespace std;

int main()
{
	int t;
	int result;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		result = 0;
		string s;
		int k;
		size_t found;
		cin >> s;
		cin >> k;
		found = s.find('-');
		while (found != string::npos && found <= (s.length()-k) ) {
			for (int j = 0; j < k; ++j) {
				if (s.at(found+j) == '+')
					s.at(found+j) = '-';
				else
					s.at(found+j) = '+';
			}
			++result;
			found = s.find('-');
		}
		if (found == string::npos) {
			cout << "Case #" << i << ": " << result << endl;
		} else if (found > (s.length() - k)) {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
		
	}
	return 0;
}