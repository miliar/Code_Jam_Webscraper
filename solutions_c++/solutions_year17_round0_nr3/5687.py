#include <iostream>
#include <vector>

int main()
{
	int T;
	std::cin >> T;

	int chosenBlock = -1;
	int cbClosest = 0, cbFarthest = 0;

	for (int i = 0; i < T; ++i) {
		int N, K;
		std::cin >> N >> K;

		std::vector<int> freeBlocks = { N };
		/* freeBlocks.reserve(N); */

		for (int j = 0; j < K; ++j) {
			chosenBlock = -1;
			cbClosest = cbFarthest = 0;

			for (unsigned int block = 0; block < freeBlocks.size(); ++block) {
				int blockSize = freeBlocks[block];
				int c = blockSize - (blockSize / 2) - 1;
				int f = blockSize / 2;

				std::cerr << f << ", " << c;

				if (c > cbClosest || (c == cbClosest && f > cbFarthest) ||
						chosenBlock == -1) {
					chosenBlock = block;
					cbClosest = c;
					cbFarthest = f;
					std::cerr << " : chosen\n";
				}

				std::cerr << '\n';
			}

			freeBlocks[chosenBlock] = cbFarthest;
			freeBlocks.insert(freeBlocks.begin() + chosenBlock, cbClosest);

			std::cerr << "###\n";
		}

		std::cout << "Case #" << i + 1 << ": " <<
			cbFarthest << ' ' << cbClosest << '\n';
	}

	return 0;
}
