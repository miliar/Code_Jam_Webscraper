#include <bits/stdc++.h>


int main(){
	int tests;
	std::cin >> tests;
	for (int test = 0; test < tests; ++test){
		std::cout << "Case #" << test + 1 << ": ";
		long long n;
		std::cin >> n;
		std::vector<int> v;
		while (n){
			v.push_back(n % 10);
			n /= 10;
		}
		std::reverse(v.begin(), v.end());
		bool flag = 0;
		while (true){
			flag = 0;
			for (int i = 0; i + 1 < v.size(); ++i){
				if (v[i] > v[i + 1])
					flag = 1;
			}
			if (!flag)
				break;
			flag = 0;
			for (int i = 0; i + 1 < v.size(); ++i){
				if (!flag && v[i] <= v[i + 1])
					continue;
				else if (!flag) {
					flag = 1;
					--v[i];
				} else {
					v[i] = 9;
				}
			}
			if (flag)
				v.back() = 9;
		}
		flag = 0;
		for (int& x : v){
			if (x != 0){
				flag = 1;
				std::cout << x;
			} else if (flag){
				std::cout << x;
			}
		}
		std::cout << "\n";
	}
}