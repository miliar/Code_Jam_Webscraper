#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
ifstream finS("small_input.txt");
ifstream finL("large_input.txt");
ofstream foutS("small_output.txt");
ofstream foutL("large_output.txt");

int digit(const char& c) {
	return c - '0';
}

int getLongestSubseq(string seq) {
	for (int i = 1; i < (int)seq.size(); ++i) {
		if (digit(seq[i]) < digit(seq[i - 1])) {
			return i - 1;
		}
	}
	return seq.size() - 1;
}

string solve(string seq) {
	stringstream ss;
	int n = seq.size();
	int leftIt = 0;
	int rightIt = getLongestSubseq(seq);
	while (rightIt != seq.size() - 1) {
		seq = seq.substr(0, rightIt + 1);
		int li = seq.size() - 1;
		--seq[li];
		rightIt = getLongestSubseq(seq);
	}
	int it = 0;
	while (seq[it] == '0') ++it;
	for (it; it < (int)seq.size(); ++it){
		ss << seq[it];
	}
	for (int i = seq.size(); i < n; ++i) {
		ss << "9";
	}
	return ss.str();
}

int t, ans, k;
string str;
int main() {
	finS >> t;
	for (int i = 1; i <= t; ++i) {
		finS >> str;
		string ans = solve(str);
		foutS << "Case #" << i << ": " << ans << "\n";
	}
	finL >> t;
	for (int i = 1; i <= t; ++i) {
		finL >> str;
		string ans = solve(str);
		foutL << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}