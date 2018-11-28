#include <iostream>
#include <string>

int main() {
	std::ios_base::sync_with_stdio(false);
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		long long N;
		std::cin >> N;
		std::string s = std::to_string(N);
		int j = s.length();
		for (int i = s.length() - 1; i > 0; --i) {
			if (s[i-1] > s[i]) {
				--s[i-1];
				j = i;
			}
		}
		for (int i = j; i < s.length(); ++i)
			s[i] = '9';
		long long ans = std::stoll(s);
		std::cout << "Case #" << t << ": " << ans << std::endl;
	}
	return 0;
}