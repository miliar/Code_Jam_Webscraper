#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
	int T; // number of tests
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		long long int N;
		long long int K;
		scanf("%lld", &N);
		scanf("%lld", &K);

		long long int h = floor(log2(K));

		long long int num_leaves = pow(2, h);

		long long int remainder = K - (num_leaves-1);

		long long int largest_parent = floor(N / pow(2, h-1));
		long long int b = (largest_parent-1) / 2;
		long long int a = largest_parent - 1 - b;

		long long int c = 0;
		long long int d = 0;
		if (a == b) {
			c = a;
			d = b - 1;
		} else {
			c = b;
			d = b;
		}

		long long int num_large_numebrs = N - d * num_leaves - (num_leaves-1);

		long long int parent = 0;
		if (remainder <= num_large_numebrs) {
			parent = a;
		} else {
			parent = d;
		}

		long long int result_min = (parent - 1) / 2;
		long long int result_max = parent - 1 - result_min;

		cout << "Case #" << i+1 << ": " << result_max << " " << result_min << endl;

	}
}