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
#include <cfloat>
using namespace std;

const size_t MAX = 1000000 + 1;

uint64_t gcd(uint64_t a, uint64_t b)
{
	return b ? gcd(b, a%b) : a;
}

void solve(string &n)
{
	for (size_t i = 0; i < n.length() - 1; ++i)
		if (n[i] > n[i + 1])
		{
			size_t j = i;
			while (j > 0 && n[j - 1] == n[i]) --j;
			n[j] -= 1;
			for (++j; j < n.length(); ++j)
				n[j] = '9';
			break;
		}
}

int main(int argc, char *argv[])
{
	ios_base::sync_with_stdio(false);
	ifstream in("input.txt");
	ofstream out("output.txt");
	int32_t t;
	string n, temp;
	cin >> t;
	for (int32_t i = 1; i <= t; ++i)
	{
		cin >> n;
		solve(n);
		while (n[0] == '0') n = n.erase(0, 1);
		cout << "Case #" << i << ": " << n << endl;
	}
	// system("pause");
	return 0;
}