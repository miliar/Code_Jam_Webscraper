#include <fstream>
#ifdef ONLINE_JUDGE
#define cin in
#define cout out
#endif
#include <algorithm>
#include <iostream>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <set>
#include <string>
#include <map>
#define M_PI 3.14159265358979323846
#include <cmath>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <bitset>
#include <cfloat>
using namespace std;

const size_t MAX = 1000 + 1;

uint64_t gcd(uint64_t a, uint64_t b)
{
	return b ? gcd(b, a%b) : a;
}

int64_t solve(bitset<MAX> &cakes, int64_t n, int64_t k)
{
	int64_t flips = 0;
	for (size_t i = 0; i <= n - k; ++i)
	{
		if (cakes[i])
		{
			++flips;
			for (size_t j = i; j < i + k; ++j)
				cakes.flip(j);
		}
	}
	if (cakes.any()) return -1;
	else return flips;
}

int main(int argc, char *argv[])
{
	ios_base::sync_with_stdio(false);
	ifstream in("input.txt");
	ofstream out("output.txt");
	string input;
	int32_t t, k;
	cin >> t;
	for (int32_t i = 1; i <= t; ++i)
	{
		cin >> input >> k;
		bitset<MAX> cakes;
		for (int32_t l = 0; l < input.length(); ++l)
			if (input[l] == '-') cakes.set(l);
		int64_t ans = solve(cakes, input.length(), k);
		cout << "Case #" << i << ": "
			<< (ans == -1 ? "IMPOSSIBLE" : to_string(ans)) << endl;
	}
	return 0;
}