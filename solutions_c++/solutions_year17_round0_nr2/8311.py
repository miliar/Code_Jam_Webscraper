#include <iostream>
#include <sstream>
#include <string>

using namespace std;

string diminish(string &s, int pos) {
	if (s[pos] == '0' && pos - 1 >= 0) {
		s[pos] = '9';
		return diminish(s, pos - 1);
	}

	if (s[pos] > '0') {
		if (pos - 1 >= 0 && s[pos - 1] > s[pos]-1)
			s[pos] = '9';
		else 
		{
			s[pos]--;
			return s;
		}
		return diminish(s, pos - 1);
	}

	return s;
}

int main(){
	int t;
	string n;
	cin >> t;
	int count = 1;
	while (t--) {
		cin >> n;
		for (int i = 0; i < n.size() - 1; i++) {
			if (n[i] > n[i + 1]) {
				for (int j = i + 1; j < n.size(); j++)
					n[j] = '9';
				diminish(n, i);
			}
		}

		stringstream ss;
		bool cutZeros = true;
		for (int i = 0; i < n.size(); i++){
			if (cutZeros && n[i] == '0')
				continue;
			else{
				cutZeros = false;
				ss << n[i];
			}
		}

		cout << "Case #" << count << ": " << ss.str() <<endl;
		count++;
	}

	return 0;
}