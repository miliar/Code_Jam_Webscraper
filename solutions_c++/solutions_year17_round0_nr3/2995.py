#include <iostream>
#include <fstream>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <iomanip>


using namespace std;

void solve(long long n, long long k, ostream& out = std::cout) {
	
	long long number = n;
	long long max_count = 1;
	long long min_count = 0;
	while (max_count + min_count < k) {
		k -= max_count + min_count;
		long long a, b;
		if ((n - 1) % 2 == 0) {
			a = 2 * max_count + min_count;
			b = min_count;
			n = (n - 1) / 2;
		} else {
			a = max_count;
			b = max_count + 2 * min_count;
			n = n / 2;
		}
		max_count = a;
		min_count = b;
	}
	--n;
	if (k > max_count) --n;
	out << n / 2 + n % 2 << " " << n / 2 << endl;
	return;
}

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	//cout << fixed << setprecision(10);
	ofstream fout("ouput.txt");
	ifstream fin("input.txt");
	size_t cases;
	long long n, k;
	fin >> cases;
	for (size_t ccase = 0; ccase < cases; ++ccase) {
		fin >> n >> k;
		fout << "Case #" << ccase + 1 << ": ";
		solve(n, k, fout);
	}
	return 0;
}