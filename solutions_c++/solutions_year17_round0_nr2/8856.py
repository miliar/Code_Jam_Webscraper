#include <iostream>
#include <stdio.h>

bool isTidy(uint64_t value) {
	if (value < 10)
		return true;

	uint32_t digitR = value % 10;
	uint32_t digitRL = (value / 10) % 10;

	if (digitRL > digitR)
		return false;

	return isTidy(value / 10);
}

int main() {
	size_t count;

	std::cin >> count;

	for (size_t i = 0; i < count; ++i) {
		uint64_t value;

		std::cin >> value;

		while (!isTidy(value))
			value--;

		std::cout << "Case #" << (i + 1) << ": " << value << std::endl;
	}

	return 0;
}
