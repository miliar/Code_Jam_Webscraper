#include <cstdio>
#include <string>

std::string solveOne(std::string s, int len) {
	int count = 0;
	while (true) {
		int pos = (int)s.find('-');
		if (pos == -1) {
			return std::to_string(count);
		}
		if (pos + len > (int)s.size()) {
			return "IMPOSSIBLE";
		}
		for (int i = pos; i < pos + len; i++) {
			s[i] = (char)('+' + '-' - s[i]);
		}
		count++;
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		char buffer[1000 + 1];
		int len;
		scanf("%1000s %d", buffer, &len);
		printf("Case #%d: %s\n", i, solveOne(buffer, len).c_str());
	}
	return 0;
}
