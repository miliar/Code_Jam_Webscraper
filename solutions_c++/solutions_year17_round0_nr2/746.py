// g++ -I tr1 femidav.cpp -O2 -Wall -std=c++0x -o femidav.exe
// ./femidav < small-attempt0.in > small-attempt0.out
// ./femidav < large.in > large.out

#include <cstdio>
#include <cstdint>
#include <cinttypes>
#include <iostream>
#include <string>

uint64_t rulln() { uint64_t r; scanf("%" PRIu64 "\n", &r); return r; }
int rin() { int r; scanf( "%d\n", &r ); return r; }

std::string solve(uint64_t N)
{
	std::string n = "";
	for(uint64_t M = N; M > 0; M /= 10)
		n += '0' + M % 10;

	std::string r(n.rbegin(), n.rend());
	int e = r.length();

	if (e > 1)
	{
		for(int i = e - 2, j = e - 1; j > 0; --i, --j)
		{
			if (r[i] > r[j]) {
				r[i] -= 1;
				for(int k = j; k < e; ++k)
					r[k] = '9';
			}
		}

		r.erase(0, r.find_first_not_of("0"));
	}

	return r;
}

int main()
{
	for(int x = 1, end_ = rin() + 1; x < end_; ++x)
		printf("Case #%d: %s\n", x, solve(rulln()).c_str());
}