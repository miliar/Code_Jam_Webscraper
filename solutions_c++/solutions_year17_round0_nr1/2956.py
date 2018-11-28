#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool is_good(const string& s, const vector<int>& adds, int cur_sum, int i) {
	if (s[i] == '+') {
		return (cur_sum + adds[i]) % 2 == 0;
	} else {
		return (cur_sum + adds[i]) % 2 != 0;
	}
}

bool try_flip(string& s, vector<int>& adds, int k, int& start, int& cur_sum, int& count) {
	for (start < s.length(); is_good(s, adds, cur_sum, start); ++start) {
		cur_sum += adds[start];
	}
	if (start < s.length() && s.length() - start >= k) { // '-' and flip is possible
		++adds[start];
		--adds[start + k];
		cur_sum += adds[start];
		++start;
		++count;
		return true;
	} else {
		return false;
	}
}

int main() {
	int t, k;
	string s;
	
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> s >> k;
		vector<int> adds(s.length() + 1, 0);
		int start = 0;
		int cur_sum = 0;
		int count = 0;
		
		while (try_flip(s, adds, k, start, cur_sum, count));
		if (start < s.length() && s.length() - start < k) {
			cout << "Case #" << i + 1 << ": IMPOSSIBLE\n";
		} else {
			cout << "Case #" << i + 1 << ": " << count << "\n";
		}
	} 
	return 0;
}