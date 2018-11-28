#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#include <string>
#include <vector>
#include <sstream>

string solve(const string & s) {
	vector <char> v;

	string r;
	for(int i = 0; i < s.size(); ++i) {
		if ((s[i] == '-') || (s[i] == '+')) {
			v.push_back(s[i]);
			continue;
		}
		r = s.substr(i+1);
		break;
	}

	std::stringstream ss(r);
	int x;
	ss >> x;

	int c = 0;
	for(int i = 0; i < v.size()-x+1; ++i) {
		if (v[i]=='-') {
			for(int j = 0; j < x; ++j) {
				if (v[i+j]=='-')
					v[i+j]='+';
				else
					v[i+j]='-';
			}
			++c;
		}
	}

	for(int i = 0; i < v.size(); ++i) {
		if (v[i] == '-')
			return "IMPOSSIBLE";
	}

	std::stringstream sr;
	sr << c;

	return sr.str();
}

int main() {
	int n;
	cin >> n;
	string x;
	getline(cin, x);
	for (int i = 1; i <= n; ++i) {
		getline(cin, x);
		cout << "Case #" << i << ": " << solve(x) << endl;
	}
	return 0;
}