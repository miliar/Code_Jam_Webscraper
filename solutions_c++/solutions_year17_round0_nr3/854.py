#include <bits/stdc++.h>

int main(){
	int tests;
	std::cin >> tests;
	for (int test = 0; test < tests; ++test){
		std::cout << "Case #" << test + 1 << ": ";
		long long n, k;
		std::cin >> n >> k;
		std::map<long long, long long> se, next;
		se.insert({- n, 1});
		long long cur = 0;
		while (cur < k){
			for (auto& x : se){
				long long left = (- x.first - 1) / 2;
				long long right = - x.first - 1 - left;
				next[- left] += x.second;
				next[- right] += x.second;
				cur += x.second;
				if (cur >= k){
					std::cout << right << " " << left << "\n";
					break;
				}
			}
			next.swap(se);
			next.clear();
		}
	}
}