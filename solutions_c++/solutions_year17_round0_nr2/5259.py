#include <cstdio>
#include <list>

using namespace std;

int main() {
	int t, cs;
	int i;
	int n;
	char c;
	list<char> digits;

	scanf("%d", &t);
	for(cs = 1; cs <= t; cs++) {
		digits.clear();

		while((c = getchar() - '0') < 0 || c > 9);
		while(0 <= c && c <= 9) {
			digits.push_back(c);
			c = getchar() - '0';
		}

		bool borrowed;
		do {
			char lastMax = 0;
			borrowed = false;
			for(auto iter = digits.begin(); iter != digits.end(); ++iter) {
				if(borrowed) {
					*iter = 9;
				} else if(*iter < lastMax) {
					--iter;
					--(*iter);
					borrowed = true;
				} else {
					lastMax = *iter;
				}
			}
		} while(borrowed);

		printf("Case #%d: ", cs);
		bool firstDigit = true;
		for(auto iter = digits.begin(); iter != digits.end(); ++iter) {
			if(firstDigit && *iter == 0) {
				continue;
			}
			firstDigit = false;
			putchar(*iter + '0');
		}
		putchar('\n');
	}
}