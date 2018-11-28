#include <iostream>
#include <map>

int main()
{
	int caseCount;

	std::cin >> caseCount;

	for (int i = 1; i <= caseCount; i++) {
		long long stallCount;
		long long personCount;

		std::cin >> stallCount >> personCount;

		if (stallCount == personCount ||
			(stallCount == personCount + 1 && personCount != 1)) {
			std::cout << "Case #" << i << ": 0 0" << std::endl;
			continue;
		}

		std::map<long long, long long> stallMap;

		stallMap[stallCount] = 1;

		long long minSpace;
		long long maxSpace;

		for (int j = 1; j <= personCount; j++) {
			int len = stallMap.rbegin()->first;
			int count = stallMap[len];

			if (count == 1) {
				stallMap.erase(len);
			} else {
				stallMap[len]--;
			}

			long long halfLen = len / 2;

			minSpace = halfLen;
			maxSpace = halfLen;

			if (len % 2 == 0) {
				stallMap[halfLen - 1]++;
				stallMap[halfLen]++;
				minSpace--;
			} else {
				stallMap[halfLen] += 2;
			}
		}

		std::cout << "Case #" << i << ": "
				  << maxSpace << " " << minSpace << std::endl;
	}

	return 0;
}
