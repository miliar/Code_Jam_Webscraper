#include <iostream>
#include <string>

int main()
{
	int T;
	std::cin >> T;

	for (int i = 0; i < T; ++i) {
		std::string N;
		std::cin >> N;

		std::cerr << "N = " << N << '\n';

		bool ok = false;
		while (!ok) {
			ok = true;

			for (int j = 0; j < N.size() - 1; ++j) {
				if (N[j] > N[j + 1]) {
					std::cerr << "N[" << j << "] = " << N[j] << " < " <<
						"N[" << j + 1 << "] = " << N[j + 1] << '\n';

					ok = false;

					N[j] = N[j] - 1;
					for (int k = j + 1; k < N.size(); ++k)
						N[k] = '9';

					if (j == 0 && N[j] == '0')
						N.erase(N.begin());

					std::cerr << "N =  " << N << '\n';
					break;
				}
			}
		}

		std::cout << "Case #" << i + 1 << ": " << N << '\n';
	}

	return 0;
}
