// g++ -I tr1 femidav.cpp -O2 -Wall -std=c++0x -o femidav.exe
// ./femidav < small-attempt0.in > small-attempt0.out
// ./femidav < large.in > large.out

#include <cstdio>
#include <cstdint>
#include <cinttypes>
#include <iostream>
#include <map>

uint64_t rull() { uint64_t r; scanf("%" PRIu64, &r); return r; }
uint64_t rulln() { uint64_t r; scanf("%" PRIu64 "\n", &r); return r; }
int rin() { int r; scanf( "%d\n", &r ); return r; }

uint64_t solve(uint64_t N, uint64_t K)
{
	//std::cerr << "Solve for: " << N << ", " << K << std::endl;
	std::map<uint64_t, uint64_t> f = {{N, 1}};

	while(K > 0) {
		uint64_t number = f.rbegin()->second, length = f.rbegin()->first, l1 = length/2, l2 = (length - 1)/2;
		//std::cerr << "Found '" << number << "' ranges with length '" << length << "', l1: " << l1 << ", l2: " << l2 << std::endl;

		if (number >= K)
			return length;
		else {
			K -= number;
			f.erase(length);

			f.emplace(std::make_pair(l1, 0));
			f.emplace(std::make_pair(l2, 0));

			f[l1] += number;
			f[l2] += number;
		}
	}
	return 0;
}

int main()
{
	for(int x = 1, end_ = rin() + 1; x < end_; ++x)
	{
		uint64_t N = rull(), K = rulln(), answer = solve(N, K);
		printf("Case #%d: %" PRIu64 " %" PRIu64 "\n", x, answer/2, (answer - 1)/2);
	}
}