#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Solution {
public:
	int solve(int n) {
		for (int j = n; j >= 1; --j) {

			if (j < 10) {
				return j;
			}

			vector<int> digits = helper(j);
			int m = digits.size();
			bool found = true;

			for (int i = 1; i < m; ++i) {
				if (digits[i] < digits[i - 1]) {
					found = false;
					break;
				}
			}

			if (found) {
				return j;
			}
		}

		return 1;
	}
private:
	vector<int> helper(int n) {

		vector<int> res;

		while (n) {
			res.push_back(n % 10);
			n /= 10;
		}

		return vector<int>(res.rbegin(), res.rend());
	}
};

int main() {

	Solution solution;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int m, n;

	fin >> m;

	for (int i = 0; i < m; ++i) {
		fin >> n;
		fout << "Case #" << i + 1 << ": " << solution.solve(n) << endl;
	}

	return 0;
}
