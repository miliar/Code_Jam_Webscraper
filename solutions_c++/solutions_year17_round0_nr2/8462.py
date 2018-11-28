#include <iostream>
#include <string>

using namespace std;


int main()
{
	int T;
	cin >> T;
	int n[T];
	bool ch;
	for (int i = 0; i < T; i++) {
		cin >> n[i];
	}
	for (int t = 0; t < T; t++) {
		for ( int i = n[t]; i > 0; i--) {
			int c = i;
			if (c % 10 != 0) {
				ch = true;
				while (c > 0 && ch) {
					int m = c % 10;
					c = c / 10;
					if (m >= c % 10) {
						ch = true;
					} else {
						ch = false;
						break;
					}
				}
				if (ch) {
					printf("Case #%d: %d\n", t + 1, i);
					break;
				}
			}
		}
	}
	return 0;
}