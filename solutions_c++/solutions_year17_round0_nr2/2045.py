#include <iostream>
#include <fstream>

using namespace std;

unsigned long long reorder(unsigned long long  in, unsigned long long factor) {
	unsigned long long out = (in/factor - 1)*factor + (factor-1);
	return out;
}

int main(int argv, const char **args) {
	ifstream cin(args[1]);
	ofstream cout(args[2]);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		unsigned long long num, res = 0;
		cin >> num;

		unsigned long long factor = 10;
		while (factor <= num) {
			if ((num/factor)%10 > (num/(factor/10))%10) {
				num = reorder(num, factor);
			}
			factor *= 10;
		}
		cout << "Case #" << i << ": " << num << endl;
	}
	return 0;
}