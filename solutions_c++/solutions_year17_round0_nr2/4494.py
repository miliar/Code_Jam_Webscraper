#include <iostream>
#include <string>
using namespace std;

string tidyNum(string& N);

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		string N;
		cin >> N;
		cout << "Case #" << i << ": " << tidyNum(N) << endl;
	}
	return 0;
}

string tidyNum(string& N) {
	int i = 0;
	while (i < N.size()) {
		if (i == 0) {
			++i;
		} else {
			if (N[i] < N[i - 1]) {
				for (int k = i; k < N.size(); ++k) {
					N[k] = '9';
				}
				N[i - 1] = N[i - 1] - 1;
				--i;
			} else {
				++i;
			}
		}
	}
  while (N[0] == '0') {
    N = N.substr(1);
  }
	return N;
}