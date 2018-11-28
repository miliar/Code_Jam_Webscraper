#include <iostream>

using namespace std;

int main() {
	int num_test_cases = 0;
	cin >> num_test_cases;
	cin.get();
	for (int t = 1; t <= num_test_cases; t++) {
		char *original = (char *) malloc(sizeof(char) * 19);
		char *num = original;
		char c = 0;
		int location = 0;
		while (cin.get(c)) {
			if (c == ' ' || c == '\n' || c == EOF) break;
			num[location++] = c;
		}

		num[location] = 0;

		untidy:
		for (int i = 1; i < location; i++) {
			if (num[i] < num[i - 1]) {
				for (int j = i; j < location; j++) {
					num[j] = '9';
				}
				num[i - 1]--;
				if (num[0] == '0') {
					location--;
					num++;
				}
				goto untidy;
			}
		}
		cout << "Case #" << t << ": " << num << endl;
		free(original);
	}
	return 0;
}
