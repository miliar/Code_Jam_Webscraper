#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
	string str;
	fstream result;
	result.open("result.txt", ios::out);

	int t , n, a, b, c, d;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		while (1) {
			a = (n % 10000) / 1000;
			b = (n % 1000) / 100;
			c = (n % 100) / 10;
			d = (n % 10);

			if (a > b || a > c || a > d || b > c || b > d || c > d){
				n--;
			}
			else {
				result << "Case #" << i + 1 << ": " << n << endl;
				break;
			}
		}
	}

	result.close();

	return 0;
}