#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve(uint64_t n, uint64_t k)
{
	++ n;
	vector<int> bits;
	while (k > 1)
	{
		bits.push_back(k&1);
		k >>= 1;
	}
	for (int i = 0; i < bits.size(); ++ i)
	{
		if (bits[i]) 
			n = n >> 1;
		else 
			n = n + 1 >> 1;
	}
	uint64_t a, b;
	a = n >> 1;
	b = n + 1 >> 1;
	cout << b - 1 << " " << a - 1 << "\n";
}


int main()
{
	int tc;
	cin >> tc;
	for (int i = 1; i <= tc; ++ i)
	{
		uint64_t n, k;
		cin >> n >> k;
		cout << "Case #" << i << ": ";
		solve(n, k);
	}
}

