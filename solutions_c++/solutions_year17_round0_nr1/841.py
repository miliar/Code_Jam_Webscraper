#include <bits/stdc++.h>

void filp(char& c){
	if (c == '+')
		c = '-';
	else 
		c = '+';
}

int main(){
	int tests;
	std::cin >> tests;
	for (int test = 0; test < tests; ++test){
		std::cout << "Case #" << test + 1 << ": ";
		std::string s;
		int k;
		std::cin >> s >> k;
		int ans = 0;
		for (int i = 0; i + k <= s.size(); ++i){
			if (s[i] == '-'){
				for (int j = i; j < i + k; ++j){
					filp(s[j]);
				}
				++ans;
			}
		}
		bool flag = true;
		for (char& c : s)
			if (c == '-'){
				flag = false;
				break;
			}
		if (flag)
			std::cout << ans << "\n";
		else 
			std::cout << "IMPOSSIBLE\n";
	}
	return 0;
}