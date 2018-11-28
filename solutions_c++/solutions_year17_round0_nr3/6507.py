#include <iostream>
#include <stdint.h>
#include <cstring>
#include <vector>

void print_stalls(std::vector<bool>& stalls) {
	for (size_t i = 0; i < stalls.size(); i++) {
		std::cout << (stalls[i] ? "O" : ".");
	}
	std::cout << std::endl;
}

int main() {
	int num_cases;
	std::cin >> num_cases;

	uint64_t num_stalls;
	uint64_t num_people;

	for (int case_num = 0; case_num < num_cases; case_num++) {
		std::cin >> num_stalls;
		std::cin >> num_people;

		std::vector<bool>& bits = *(new std::vector<bool>(num_stalls + 2, false));
		bits[0] = true;
		bits[num_stalls + 1] = true;

		// print_stalls(bits);

		for (uint64_t person_index = 0; person_index < num_people; person_index++) {
			size_t first_iteration = true;
			size_t best_stall_i;
			size_t best_min;
			size_t best_max;

			for (size_t i = 1; i < (num_stalls + 2); i++) {
				if (bits[i]) { continue; }

				size_t ls;
				for (size_t j = i; j > 0; j--) {
					if (bits[j - 1]) {
						ls = i - j;
						break;
					}
				}

				size_t rs;
				for (size_t j = (i + 1); j < (num_stalls + 2); j++) {
					if (bits[j]) {
						rs = j - (i + 1);
						break;
					}
				}

				size_t min = (ls < rs) ? ls : rs;
				size_t max = (ls > rs) ? ls : rs;

				if (first_iteration) {
					best_stall_i = i;
					best_min = min;
					best_max = max;
					first_iteration = false;
				} else {
					if (min > best_min) {
						best_stall_i = i;
						best_min = min;
						best_max = max;
					} else if (min == best_min) {
						if (max > best_max) {
							best_stall_i = i;
							best_min = min;
							best_max = max;
						} else if (max == best_max) {
							if (i < best_stall_i) {
								best_stall_i = i;
								best_min = min;
								best_max = max;
							}
						}
					}
				}
			}

			bits[best_stall_i] = true;
			// print_stalls(bits);

			if (person_index == (num_people - 1)) {
				std::cout << "Case #" << (case_num + 1) << ": " << best_max << " " << best_min << std::endl;
			}
		}

		delete &bits;
	}

	return 0;
}
