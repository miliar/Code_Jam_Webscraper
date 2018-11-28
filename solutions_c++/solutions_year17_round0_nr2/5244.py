#include <iostream>
#include <string>

using namespace std;

char beforeOf(char);
void setNine(string&, int);

int main() {
	string N;
	int T;

	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> N;

		if (N.size() != 1) {
			for (int i = N.size() - 2; i >= 0; --i) {
				if (N[i] > N[i + 1]) {
					N[i] = beforeOf(N[i]);
					setNine(N, i + 1);
				}
			}
			while (N[0] == '0')
				N.erase(N.begin());
		}

		cout << "Case #" << t << ": " << N << endl;
	}

	return 0;
}


char beforeOf(char c)
{
	if (c >= '1' || c <= '9')
		return c - 1;
	if (c == '0')
		return '9';
	return '?';
}

void setNine(string& number, int start) {
	for (int i = start; i < number.size(); i++)
		number[i] = '9';
}