#include <iostream>
#include <string>
#include <vector>

//#define DEBUG 1

using namespace std;

template <class Type>
void output(const vector<Type>& v) {
	cout << "Print: ";
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

string solve(const string& pancakes, int k) {
	vector<bool> v;
	for(auto ch : pancakes) {
		v.push_back(ch == '+');
	}
	int count = 0;
	for(int i = 0; i < v.size(); i++) {
		#ifdef DEBUG
		output(v);
		#endif
		
		if(!v[i] && i + k - 1 < v.size()) {
			for(int j = i; j < i + k; j++) {
				v[j] = !v[j];
			}
			++count;
		}
		
		if(!v[i]) {
			return "IMPOSSIBLE";
		}
	}
	return to_string(count);
}

int main() {
	int T;
	cin >> T;
	for(int cas=1; cas <=T; cas++) {
		string pancakes;
		int k;
		cin >> pancakes >> k;
		cout << "Case #" << cas << ": " << solve(pancakes, k) << endl;
	}
	return 0;
}
