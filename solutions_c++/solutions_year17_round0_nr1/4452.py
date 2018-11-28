#include <iostream>
#include <vector>
#include <string>
#include <istream>

int main() {
	int n;
	std::cin >> n;
	for (int i = 0; i < n; ++i) {
		std::string ponchiki;
		int amount;

		std::cin >> ponchiki;
		std::cin >> amount;

		std::vector<bool> flip_amounts(ponchiki.length(), false);
		int answer = 0;

		for (int j = ponchiki.length() - 1; j >= amount-1; --j) {

			if ((flip_amounts[j] + (ponchiki[j] == '-' ? -1 : 0)) != 0) {
				answer++;
				for (int k = j; k > j-amount; --k) {
					flip_amounts[k] = !flip_amounts[k];
				}
			}

			// for (int l = 0; l < flip_amounts.size(); ++l) {
			// 	std::cout << int(flip_amounts[l]);
			// }
			// std::cout << '\n';
		}

		bool is_ok = true;
		for (int j = amount-1; j >= 0; --j) {
			if ((flip_amounts[j] + (ponchiki[j] == '-' ? -1 : 0)) != 0) {
				is_ok = false;
				break;
			}
		}

		if (!is_ok) std::cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
		else std::cout << "Case #" << i+1 << ": " << answer << '\n';
	}
	return 0;
}