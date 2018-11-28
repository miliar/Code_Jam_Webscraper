#include <iostream> 
#include <stdlib.h>
#include <string>
#include <math.h>

using namespace std;
int flipPancakes(string str, int num);

void main() {

	unsigned long long int n, num;
	cin >> n;
	string str;
	for (int i = 0; i < n; i++) {
		cin >> str >> num;
		int res = flipPancakes(str, num);
		if (res == -1) {
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		}
		else {
			printf("Case #%d: %d\n", i + 1, res);
		}
	}

}

int flipPancakes(string str, int num) {
	int j, count = 0;
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '-') {
			if (str.length() - i > num -1) {
				for (j = i; j - i < num; j++) {
					if (str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				count++;

			}
			else {
				return -1;
			}
		}
	}
	return count;
}