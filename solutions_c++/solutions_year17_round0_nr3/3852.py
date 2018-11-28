#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <limits.h>
#include <assert.h>
#include <stack>
#include <cmath>
#include <iomanip>
using namespace std;

int main () {
	long long t;
	cin >> t;
	for(long long tcase = 0; tcase < t; ++tcase) {
		long double result;
		long double N, K;
		cin >> N;
		cin >> K;
		long long min_result = 0;
		long long max_result = 0;
		long double i = N, j = K;
		multiset<long double> intervals;
		intervals.insert(N);
		for(; i > 1 && j > 1; i = *(intervals.rbegin()), --j) {
			long double lower = floor((i - 1)/2.0);
			long double upper = ceil((i - 1)/2.0);
			multiset<long double>::iterator end_element = intervals.end();
			--end_element;
			intervals.erase(end_element);
			intervals.insert(upper);
			intervals.insert(lower);
		}
		if(i > 1) {
			max_result = ceil((i - 1)/2.0);
			min_result = floor((i - 1)/2.0);
		}
		cout << "Case #" << tcase + 1 << ": " << max_result << " " << min_result << "\n";
	}
}
