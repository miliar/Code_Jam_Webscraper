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
	string result;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		result = "";
		string s;
		cin >> s;
		int d1, d2;
		bool tidy = false;
		if (s.length() == 1)
			result = s;
		else {
			while (!tidy) {
				size_t j;
				for (j = 1; j < s.length(); ++j) {
					d1 = int(s.at(j - 1));
					d2 = int(s.at(j));
					if (d1 > d2) {
						tidy = false;
						if (s.at(j - 1) == '1') {
							s.at(j - 1) = '0';
							//s.at(j) = '9';
						}
						else {
							s.at(j - 1) = s.at(j - 1) - 1;
							//s.at(j) = '9';
						}
						for (size_t k = j; k < s.length(); ++k) {
							s.at(k) = '9';
						}
						break;
					} 
				}
				if (j == s.length())
					tidy = true;
			}
			
			if (s.at(0) == '0')
				s = s.substr(1,string::npos);
			result = s;
		}
		
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}