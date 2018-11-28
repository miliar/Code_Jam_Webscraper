#include <iostream>
#include <cassert>
#include <map>

int main()
{
	size_t T, N, K, Y, Z;

	std::cin >> T;
	assert(T <= 100);

	for (size_t i = 0; i < T; ++i) {
		std::cin >> N >> K;
		assert(1 <= K);
		assert(K <= N);
		
		std::map<size_t, size_t, std::greater<size_t>> table;
		table[N] = 1;
		while(K--) {
			auto next = table.begin();
			size_t size = (next->first)-1;
			size_t & amount = (next->second);

			Y = size / 2;
			Z = size - Y;
			
			if (1 < amount) {
				--amount;
			} else {
				table.erase(next);
			}
			++table[Y];
			++table[Z];
		}
		std::cout << "Case #" << i+1 << ": " << Z << " " << Y << std::endl;
	}
	return 0;
}

