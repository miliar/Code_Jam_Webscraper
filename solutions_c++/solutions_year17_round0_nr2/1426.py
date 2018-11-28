#include<iostream>

using namespace std;

int my_strlen(char* input) {
	int idx = 0;
	while (input[idx] != '\0')
		idx++;
	return idx;
}

int main() {
	int cnt;
	cin >> cnt;
	for (int itr = 0; itr < cnt; itr++)
	{
		char* input = new char[20];
		cin >> input;
		int len = my_strlen(input);
		char* result = new char[20];
		int idx = 0;
		while (idx != len) {
			if (idx != len - 1 && input[idx] > input[idx + 1]) {
				while (input[idx] == input[idx - 1])
					idx--;
				result[idx] = (input[idx] - '0' + 9) % 10 + '0';
				for (int i = idx + 1; i < len; i++)
				{
					result[i] = '9';
				}
				break;
			}
			else {
				result[idx] = input[idx];
			}
			idx++;
		}
		cout << "Case #" << itr + 1 << ": ";
		for (int i = 0; i < len; i++)
		{
			if (!(i == 0 && result[0] == '0')) {
				cout << result[i];
			}
		}
		cout << endl;
	}
	return 0;
}