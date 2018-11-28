#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <numeric>
#include <map>

#pragma warning(disable:4996)
using namespace std;

long long T;
long long N, K;

int main(void)
{
	freopen("./GoogleCodeJam/Input/C-small-2-attempt2.in", "r", stdin);
	freopen("./GoogleCodeJam/Output/C-small-2-ans.txt", "w", stdout);
	cin >> T;

	for (long long t = 0; t < T; ++t) {
		cin >> N >> K;
		long long depth = log2(K);
		double r = log2(K);
		// 0 is none
		int size_odd = 0, size_even = 0, num_odd = 0, num_even = 0;
		
		if (N % 2 == 0) {
			size_even = N;
			num_even = 1;
		}
		else {
			size_odd = N;
			num_odd = 1;
		}
		
		if (size_odd == 1) {
			cout << "Case #" << t + 1 << ": " << 0 << " " << 0 << " " << endl;
			continue;
		}
		if (size_even == 2) {
			if (K == 1) {
				cout << "Case #" << t + 1 << ": " << 1 << " " << 0 << " " << endl;
			}
			else if (K == 2) {
				cout << "Case #" << t + 1 << ": " << 0 << " " << 0 << " " << endl;
			}
			continue;
		}

		for (int d = 1; d <= depth; ++d) {
			int mod = size_odd % 4;
			int p_size_odd = size_odd, p_size_even = size_even, p_num_odd = num_odd, p_num_even = num_even;
			
			int part = p_size_even / 2;
			int even_part, odd_part;
			if (part % 2 == 0) {
				even_part = part;
				odd_part = part - 1;
			}
			else {
				odd_part = part;
				even_part = part - 1;
			}

			if (p_size_odd != 0) {
				if (mod == 3) size_odd = p_size_odd / 2;
				else if (mod == 1) size_even = p_size_odd / 2;
			}
			if (p_size_even != 0) {
				size_odd = odd_part;
				size_even = even_part;
			}
			if (p_size_even == 0) {
				if (mod == 3) size_even = 0;
				else if(mod == 1) size_odd = 0;
			}
			
			num_even = 0; num_odd = 0;
			if (p_num_odd != 0) {
				if (mod == 3) num_odd = 2 * p_num_odd;
				else if(mod == 1) num_even = 2 * p_num_odd;
			}
			//
			if (p_num_even != 0) {
				num_odd += p_num_even;
				num_even += p_num_even;
			}
			//
			if (p_num_even == 0) {
				if (mod == 3) num_even = 0;
				else if(mod == 1) num_odd = 0;
			}

			if (size_odd == 1) {
				depth = d;
				break;
			}
		}

		long long ith = K - (pow(2, depth) - 1);

		long long L, R;
		if (size_odd > size_even) {
			if (ith > num_odd) {
				L = size_even / 2 - 1;
				R = size_even / 2;
			}
			else {
				L = R = size_odd / 2;
			}
		}
		else {
			if (ith > num_even) {
				L = R = size_odd / 2;
			}
			else {
				L = size_even / 2 - 1;
				R = size_even / 2;
			}
		}

		cout << "Case #" << t + 1 << ": " << max(L, R) << " " << min(L, R) << " "  <<  endl;
	}
}