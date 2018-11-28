#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <numeric>
#include <limits>
#include <functional>
#include <set>
#include <map>
#include <fstream>

using namespace std;
typedef long long ll;
int const INF = numeric_limits<int>::max();



int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		ll n, k;
		cin >> n >> k;
		map<ll, ll> m;
		m[n] = 1;
		while (k > 0)
		{
			auto it = prev(m.end());
			if (it->second >= k)
			{
				cout << "Case #" << test << ": " << it->first / 2 << " " << (it->first - 1) / 2 << endl;
				break;
			}
			k -= it->second;
			m[it->first / 2] += it->second;
			m[(it->first - 1) / 2] += it->second;
			m.erase(it);
		}
	}
    return 0;
}

