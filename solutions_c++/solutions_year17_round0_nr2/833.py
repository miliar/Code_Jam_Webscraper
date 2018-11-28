#include <iostream>
#include <string>

int main(int argc, char** argv) {
	int T;
	std::cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		std::cout << "Case #" << tc << ": ";
		std::string N;
		std::cin >> N;
		int Nl = (int)N.length();

		for (int i = Nl - 2; i >= 0; i--) {
			if (N[i] > N[i + 1]) {
				N[i]--;
				for (int j = i + 1; j < Nl; j++) {
					N[j] = '9';
				}
			}
		}

		bool leading = true;
		for (int i = 0; i < Nl; i++) {
			if (N[i] == '0' && leading) {
				continue;
			}
			leading = false;
			std::cout << N[i];
		}
		std::cout << '\n';
	}

	return 0;
}