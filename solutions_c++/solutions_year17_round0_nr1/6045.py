#include <iostream>
#include <vector>
using namespace std;

void get_min(string &input, int start, int end, int &ans, int size) {
	while (start <= end && input[start] == '+')
		++start;

	while (start <= end && input[end] == '+')
		--end;

	if (start > end)
		return;

	int diff = end - start + 1;
	if (diff < size)
		ans = -1;
	else {
		for (int i = start; i < start + size; ++i) {
			if (input[i] == '+')
				input[i] = '-';
			else
				input[i] = '+';
		}
		++ans;
		get_min(input, start, end, ans, size);
	}
}

int get_min_flips(string &input, int size) {
	int ans = 0;
	int start = 0;
	int end = input.size() - 1;

	get_min(input, start, end, ans, size);

	return ans;
}

int main()
{
	int T;
	string input;
	int size;

	cin >> T;

	for (int i = 0; i < T; ++i) {
		cin >> input >> size;
		int result = get_min_flips(input, size);

		cout << "Case #" << i + 1 << ": ";
		if (result < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << result << endl;
	}
}
