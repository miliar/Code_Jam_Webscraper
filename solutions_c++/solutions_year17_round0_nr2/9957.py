#include<iostream>

using namespace std;

int T = 0;
int N = 0;

bool check_tidy() {

	int last_num = 10;
	int candi_tidy = N;
	while (candi_tidy) {

		int test = candi_tidy % 10;
		if (test <= last_num) {
			last_num = test;
			candi_tidy = candi_tidy / 10;
		}
		else {
			return false;
		}
	}

	return true;

}

int main() {

	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> N;

		while (1) {

			if (!check_tidy()) {
				N--;
			}
			else {
				cout << "Case #" << i << ": " << N << endl;
				break;
			}

		}
	}

}