#include <iostream>
//#include "stdio.h"
#include <string>
using namespace std;


int main() {
	int t;
	cin >> t;

	long long k, n;
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> n >> k;
		cout << "Case #" << tcount << ": ";

		long long count = 0;
		long long tc = 1;
		long long odd = -1, even = -1;
		long long oc = 0, ec = 0;

		if (n % 2 == 0) {
			even = n;
			ec = 1;
		}
		else {
			odd = n;
			oc = 1;
		}

		while (count + tc < k) {
			//magic
			long long _odd = odd;
			long long _even = even;
			long long _oc = oc;
			long long _ec = ec;

			odd = -1;
			even = -1;
			oc = 0;
			ec = 0;

			if (_oc > 0 && _odd > 0) {
				long long temp = (_odd - 1) / 2;
				if (temp % 2 == 0) {
					even = temp;
					ec += _oc * 2;
				}
				else {
					odd = temp;
					oc += _oc * 2;
				}
			}
			if (_ec > 0 && _even > 0) {
				long long temp = _even / 2;
				if (temp % 2 == 0) {
					even = temp;
					odd = temp - 1;
				}
				else {
					odd = temp;
					even = temp - 1;
				}
				oc += _ec;
				ec += _ec;
			}
			if (oc == 0)
				odd = -1;
			if (ec == 0)
				even = -1;

			count += tc;
			tc *= 2;
		}

		long long left = k - count;

		if (odd > even)
			if (left > oc)
				goto evenend;
			else
				goto oddend;
		else
			if (left > ec)
				goto oddend;
			else
				goto evenend;

	oddend:
		cout << (odd - 1) / 2 << " " <<  (odd - 1) / 2 << endl;
		continue;
	evenend:
		cout << even / 2 << " " << even / 2 - 1 << endl;
		continue;
	}

	return 0;
}