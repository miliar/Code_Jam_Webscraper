#include <iostream>
#include <cstdlib>
#include <sstream>

using namespace std;

void isTidy (long long int a) {

	bool f = true;

	stringstream ss;
	ss << a;

	string aux = ss.str();

	if (aux.size() == 1) {
		cout << aux << '\n';
		return;
	}

	while (f) {
		f = false;
		for (int i = 0; i < (int)aux.size() - 1; ++i) {
			if (aux[i] > aux[i + 1]) {
				f = true;
				if (aux[i] != '9') {
					aux[i]--;
				}

				aux[i + 1] = '9';

				if (atoi(aux.c_str()) > a)
					aux[i]--;
			}
		}
	}

	for (int i = ((aux[0] == '0') ? 1 : 0); i < (int)aux.size(); ++i) {
		cout << aux[i];
	}

	cout << '\n';
}

int main(int argc, char const *argv[]) {

	int T;
	int c = 0;
	long long int a;

	cin >> T;

	while (T--) {

		cin >> a;

		cout << "Case #" << ++c << ": ";

		isTidy(a);

	}

	return 0;
}