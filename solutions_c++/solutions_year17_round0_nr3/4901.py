#include "stdafx.h"
#include <boost/lambda/lambda.hpp>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

class Span
{
public:
	int left;
	int right;
	int length;
	int middleLeft;
	Span(int _left, int _right);
};

Span::Span(int _left, int _right) {
	left = _left;
	right = _right;
	length = _right - _left - 1;
	middleLeft = left + (length / 2 + length % 2);
}

struct LessThanSpan
{
	bool operator()(const Span& span1, const Span& span2) const 
	{
		return (span1.length < span2.length) || ((span1.length == span2.length) && (span1.left > span2.left));
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
	long long t, n, k;
	cin >> t;  
	for (int i = 1; i <= t; ++i) {
		cin >> n >> k; 
		//cout << "n: " << n << " " << "k: " << k << endl;

		if (k >= n) {
			cout << "Case #" << i << ": " << 0 << " " << 0 << endl;
			continue;
		}

		long iterations = 0;
		long long personsWithStall = 0;
		while (personsWithStall + pow(2, iterations) < k) {
			personsWithStall += pow(2, iterations);
			iterations++;
		}

		long long personsWithoutStall = k - personsWithStall;

		long long average = (n - personsWithStall) / (personsWithStall + 1);
		long long extra = (n - personsWithStall) % (personsWithStall + 1);

		long long spanLen;
		if (personsWithoutStall <= extra) {
			spanLen = average + 1;
		}
		else {
			spanLen = average;
		}
		long long leftSpanLen = spanLen / 2 + spanLen % 2 - 1;
		long long rightSpanLen = spanLen - leftSpanLen - 1;

		long long y = max(leftSpanLen, rightSpanLen);
		long long z = min(leftSpanLen, rightSpanLen);

		cout << "Case #" << i << ": " << y << " " << z << endl;
	}
	return 0;
}

