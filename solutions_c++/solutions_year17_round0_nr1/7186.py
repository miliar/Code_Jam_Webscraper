#include <iostream>

using namespace std;

void solve (int num) {
	string s;
	size_t k;

	cin >> s >> k;

	int swaps = 0;

	size_t i;


	for (i=0; i<=s.length() - k; i++) {
		if (s[i] == '-') {
			for (size_t j=i; j<i+k; j++) {
				if (s[j] == '-')
					s[j] = '+';
				else if (s[j] == '+')
					s[j] = '-';
			}
			swaps++;
		}
	}

	bool goodo = true;

	for (;i<s.length(); i++) {
		if (s[i] == '-') {
			goodo = false;
			break;
		}			
	}

	cout << "Case #" << num << ": ";

	if (goodo)
		cout << swaps << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}

int main () {
	int N;
	cin >> N;

	for (int i=0; i<N; i++)
		solve(i+1);

	return 0;
}