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
		ll n;
		cin >> n;
		vector<ll> v;
		while (n > 0)
		{
			v.push_back(n % 10);
			n /= 10;
		}
		for (int i = 0; i < v.size() - 1; i++)
		{
			if (v[i] < v[i + 1])
			{
				for (int j = i; j >= 0; j--)
				{
					v[j] = 9;
				}
				v[i + 1]--;
			}
		}
		while (v.back() == 0)
		{
			v.pop_back();
		}
		cout << "Case #" << test << ": ";
		for (int i = v.size() - 1; i >= 0; i--)
		{
			cout << v[i];
		}
		cout << endl;
	}
    return 0;
}

