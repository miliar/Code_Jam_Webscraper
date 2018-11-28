#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <math.h>
#include <time.h>

using namespace std;

void func(vector<int> &arr) {
	for (int i = 1; i < arr.size(); i ++) {
		if (arr[i] < arr[i - 1]) {
			arr[i - 1] --;

			for (int j = i; j < arr.size(); j ++) {
				arr[j] = 9;
			}

			func(arr);
			return;
		}
	}
}


int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int w;
	scanf("%d", &w);

	int t = 1;
	while (t <= w) {
		long long n;
		scanf("%lld", &n);

		vector<int> arr;
		while (n > 0) {
			arr.push_back(n % 10);
			n /= 10;
		}

		reverse(arr.begin(), arr.end());

		func(arr);

		int i = 0;
		while (arr[i] == 0) i ++;

		printf("Case #%d: ", t);
		for (; i < arr.size(); i ++) {
			printf("%d", arr[i]);
		}
		printf("\n");

		t ++;
	}
}