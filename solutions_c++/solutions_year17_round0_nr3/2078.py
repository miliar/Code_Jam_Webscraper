#include <iostream>
#include <cmath>
#include <cstdint>
using namespace std;

uint64_t parity[100];

int find_parity(uint64_t k1, int z1)
{
	while(k1 > 0)
	{
		parity[z1++] = k1 % 2;
		k1 /= 2;
	}
	return z1;
}

int main() {
	int t, z;
	uint64_t n, k, ls, rs, max, min;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> n >> k;
		z = find_parity(k, 0);
		for(uint64_t j = 0; j < z; j++)
		{
			ls = ( n - 1 ) / 2;
			rs = n / 2;
			if(parity[j] == 0)
				n = rs;
			else
				n = ls;
		}
		max = rs > ls ? rs : ls;
		min = rs < ls ? rs : ls;
		cout << "Case #" << i + 1 << ": " << max << " " << min << "\n";
	}
	return 0;
}
