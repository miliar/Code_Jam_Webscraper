#include <bits/stdc++.h>

int main(){
	int tests;
	std::cin >> tests;
	for (int test = 0; test < tests; ++test){
		std::cout << "Case #" << test + 1 << ":\n";
		int r, c;
		std::cin >> r >> c;
		std::vector<std::string> s(r);
		for (int i = 0; i < r; ++i){
			std::cin >> s[i];
		}
		std::set<char> se;
		for (int i = 0; i < r; ++i){
			for (int j = 0; j < c; ++j){
				if (s[i][j] != '?' && !se.count(s[i][j])){
				std::vector<std::vector<int>> above(r, std::vector<int>(c)), below(r, std::vector<int>(c));
					for (int i = 0; i < r; ++i){
						for (int j = 0; j < c; ++j){
							if (s[i][j] == '?'){
								if (i == 0){
									above[i][j] = 1;
								} else {
									above[i][j] = above[i - 1][j] + 1;
								}
							}
						}
					}
					for (int i = r; i--; ){
						for (int j = c; j--; ){
							if (s[i][j] == '?'){
								if (i == r - 1){
									below[i][j] = 1;
								} else {
									below[i][j] = below[i + 1][j] + 1;
								}
							}
						}
					}
					int up = i > 0 ? above[i - 1][j] + 1: 1;
					int down = i < r - 1? below[i + 1][j] + 1: 1;
					int left = 0, right = c;
					for (int k = j; k--; ){
						if (s[i][k] == '?'){
							up = std::min(up, above[i][k]);
							down = std::min(down, below[i][k]);
						} else {
							left = k + 1;
							break;
						}
					}
					for (int k = j + 1; k < c; ++k){
						if (s[i][k] == '?'){
							up = std::min(up, above[i][k]);
							down = std::min(down, below[i][k]);
						} else {
							right = k;
							break;
						}
					}
					for (int k = i - up + 1; k < i + down; ++k){
						for (int l = left; l < right; ++l){
							s[k][l] = s[i][j];
						}
					}
					se.insert(s[i][j]);
				}
			}
		}
		for (int i = 0; i < r; ++i){
			std::cout << s[i] << "\n";
		}
	}
	return 0;
}