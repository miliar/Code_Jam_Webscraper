#include<iostream>

using namespace std;

int main() {
	int cnt;
	cin >> cnt;
	for (int itr = 0; itr < cnt; itr++)
	{
		long long int a, b;
		cin >> a >> b;
		while (b != 1) {
			if (b % 2 == 0) {
				a = (a - 1) / 2 + (a - 1) % 2;
			}
			else {
				a = (a - 1) / 2;
			}
			b = b / 2;
		}
		cout << "Case #" << itr + 1 << ": " << (a - 1) / 2 + (a - 1) % 2 << " " << (a - 1) / 2 << endl;
	}
	return 0;
}