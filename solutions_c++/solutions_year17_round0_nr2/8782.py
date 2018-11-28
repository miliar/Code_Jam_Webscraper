#pragma comment(linker, "/STACK:100000000")
#define _SCL_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#pragma GCC optimize ("O2")
#define _USE_MATH_DEFINES
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <iterator>
#include <ostream>
#include <iomanip>
#include <cstring>
#include <sstream>
#include <cassert>
#include <cstdlib>
#include <istream>
#include <fstream>
#include <climits>
#include <complex>
#include <memory>
#include <string>
#include <bitset>
#include <vector>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef complex <ld> cd;

const bool db = false;

#define fs first
#define sd second
#define mp make_pair
#define pb push_back
#define ppb pop_back

#define inf 1000000007
#define nmax 100100
#define mmax 100100
#define eps 1e-12

vector<int> digits;

int main() {
#ifdef Ahoma
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif // Ahoma
	int tests, count = 0;
	cin >> tests;
	long long num;
	while (tests--) {
		cin >> num;
		count++;
		digits.clear();
		while (num)
			digits.push_back(num % 10), num /= 10;
		reverse(digits.begin(), digits.end());
		int position = 0;
		bool change = false;
		for (position = 0; position < (int)digits.size() - 1; position++) {
			if (digits[position] > digits[position + 1]) {
				change = true;
				break;
			}
		}
		if (change) {
			digits[position]--;
			for (int i = position + 1; i < (int)digits.size(); i++)
				digits[i] = 9;
			while (position && digits[position - 1] > digits[position])
				digits[position - 1]--, digits[position] = 9, position--;
			while (!digits.front())
				digits.erase(digits.begin());
		}
		cout << "Case #" << count << ": ";
		for (int d : digits)
			cout << d;
		cout << '\n';
	}
	return 0;
}