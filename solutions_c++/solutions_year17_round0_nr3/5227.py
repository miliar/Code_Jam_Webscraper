#include <iostream>
#include <vector>
#include <iterator>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <map>
#include <unordered_map>
#include <cmath>

using namespace std;

long long mypow(int base, int index) {
	long long result = 0;
	if (index == 0)
		return 1;
	if (index == 1)
		return long long(base);
	if (index >= 2) {
		result = long long(base);
		for (int i = 2; i <= index; ++i) {
			result *= base;
		}
		return result;
	}

}

int main()
{
	int t;
	long long left, right;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		left = 0;
		right = 0;
		long long n, k;
		cin >> n >> k;
		
		double fractpart, intpart;
		fractpart = modf(log2(k), &intpart);
		long long nParts; 
		nParts = mypow(2, (int(intpart) + 1));
		long double avgDis = (n - k) / long double (nParts);
		fractpart = modf(avgDis, &intpart);
		if (fractpart >= 0.5) {
			left = floor(avgDis);
			right = ceil(avgDis);
		}
		else {
			left = floor(avgDis);
			right = floor(avgDis);
		}
		

		long long y;
		long long z;
		y = right; // max distance
		z = left; // min distance
		cout << "Case #" << i << ": " << y << " " << z << endl;
	}
	return 0;
}