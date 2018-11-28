#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

using ll = long long int;
ifstream fin("3.in");
ofstream fout("3.out");

bool iterate(map<ll, ll>& m, ll& k) {
	ll len = prev(m.end())->first - 1;
	ll count = prev(m.end())->second;
	m.erase(prev(m.end()));

	ll high, low;
	if (len % 2 == 0)
		high = low = len/2;
	else {
		high = 1 + len / 2;
		low = len / 2;
	}

	if (count >= k) {
		fout << high << " " << low << endl;
		return false;
	}

	m[high] += count;
	m[low] += count;
	k -= count;

	return true;
}

int main() {
	ll T,n,k;
	fin >> T;
	for (ll t = 1; t <= T; t++) {
		fout << "Case #" << t << ": ";

		fin >> n >> k;
		map<ll, ll> m;
		m[n] = 1;
		while (iterate(m,k)) {}
		
	}
}
