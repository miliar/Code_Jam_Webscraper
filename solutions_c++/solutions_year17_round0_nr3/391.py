#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#include <string>
#include <vector>
#include <sstream>
#include <map>

void calc(long long length, long long &r1, long long &r2);

void add_to_m(long long a1, long long n, map<long long, long long> &map);

string solve(const string & s) {

	std::stringstream ss(s);
	long long k,n;
	ss >> n >> k;

	map <long long, long long> m;
	m[n]=1;

	long long i = k;

	long long r1 = -1;
	long long r2 = -1;

	while(!m.empty()) {
		if (i == 0) {
			break;
		}
		auto it = *m.rbegin();

		if (it.second >= i) {
			calc(it.first, r1, r2);
			break;
		}

		i -= it.second;
		long long a1 = it.first/2;
		long long a2 = (it.first-1)/2;
		add_to_m(a1, it.second, m);
		add_to_m(a2, it.second, m);
		m.erase(it.first);
	}

	std::stringstream sr;
	sr << r1 << " " << r2;

	return sr.str();
}

void add_to_m(long long a, long long n, map<long long, long long> &map) {
	if (a == 0)
		return;
	if (map.find(a) == map.end()) {
		map[a] = n;
	} else {
		map[a] += n;
	}
}

void calc(long long length, long long &r1, long long &r2) {
	r1 = length/2;
	r2 = (length-1)/2;
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