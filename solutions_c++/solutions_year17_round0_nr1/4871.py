#include <fstream>
#include <string>
#include <vector>
using namespace std;
ifstream finS("small_input.txt");
ifstream finL("large_input.txt");
ofstream foutS("small_output.txt");
ofstream foutL("large_output.txt");

int solve(string seq, int k, ifstream& in, ofstream& out) {
	int n = seq.size();
	int cnt = 0;
	char temp;
	vector<bool> flipped(n, false);

	for (int i = 0; i <= n - k; ++i) {
		if (flipped[i]) {
			temp = (seq[i] == '+') ? '-' : '+';
		}
		else {
			temp = seq[i];
		}
		if (temp!='+'){
			++cnt;
			for (int j = 0; j < k; ++j) {
				flipped[i+j] = !flipped[i+j];
			}
		}
	}
	for (int i = n - k + 1; i < n; ++i) {
		if (flipped[i]) {
			temp = (seq[i] == '+') ? '-' : '+';
		}
		else {
			temp = seq[i];
		}
		if (temp != '+') {
			return -1;
		}
	}
	return cnt;
}

int t, ans, k;
string str;
int main() {
	finL >> t;
	for (int i = 1; i <= t; ++i) {
		finL >> str >> k;
		ans = solve(str, k, finL, foutL);
		foutL << "Case #" << i << ": ";
		if (ans == -1) {
			foutL << "IMPOSSIBLE";
		}
		else {
			foutL << ans;
		}
		foutL << "\n";
	}
	return 0;
}