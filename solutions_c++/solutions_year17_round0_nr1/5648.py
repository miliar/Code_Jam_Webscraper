#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int ii = 0; ii < t; ++ii) {
		string s;
		int wi;
		cin >> s >> wi;
		int f = 0, pos = 0;
		bool imp = false;
		while (pos < s.length()) {
			if (s[pos] == '+') {
				++pos;
				continue;
			}
			++f;
			for (int i = 0; i < wi; ++i) {
				if (pos + i >= s.length()) {
					imp = true;
					break;
				}
				if (s[pos+i] == '-') s[pos+i] = '+';
				else if (s[pos+i] == '+') s[pos+i] = '-';			
			}
			if (imp) {
				break;
			}
			++pos;
		}
		cout << "CASE #" << ii+1 << ": ";
		if (imp) cout << "IMPOSSIBLE\n";
		else cout << f << endl;
		
	}
	
	return 0;
}