#include <iostream>
int main() {
	int t;
	std::cin >> t;
	for(int _ = 0;_ < t;_ ++) {
		std::string inp;
		std::cin >> inp;
		int len, ans = 0;
		std::cin >> len;
		for(int i = 0;i <= inp.size() - len;i ++) {
			if(inp[i] == '+') continue;
			ans ++;
			for(int j = 0;j < len;j ++) {
				inp[i+j] = (inp[i+j] == '+' ? '-' : '+');
			}
		}
		bool fail = false;
		for(int i = 0;i < inp.size();i ++) {
			if(inp[i] == '-') {
				fail = true;
				break;
			}
		}
		std::cout << "Case #" << _+1 << ": ";
		if(fail) std::cout << "IMPOSSIBLE";
		else std::cout << ans;
		std::cout << '\n';
	}
	return 0;
}
