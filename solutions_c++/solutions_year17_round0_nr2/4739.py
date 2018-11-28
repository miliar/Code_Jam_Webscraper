#include <iostream>
#include <string>

using namespace std;

void reduceBackwards(string& n, int from) {

	if (n[from] != '0') {
		n[from] -= 1;
		return;
	} else {
		if (from == 0)
			return;
		n[from] = '9';
		reduceBackwards(n, from - 1);
	}
}

void reduceNumber(string& n, int from) {

	for (int i = from + 1; i < n.size(); ++i) {
		n[i] = '9';
	}

	reduceBackwards(n, from);
}

bool transformToLastTidyNumber(string& n) {

	if (n.size() == 1)
		return true;

	for (int i = 0; i < n.size() - 1; ++i) {

		if (n[i] > n[i + 1]) {
			reduceNumber(n, i);
			return false;
		}
	}

	return true;

}

int main(int argc, char* argv[]) {

	int testCases = 0;
	cin >> testCases;

	string n;
	for (int i = 0; i < testCases; i++) {

		cin >> n;

		bool finish = transformToLastTidyNumber(n);
		while (!finish) finish = transformToLastTidyNumber(n);

		cout << "Case #" << i + 1 << ": " << n.erase(0, min(n.find_first_not_of('0'), n.size()-1)) << endl;

	}
}