#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void erase_plus();
vector<int> l;

int main() {
	int n, k;
	int result = 0;
	char s[104];

		freopen("A-small-attempt3.in", "r", stdin);
		freopen("output.txt", "w", stdout);


	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		scanf("%s%d", &s, &k);
		for (int j = 0; s[j] != '\0'; j++) {
			if (s[j] == '+') {
				l.push_back(1);
			}
			else {
				l.push_back(-1);
			}
		}


		erase_plus();

		while (l.size()>k) {
			for (int j = 0; j<k; j++) {
				l.at(j) *= -1;
			}
			result += 1;
			erase_plus();
		}

		if (l.size() == 0)
			printf("Case #%d: %d\n", i, result);
		else if (l.size() == k) {
			int num = 0;
			for (int j = 0; j < k; j++) {
				if (l[j] == -1)
					num++;
			}
			if (num == k) {
				result += 1;
				printf("Case #%d: %d\n", i, result);
			}
			else {
				printf("Case #%d: IMPOSSIBLE\n", i);
			}

		}
		else if (l.size() < k) {
			printf("Case #%d: IMPOSSIBLE\n", i);
		}


		result = 0;
		l.clear();
		for (int j = 0; j < 104; j++) {
			s[j] = '\0';
		}
	}
	return 0;

}

void erase_plus() {
	while (1) {
		if (l.size() == 0) {
			break;
		}
		else if (l.at(0) == -1 && l.back() == -1) {
			break;
		}
		if (l.at(0) == 1) {
			l.erase(l.begin());
		}
		else if (l.back() == 1) {
			l.pop_back();
		}
	}
}



