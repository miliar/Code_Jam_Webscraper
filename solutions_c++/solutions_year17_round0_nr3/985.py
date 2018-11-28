
#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <algorithm>
#include <map>
using namespace std;

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		long long N, K;
		cin >> N >> K;
		map<long long, long long> elems;
		elems[N] = 1;
		while (elems.rbegin()->second < K)
		{
			elems[elems.rbegin()->first / 2] += elems.rbegin()->second;
			elems[(elems.rbegin()->first-1) / 2] += elems.rbegin()->second;
			K -= elems.rbegin()->second;;
			elems.erase(--elems.end());
		}
		cout << "Case #" << i + 1 << ": " << elems.rbegin()->first / 2 << " " << (elems.rbegin()->first - 1) / 2 << endl;
		
	}
	return 0;
}